from web3 import Web3
from config.settings import RPC_URL

def get_web3():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        raise Exception("RPC connection failed")
    return w3
