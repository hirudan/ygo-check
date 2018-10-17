#
# Wrapper class for the yugiohprices api
#
import requests

class YgoApi(object):

    # Gets the price of a card by its name
    # param name: The name of the card to get
    # param base_url: the api endpoint to pull from
    # Returns: a json blob of the response
    @staticmethod
    def get_price_by_name(name, base_url):
        url = "get_card_prices/"
        r = requests.get(base_url+url+name)
        return r.json()

    # Gets the price of a card by its print tag
    # param tag: The print tag of the card to get
    # param base_url: the api endpoint to pull from
    # Returns: a json blob of the response
    @staticmethod
    def get_price_by_print_tag(tag, base_url):
        url = "price_for_print_tag/"
        r = requests.get(base_url+url+tag)
        return r.json()

    # Gets price history by print tag and rarity
    # param tag: The print tag of the card to get
    # param rarity: The rarity of the card to get
    # param base_url: the api endpoint to pull from
    # Returns: a json blob of the response
    @staticmethod
    def get_price_by_rarity(tag, rarity, base_url):
        payload = {'rarity' : rarity}
        url = "price_history/"
        r = requests.get(base_url+url+tag, params=payload)
        return r.json()
