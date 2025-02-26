import json
from pprint import pprint

with open("./offers.json", "r") as f:
    data = json.loads(f.read())

data = data[0]
processed_data = []

for benefit in data["benefits"]:
    name = benefit["value"]
    price = benefit["price"]
    desc = benefit["description"]

    d = dict()
    d["name"] = name
    d["price"] = price
    d["desc"] = desc

    processed_data.append(d)


with open("offers_processed.json", "w") as f:
    f.write(json.dumps(processed_data))