import requests

PUB_API_BASE_URL = "https://www.coinspot.com.au/pubapi/v2" 

class PublicCoinspotAPI():
    """Gives access to all public Coinspot API
    """
    def latest_prices(self) -> requests.Response:
        """
        https://www.coinspot.com.au/v2/api#latestprices
        
        Returns:
            requests.Response
        """
        
        return requests.get(f"{PUB_API_BASE_URL}/latest")
    
    def latest_coin_price(self, coin) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestpricescoin
        
        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/latest/" + coin)
    
    def latest_coin_market_price(self, coin, market) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestpricescoinmarket

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'
            markettype (string): market coin short name, example value 'USDT' (only for available markets)

        Returns:
            requests.Response 
        """
        
        return requests.get(PUB_API_BASE_URL + "/latest/" + f"{coin}/{market}")
    
    def latest_buy_price(self, coin) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestbuyprice

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/buyprice/" + coin)
    
    def latest_buy_market_price(self, coin, market) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestbuypricenonfiat

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'
            market (string): coin market you wish to use to buy it, example value: USDT' (only for available markets)

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/buyprice/" + f"{coin}/{market}")
    
    def latest_sell_price(self, coin) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestsellprice

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/sellprice/" + coin)
    
    def latest_sell_market_price(self, coin, market) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#latestsellpricenonfiat

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'
            market (string): coin market you wish to sell it for, example value: 'USDT' (note: only for available markets)

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/sellprice/" + f"{coin}/{market}")
    
    def open_orders_coin(self, coin) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#openorders

        Args:
            coin (string): the coin short name, example value 'BTC', 'LTC', 'DOGE'

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/orders/open/" + {coin})
    
    def open_orders_coin_market(self, coin, market) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#openordersmarket

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'
            market (string): coin market, example values 'USDT' (note: only for available markets)

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/orders/open/" + f"{coin}/{market}")
    
    def completed_orders_coin(self, coin) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#historders

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "orders/completed/" + coin)
    
    def completed_orders_coin_market(self, coin, market) -> requests.Response:
        """https://www.coinspot.com.au/v2/api#histordersmarket

        Args:
            coin (string): coin short name, example value 'BTC', 'LTC', 'DOGE'
            market (string): coin market, example values 'USDT' (note: only for available markets)

        Returns:
            requests.Response
        """
        
        return requests.get(PUB_API_BASE_URL + "/orders/completed/" + f"{coin}/{market}")