from ygo_api import YgoApi

base_url = "http://yugiohprices.com/api/"

print(YgoApi.get_price_by_name("Divine Grace - Northwemko", base_url))

print(YgoApi.get_price_by_print_tag("SOVR-EN039", base_url))

print(YgoApi.get_price_by_rarity("SOVR-EN039", "Ultra Rare", base_url))
