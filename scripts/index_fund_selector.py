import requests
from pprint import pprint
import pandas as pd

headers = {
    'content-type': 'application/json',
    'origin': 'https://www.tickertape.in',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

json_data = {
    'match': {
        'option': [
            'Growth',
        ],
        'subsector': [
            'Index Fund',
        ],
    },
    'sortBy': 'aum',
    'sortOrder': -1,
    'project': [
        'subsector',
        'option',
        'aum',
        'expRatio',
        'trackErr',
    ],
    'offset': 0,
    'count': 200,
    'mfIds': [],
}

resp = requests.post('https://api.tickertape.in/mf-screener/query',  headers=headers, json=json_data)

data = resp.json()["data"].get("result")

# pprint(data)
processed_data = []

for row in data:
    d = dict()
    d["name"] = row["name"]
    for v in row["values"]:
        if(v["filter"] not in ("aum", "expRatio", "trackErr")): continue
        val  = v.get("doubleVal") or v.get("strVal")
        if val is not None: d[v["filter"]] = val
    # print(d)
    if(len(d) == 4): processed_data.append(d)


df = pd.DataFrame(processed_data, columns=("name", "aum", "expRatio", "trackErr"))

df['final_number'] = df["expRatio"].rank(method="dense") * 0.80 + df["trackErr"].rank(method="dense") * 0.20

df["final_rank"] = df["final_number"].rank(method="dense")

df.sort_values(by="final_rank", inplace=True)
# df.to_clipboard()
print(df.head())