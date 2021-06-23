import json
import requests
import re
import os
import sys
import logging
from utils import get_psm_config
import warnings
warnings.simplefilter("ignore")

HOME = os.environ["HOME"]
psm_config_path = HOME+"/.psm/config.json"
psm_config = {}

def downloadSwaggerFiles():
    host = psm_config["psm-ip"]
    if not os.path.exists("swagger"):
        os.mkdir("swagger")

    response = requests.get("https://"+host+"/docs/generated/swaggeruri.html", verify=False)
    matches = re.findall("href=\"([^\"]*)", response.text)

    for match in matches:
        resp = requests.get("https://"+host+match, verify=False)
        filename = match.replace("/swagger/", "")
        jsondata = processSwagger(filename, resp.json())
        with open("swagger/"+filename+".json", "w") as f:
            json.dump(jsondata, f, indent=4)

def removeRequired(filename, jsondata):
    for key in jsondata["definitions"]:
        if "required" in jsondata["definitions"][key] and len(jsondata["definitions"][key]["required"]):
            print(filename, key, jsondata["definitions"][key]["required"])
            jsondata["definitions"][key]["required"] = []
    return jsondata

def processSwagger(filename, jsondata):

    jsondata = removeRequired(filename, jsondata)
    if filename == "fwlog":
        # fwlog api group
        # remove minLength for fwlogList
        del jsondata["definitions"]["apiListWatchOptions"]["properties"]["name"]["minLength"]
        del jsondata["definitions"]["apiListWatchOptions"]["properties"]["tenant"]["minLength"]
        del jsondata["definitions"]["apiListWatchOptions"]["properties"]["namespace"]["minLength"]
        del jsondata["definitions"]["apiListWatchOptions"]["properties"]["name"]["pattern"]
        del jsondata["definitions"]["apiListWatchOptions"]["properties"]["tenant"]["pattern"]
        del jsondata["definitions"]["apiListWatchOptions"]["properties"]["namespace"]["pattern"]

        del jsondata["definitions"]["apiObjectMeta"]["properties"]["name"]["minLength"]
        del jsondata["definitions"]["apiObjectMeta"]["properties"]["tenant"]["minLength"]
        del jsondata["definitions"]["apiObjectMeta"]["properties"]["namespace"]["minLength"]
        del jsondata["definitions"]["apiObjectMeta"]["properties"]["name"]["pattern"]
        del jsondata["definitions"]["apiObjectMeta"]["properties"]["tenant"]["pattern"]
        del jsondata["definitions"]["apiObjectMeta"]["properties"]["namespace"]["pattern"]
    if filename == "objstore":
        del jsondata["paths"]["/objstore/v1/uploads/snapshots"]
        del jsondata["paths"]["/objstore/v1/uploads/images"]
    return jsondata

if __name__ == "__main__":
    psm_config = get_psm_config()
    downloadSwaggerFiles()
