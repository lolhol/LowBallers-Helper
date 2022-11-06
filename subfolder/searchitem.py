import json
from multiprocessing.resource_sharer import stop
from urllib.request import urlopen, Request
from urllib.request import urlopen
from subfolder.subfolder20.uuidStuff.profileUuid import profile_uuid
from subfolder.subfolder20.uuidStuff.acuuid import accountID

item = input("Please enter the item first word in name: \n")

link14 = "https://sky.shiiyu.moe/api/v2/profile/" + accountID

k = urlopen(Request(link14, headers={'User-Agent': 'Mozilla'}))
myfile27 = k.read()
items_profile = json.loads(myfile27)

slot_1_item = items_profile["profiles"][profile_uuid]["items"]["inventory"]

slotItemReforge = input("Does the item have a reforge? (y/n) \n")

for slotitem in slot_1_item:
    if "tag" in slotitem:
        display_name = slotitem["display_name"]
        if item in display_name:
            if slotItemReforge == "n":
                slotitemreforge_new = display_name
                slotitemreforge_new = slotitemreforge_new.replace(" ", "%20")
            if slotItemReforge == "y":
                slotitemreforge = slotitem["extra"]["reforge"]
                first_word = display_name.split()[0]
                slotitemreforge_new = display_name.replace(first_word + " ", "")
                slotitemreforge_new = slotitemreforge_new.replace(" ", "%20")
                slotitemreforge_new = slotitemreforge_new.replace("✪", "")
            break

##item_recombobulated = slotitem[""]

itemlist = ("untimate_bank", "ultimate_combo", "ultimate_chrimera", "ultimate_duplex", "ultimate_soul_eater", "ultimate_bobbin_time", "ultimate_fatal_tempo", "ultimate_habanero_tactics","ultimate_inferno", "ultimate_last_stand", "ultimate_legion", "ultimate_one_for_all", "ultimate_swarm", "ultimate_wise", "ultimate_wisdom")
item_list_gems = ("SAPPHIRE_0", "JADE_0", "AMBER_0", "TOPAZ_0", "AMETHIST_0", "JASPER_0", "RUBY_0")

recombobulated = slotitem["recombobulated"]

ExtraA = slotitem["tag"]["ExtraAttributes"]
ExtraO = slotitem["extra"]

if 'gems' in ExtraO.keys():

    gems_thing = slotitem["extra"]["gems"]
    for y in item_list_gems:
        if y in gems_thing:
            gems_thing_perfect = slotitem["extra"]["gems"][y]
            if gems_thing_perfect == "PERFECT":
                perfect_gem = gems_thing_perfect + "_" + y
                perfect_gem = perfect_gem.replace("_0", "")
                perfect_gem = perfect_gem + "_GEM"
                perfect_gem1 = "stop"
else:
    perfect_gem = 0

if 'enchantments' in ExtraA.keys():
    enchants = slotitem["tag"]["ExtraAttributes"]["enchantments"]

    for x in itemlist:
        if x in enchants:
            ultimate_enchant = x 
            enchant_number = slotitem["tag"]["ExtraAttributes"]["enchantments"][ultimate_enchant]
            enchant_number = str(enchant_number)
            ultimate_enchant = ultimate_enchant.upper()
            ultimate_enchant = "ENCHANTMENT_" + ultimate_enchant + "_" + enchant_number
            ultimate_enchant1 = "stop"
else: 
    ultimate_enchant = 0