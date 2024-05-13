"""
Gives access to CoinSpots APIs

Only supports API V2

Classes:
    PublicCoinspotAPI()
    CoinspotAPI()
    ROCoinspotAPI()
"""

import hmac
import json
import time
import hashlib
import requests

PUB_API_BASE_URL = "https://www.coinspot.com.au/pubapi/v2"
RO_API_BASE_URL = "https://www.coinspot.com.au/api/v2/ro"
API_BASE_URL = "https://www.coinspot.com.au/api/v2"

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

class ROCoinspotAPI():
    def __init__(self, pub_key, priv_key) -> None:
        self.pub_key = pub_key
        self.priv_key = priv_key
    
    def _create_hmac(self, postdata):
        return hmac.new(self.priv_key.encode("utf-8"), json.dumps(postdata, separators=(",", ":")).encode("utf-8"), hashlib.sha512).hexdigest()
    
    def _create_headers(self, sign):
        return {
            "Content-type": "application/json",
            "Accept": "text/plain",
            "key": self.pub_key,
            "sign": sign
        }
    
    def read_only_status_check(self):
        postdata = {
            "nonce": int(time.time()*1000000)
        }
        
        sign = self._create_hmac(postdata)
        
        headers = self._create_headers(sign)
        
        return requests.post(RO_API_BASE_URL + "/status", headers=headers, data=json.dumps(postdata))
