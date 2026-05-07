import polars as pl
import re

def load_data(file: str):
    c = pl.scan_ndjson(file).select(["id", "url", "created_utc", "num_comments", "title", "selftext"])
    df = c.collect()
    df = df.rename({"created_utc":"created", "selftext":"text"})
    return df

def process_data(file: str, hw: str, aw: str):
    submissions = load_data(file)

    with open(hw, 'r', encoding='utf-8') as hf:
        hterms = [line.rstrip() for line in hf]
    hpattern = r"(?i)(" + "|".join(map(re.escape, hterms)) + r")"
    filtered_lf = submissions.filter(pl.col("title").fill_null("").str.contains(hpattern))

    filtered_lf = filtered_lf.with_columns(
        created_dt = pl.from_epoch(pl.col("created"), time_unit="s"),
        year       = pl.from_epoch(pl.col("created"), time_unit="s").dt.year(),
        month      = pl.from_epoch(pl.col("created"), time_unit="s").dt.month(),
        )
    lf_sorted = filtered_lf.sort(
        by=["year", "month", "n_comments"],
        descending=[False, False, True],
        )
    lf_sorted = lf_sorted.remove(pl.col("n_comments") == 0)

    with open(aw, 'r', encoding='utf-8') as af:
        aterms = [line.rstrip() for line in af]
    apattern = r"(?i)(" + "|".join(map(re.escape, aterms)) + r")" 
    sorted_flf = lf_sorted.filter(pl.col("title").fill_null("").str.contains(apattern))

    top_per_year = (sorted_flf
    .sort(["year", "n_comments"], descending=[False, True])
    .group_by("year", maintain_order=True)
    .head(5)
    )

    return top_per_year

if __name__ == '__main__':
    fpath = 'raw file path in json'
    housing_file = 'housing_en.txt'
    afford_file = 'afford_en.txt'
    opath = 'out.csv'

    filtered = process_data(fpath, housing_file, afford_file)
    filtered.write_csv(opath)