# ygo-check
Keeping track of price swings makes it difficult to concentrate on children's card games.

## Usage
Edit wishlist.tsv to contain the cards on your buy list along with the desired
price and rarity. Format is

CARD_NAME   TARGET_PRICE    TARGET_RARITY

Use '\*' to indicate any available rarity.

This script assumes that it will be run on a system configured as a SMTP server.
Modify the recipient address in ygo_check.py to your desired receiving address.

## Credits
Using the yugiohprices.com API to retrieve card price data.
API specification available at https://yugiohprices.docs.apiary.io/
