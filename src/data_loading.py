import json
import gzip
from pathlib import Path
import pandas as pd

def load_tx(path: str | Path) -> pd.DataFrame:
    p = Path(path)
    with open(p, "r") as f:
        first_char = f.read(1)
        f.seek(0)
        if first_char == "[":
            data = json.load(f)
        else:
            data = [json.loads(line) for line in f if line.strip()]
    return pd.DataFrame(data)
