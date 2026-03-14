import pandas as pd
from ingestion.rpc_client import get_web3
from config.settings import DATA_RAW_PATH

def fetch_swaps():

    w3 = get_web3()

    # example mock data (replace with real event query)
    swaps = [
        {"trader": "0xabc", "pair": "ETH/USDC", "amount_usd": 120000},
        {"trader": "0xdef", "pair": "ETH/USDC", "amount_usd": 2000},
        {"trader": "0xghi", "pair": "WBTC/USDC", "amount_usd": 54000},
    ]

    df = pd.DataFrame(swaps)
    df.to_csv(DATA_RAW_PATH, index=False)

    print("Swaps saved")

if __name__ == "__main__":
    fetch_swaps()
