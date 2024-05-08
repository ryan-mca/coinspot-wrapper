import requests

PUB_API_BASE_URL = "https://www.coinspot.com.au/pubapi/v2" 

class PublicCoinspotAPI():
    """Gives access to all public Coinspot API
    """
    def latest_prices(self) -> requests.Response:
        """
        https://www.coinspot.com.au/v2/api#latestprices
        
        Returns:
            requests.Response: A response containing all coin price data
        """
        
        return requests.get(f"{PUB_API_BASE_URL}/latest")
    
    def latest_coin_price(self, coin) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestpricescoin
        
        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'

        Returns:
            requests.Response: A response containing coin price data
        """
        
        return requests.get(PUB_API_BASE_URL + "/latest/" + coin)
    
    def latest_coin_market_price(self, coin, markettype) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestpricescoinmarket

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'
            markettype (string): market coin short name, example value 'USDT' (only for available markets)

        Returns:
            requests.Response: object with set of properties for coin with latest buy, ask and last prices 
        """
        
        return requests.get(PUB_API_BASE_URL + "/latest" + f"/{coin}/{markettype}")
    
    def latest_buy_price(self, coin) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestbuyprice

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'

        Returns:
            requests.Response: _description_
        """