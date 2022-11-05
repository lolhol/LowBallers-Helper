import profile
from urllib.request import urlopen, Request
import json
import ssl
from subfolder20.uuidStuff.acuuid import accountID


def read_link_profileUUID():
# apiKey = input("Please enter api key:\n")

    key = input("Please paste an api key here.")

    with open("test.txt",'w') as f:
        f.write(key)

    file = open('test.txt')
    content_test_file = file.read()

# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
    link11 = "https://api.hypixel.net/skyblock/profiles?key=" + content_test_file + "&uuid=" + accountID

    m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
    myfile2 = m.read()
    profile3 = json.loads(myfile2) 
    return profile3


def profileUuid():
# apiKey = input("Please enter api key:\n")

# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
    file = open('test.txt')
    content_test_file = file.read()
    
    link11 = "https://api.hypixel.net/skyblock/profiles?key=" + content_test_file + "&uuid=" + accountID

    m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
    myfile2 = m.read()
    profile3 = json.loads(myfile2)  

    profile_uuid_pre = profile3["profiles"]

## error - fix here <----------

    for x in profile_uuid_pre:
        profile5 = profile_uuid_pre[x]
        if profile5["selected"] == False:
            pass
        if profile5["selected"] == True:
            profile_uuid = x
        break
    return profile_uuid

