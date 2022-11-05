from urllib.request import urlopen, Request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input the account name
accountName = input("Please enter the account ign:\n")

# Looks up mc uuid on mc official website
mc_uuid_link = "https://api.mojang.com/users/profiles/minecraft/" + accountName

# Opens url above
mc_uuid_urlopen = urlopen(
    Request(mc_uuid_link, headers={'User-Agent': 'Mozilla'}))
mc_uuid_file = mc_uuid_urlopen.read()
mc_uuid_profile = json.loads(mc_uuid_file)

# Figures out what the account uuid is
accountID = mc_uuid_profile['id']

# Prints "The token of the account that you have just entered is <account token>"
# print('The token of the account that you have just entered is ' + accountID)
