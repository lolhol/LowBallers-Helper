from urllib.request import urlopen
import json

# Opens this link to check bz prices
link = "https://api.hypixel.net/skyblock/bazaar"

f = urlopen(link)
myfile = f.read()
bz = json.loads(myfile)

# Finds the EXACT price of a given item
bz_recombobulator = bz["products"]["RECOMBOBULATOR_3000"]["quick_status"]["buyPrice"]
