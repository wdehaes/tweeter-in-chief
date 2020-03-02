import json
import re

with open('raw_data.json', 'r') as f:
    tweets = json.load(f)

with open('raw_data_10.json', 'w', encoding='utf-8') as f:
    json.dump(tweets[:10],
                        f, ensure_ascii=False, indent=4)

                    