# Application to check YuGiOh card prices based on a wishlist file
# Usage: Enter desired cards in wishlist.tsv in this format:
# CARD NAME TARGET_PRICE
# Name should be entered exactly as it appears on yugiohprices.com
# Notifications will trigger if a card is found listed below its current target

import json
import os.path
import sys
import smtplib
from email.message import EmailMessage
from ygo_api import YgoApi

base_url = "http://yugiohprices.com/api/"
filename = "./wishlist.tsv"
hit = []
notifs = []
errors = []
notif_string = ""
lowest_found = 0

with open(filename, 'r') as wishlist:
    for card in wishlist:
        tokens = card.split('\t')
        if len(tokens) != 3:
            print("Invalid format. Valid format is NAME TARGET_PRICE TARGET_RARITY")
            print("Use * for any rarity")
            errors.append("Error with card " + tokens[0])
        else:
            lowest_found = sys.maxsize
            card_name = tokens[0]
            target_price = float(tokens[1])
            target_rarity = tokens[2].strip() # remove endline character
            # Acquire and format data
            data = str(YgoApi.get_price_by_name(card_name, base_url))
            data = data.replace('\'', '\"')
            pdata = json.loads(data)
            listings = pdata["data"]
            # Look for prices @ target rarity
            rarity = ""
            price_low = -1
            for entry in listings:
                rarity = entry["rarity"]
                price_low = entry["price_data"]["data"]["prices"]["low"]
                if price_low <= target_price and (target_rarity == "*" or rarity == target_rarity):
                    # We only want the lowest price available
                    if price_low < lowest_found:
                        lowest_found = price_low
                        hit = entry
            notif_string = "Found " + card_name + " in rarity " + hit["rarity"] + " for $" + str(lowest_found)
            notifs.append(notif_string)

'''
Handle email sending
'''
if len(notifs) > 0:
    sender = "noreply@kame-game.net"
    recipient = "test@example.org"
    subject = "Yu-Gi-Oh Price Alert"
    body = "Subject: " + subject + "\n"
    for item in notifs:
        body = body + item + "\n"
    body = body + "\nSincerely,\nKame Game Staff"

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP('localhost')
        server.sendmail(sender, recipient, body)
        server.quit()
        print("Notification sent")
    except Exception:
        print(sys.exc_info())
        print("Connection error. Exiting...")
else:
    print("Nothing to report")
