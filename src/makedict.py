import json
import yaml

# Load constants and settings
with open('../config/constants.json', 'r') as f:
    constants = json.load(f)

with open('../config/settings.yaml', 'r') as f:
    settings = yaml.safe_load(f)

name_dict = constants["name_dict"]
A4_FREQ = settings["A4_FREQ"]

with open("../config/constants.json", "w") as f:
    for i in range(1, 7):
        for j in range(1, 13):
            base = A4_FREQ * (2 ** (i - 4))
            f.write(f'"{name_dict[str(j)]}{i}": {base * (2 ** ((j - 10) / 12))},\n')
    
    
    
