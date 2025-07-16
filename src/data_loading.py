import json
import gzip
from pathlib import Path
import pandas as pd

def load_tx(path: str | Path, chunksize: int = 1_000_000) -> pd.DataFrame:
    p = Path(path)
    open_fn = gzip.open if p.suffix == ".gz" else open
    rows = []
    with open_fn(p, "rt") as f:
        for line in f:
            rows.append(json.loads(line))
    return pd.DataFrame(rows)
