import polars as pl
import re

def load_data(file: str):
    c = pl.scan_ndjson(file).select(["id", "link_id", "created_utc", "score", "body"])
    df = c.collect()
    df = df.rename({"link_id":"thread_id", "created_utc":"created", "body":"text"})
    return df

def process_data(coms: str, subs: str):
    comments = load_data(coms)
    comments = comments.with_columns(
        pl.col("thread_id")
        .str.strip_prefix("t3_")
        .alias("thread_id")
        )
    
    threads = pl.read_csv(subs)
    sub_ids = set(pl.Series(threads.select('id')).to_list())

    coms_filtered = comments.filter(
    pl.col("thread_id").is_in(list(sub_ids))
    )
    coms_filtered = coms_filtered.with_columns(
    created_dt = pl.from_epoch(pl.col("created"), time_unit="s"),
    year       = pl.from_epoch(pl.col("created"), time_unit="s").dt.year(),
    month      = pl.from_epoch(pl.col("created"), time_unit="s").dt.month(),
    )
    lf_sorted = coms_filtered.sort(
    by=["year", "month", "score"],
    descending=[False, False, True],
    )

    return lf_sorted

if __name__ == '__main__':
    cpath = 'path for comments file in csv'
    spath = 'path for submissions file in csv'
    opath = 'output path in csv'

    filtered = process_data(cpath, spath)
    filtered.write_csv(opath)