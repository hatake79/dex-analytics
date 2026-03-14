import pandas as pd
from config.settings import DATA_PROCESSED_PATH

def calculate_volume():

    df = pd.read_csv(DATA_PROCESSED_PATH)

    total_volume = df["amount_usd"].sum()

    volume_by_pair = df.groupby("pair")["amount_usd"].sum()

    print("Total Volume:", total_volume)
    print("Volume by pair")
    print(volume_by_pair)

if __name__ == "__main__":
    calculate_volume()
