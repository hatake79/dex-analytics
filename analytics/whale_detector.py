import pandas as pd
from config.settings import DATA_PROCESSED_PATH, SWAP_THRESHOLD_USD

def detect_whales():

    df = pd.read_csv(DATA_PROCESSED_PATH)

    whales = df[df["amount_usd"] > SWAP_THRESHOLD_USD]

    print("Whale Trades")
    print(whales)

if __name__ == "__main__":
    detect_whales()
