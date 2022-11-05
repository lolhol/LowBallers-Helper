import imp
from multiprocessing.resource_sharer import stop
from urllib.request import urlopen, Request
import ssl
from urllib.request import urlopen
import json
from subfolder20.uuidStuff.profileUuid import read_link_profileUUID
from subfolder20.uuidStuff.profileUuid import profileUuid
import os
import sys

profile3 = read_link_profileUUID()
profile_uuid = profileUuid()

item = input("Please enter the item first word in name:\n")

slot_1_item = profile3["profiles"][profile_uuid]["items"]["inventory"]

slotItemReforge = input("Does the item have a reforge? (y/n) \n")

for x in slot_1_item:
  if "tag" in x:
    slotitem = x
    slotitem1 = slotitem["display_name"]
    if slotItemReforge == "n":
      slotitemreforge_new = slotitem1
    if slotItemReforge == "y":
      print(slotItemReforge)
      slotitemreforge = slotitem["extra"]["reforge"]
      first_word = slotitem1.split()[0]
      no_caps = first_word.lower()
    break 


