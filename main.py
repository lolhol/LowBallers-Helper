import time
import random
import json
from urllib.request import urlopen, Request
from urllib.request import urlopen
from subfolder.searchitem import slotitemreforge_new, recombobulated
from subfolder.enchantPrices.recomPrice import item_recom_price, item_enchant_price

ah_link = "https://sky.coflnet.com/api/auctions/tag/" + slotitemreforge_new + "/active/bin"

ah_urlopen = urlopen(Request(ah_link, headers={'User-Agent': 'Mozilla'}))
ah_url_file = ah_urlopen.read()
ah_item_price = json.loads(ah_url_file)

for x in range(100):
    time.sleep(0.01)
    print(random.randint(1000000000000000,1000000000000000000000000000000000000))

# Finds the EXACT price of a given item
ah_item_price_final = ah_item_price[1]["startingBid"]

finall_price = ah_item_price_final + item_enchant_price

if recombobulated == "true":
    finall_pricw = finall_price + item_recom_price
else:
    print(" ")
    time.sleep(0.1)
    print("YOUR TOTAL ITEM PRICE IS... ")
    for y in range(3):
        print("...")
        time.sleep(1)
    print(finall_price, "coins")


