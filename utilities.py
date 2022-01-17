import json
import requests


def get_rarity():

    # JSON file
    f = open("page-data.json", "r")

    # Reading from file
    data = json.loads(f.read())

    # Iterating through the json
    categories = {}

    # Get category dictionary into percentage format
    for i in data["result"]["pageContext"]["collectionInfo"]["attributeCategories"]:
        temp = {}
        temp2 = {}
        for x in i["values"]:
            temp[x["value"]] = x["count"]
        # convert temp into percentages
        s = sum(temp.values())
        for k, v in temp.items():
            pct = v * 100.0 / s
            temp2[k] = pct
        categories[i["type"]] = temp2

    # Closing file
    f.close()
    return categories


def ranking(rarity):
    pass
