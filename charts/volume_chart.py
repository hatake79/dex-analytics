import pandas as pd
import matplotlib.pyplot as plt
from config.settings import DATA_PROCESSED_PATH

def plot_volume():

    df = pd.read_csv(DATA_PROCESSED_PATH)

    volume = df.groupby("pair")["amount_usd"].sum()

    volume.plot(kind="bar")

    plt.title("DEX Volume by Pair")
    plt.ylabel("USD Volume")
    plt.show()

if __name__ == "__main__":
    plot_volume()
