import pandas as pd

def calculate_metrics(matches):
    df = pd.DataFrame(matches)

    kd = df["kills"].sum() / max(df["deaths"].sum(), 1)
    win_rate = df["win"].mean() * 100

    early_death_percent = (
        (df["death_time"] < 30).sum() / len(df)
    ) * 100

    fatigue_slope = (
        df["kills"].rolling(3).mean().diff().mean()
    )

    tilt_index = df["deaths"].diff().clip(lower=0).mean()

    return {
        "kd": kd,
        "win_rate": win_rate,
        "early_death_percent": early_death_percent,
        "fatigue_slope": fatigue_slope,
        "tilt_index": tilt_index
    }
