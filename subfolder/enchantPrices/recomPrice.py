import profile
from urllib.request import urlopen, Request
import json
import ssl
from subfolder20.uuidStuff.acuuid import accountID
from searchItemsBazar import bz_recombobulator
from subfolder20.uuidStuff.profileUuid import profile_uuid

# apiKey = input("Please enter api key:\n")

# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
link11 = "https://api.hypixel.net/skyblock/bazaar"

def recompricefunc():
    m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
    myfile2 = m.read()
    profile4 = json.loads(myfile2)

    item_recom = profile4["producs"]["RECOMBOBULATOR_3000"]["sell_summery"]

    if item_recom:
        price1 = bz_recombobulator
    else:
        price1 = 0

# add 50 to recom price.
