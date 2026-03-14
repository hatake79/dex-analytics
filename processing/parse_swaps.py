import pandas as pd
from config.settings import DATA_RAW_PATH, DATA_PROCESSED_PATH

def process_swaps():

    df = pd.read_csv(DATA_RAW_PATH)

    df["is_whale"] = df["amount_usd"] > 100000

    df.to_csv(DATA_PROCESSED_PATH, index=False)

    print("Processed swaps saved")

if __name__ == "__main__":
    process_swaps()
