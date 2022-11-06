from urllib.request import urlopen, Request
import json
from subfolder.subfolder20.uuidStuff.acuuid import accountID
import os
import time
import time
import os.path
from pathlib import Path
import os.path

current_time = time.time()
current_time1 = str(current_time)

if os.path.exists("/text.txt") == "False":
    key = input("Please paste an api key here -- ")

    with open("test.txt",'w') as b:
        b.write(current_time1 + "\n" + key)
    content_test = key

file = open('test.txt')
content_test_file = file.read()
slice = "\n"
content_test_file1 = content_test_file.split(slice, 1)[0]
content_test = content_test_file.split(slice, 1)[1]
slice1 = "."
content_test_file0 = content_test_file1.split(slice1, 1)[0]
content_test_file_int = int(content_test_file0)

current__time = current_time1.split(slice1, 1)[0]
current_time2 = int(current__time)

timeuntill_runout = current_time2 - content_test_file_int

if timeuntill_runout > 3600:
    key = input("Please paste an api key here -- ")

    with open("test.txt",'w') as f:
        f.write(current_time1 + "\n" + key)
    content_test = key
else:
    pass
    
    
# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
try:
    link11 = "https://api.hypixel.net/skyblock/profiles?key=" + content_test + "&uuid=" + accountID
    m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
    myfile2 = m.read()
    profile3 = json.loads(myfile2) 
except:
    key = input("Please paste an api key here -- ")

    with open("test.txt",'w') as f:
        f.write(current_time1 + "\n" + key)
    content_test = key



# apiKey = input("Please enter api key:\n")

file = open('test.txt')
content_test_file = file.read()
slice = "\n"
content_test = content_test_file.split(slice, 1)[1]

# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
file = open('test.txt')
content_test_file = file.read()
    
link11 = "https://api.hypixel.net/skyblock/profiles?key=" + content_test + "&uuid=" + accountID

m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
myfile2 = m.read()
profile3 = json.loads(myfile2)    

profile_uuid_pre0 = profile3["profiles"]

for x in profile_uuid_pre0:
    if "selected" in x:
        selectedtrue = x["selected"]
        if selectedtrue == True:
            profile_uuid = x["profile_id"]
        if selectedtrue == False:
            continue
    break
    