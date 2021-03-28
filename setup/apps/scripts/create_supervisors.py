import os
import json
import requests


specs_path = "/specs"

druid_url = "http://" + os.environ["DRUID_URL"] + "/druid/indexer/v1/supervisor"

headers = {"Content-Type": "application/json"}

json_files = [pos_json for pos_json in os.listdir(specs_path)
                            if pos_json.endswith('.json')]

for jf in json_files:
    with open(specs_path + "/" +  jf, "r") as f:
        sp = json.load(f)
    r = requests.post(druid_url, json.dumps(sp), headers=headers)
    print("Spec " + jf + "status" + str(r.status_code))

