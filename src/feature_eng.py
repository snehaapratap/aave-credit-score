import pandas as pd

_TX_TYPES = ["deposit", "borrow", "repay",
             "redeemunderlying", "liquidationcall"]

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    # basic aggregates
    g = df.groupby("user_address")
    feats = pd.DataFrame(index=g.size().index)

    # 1. volume features
    for t in _TX_TYPES:
        feats[f"{t}_cnt"] = g.apply(lambda x, tt=t: (x["action"] == tt).sum())
        feats[f"{t}_vol"] = g.apply(
            lambda x, tt=t: x.loc[x["action"] == tt, "amount"].sum())

    # 2. behavioural ratios
    feats["borrow_repay_ratio"] = (
        feats["repay_vol"] / feats["borrow_vol"].replace(0, 1))

    feats["liquidation_rate"] = (
        feats["liquidationcall_cnt"] / g.size())

    # 3. temporal
    df["block_ts"] = pd.to_datetime(df["timestamp"], unit="s")
    feats["lifetime_days"] = (
        g["block_ts"].max() - g["block_ts"].min()).dt.days.clip(lower=1)

    # 4. activeness
    feats["tx_per_day"] = g.size() / feats["lifetime_days"]
    return feats.fillna(0)
