import requests

PUB_API_BASE_URL = "https://www.coinspot.com.au/pubapi/v2" 

class PublicCoinspotAPI():
    """Gives access to all Coinspot API
    """
    def latest_prices(self) -> requests.Response:
        """
        status - ok, error
        message - ok, description of error if error occurred
        prices - array of objects with one set of properties for each coin with latest buy and sell prices, non aud markets are symbolised by (e.g.) 'btc_usdt'
        """
        
        return requests.get(f"{PUB_API_BASE_URL}/latest")
    
