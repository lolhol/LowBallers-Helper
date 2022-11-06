from urllib.request import urlopen, Request
import json
from subfolder.searchitem import ultimate_enchant, ultimate_enchant1


# apiKey = input("Please enter api key:\n")

# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
link11 = "https://api.hypixel.net/skyblock/bazaar"


m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
myfile2 = m.read()
profile4 = json.loads(myfile2)

item_recom_price = profile4["products"]["RECOMBOBULATOR_3000"]["sell_summary"][0]["pricePerUnit"]

if ultimate_enchant1 == "stop": 
    item_enchant_price = profile4["products"][ultimate_enchant]["sell_summary"][0]["pricePerUnit"]
    item_enchant_price = int(item_enchant_price)
else:
    item_enchant_price = 0

