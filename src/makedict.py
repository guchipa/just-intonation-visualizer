import json

with open("../config/constants.json", "r") as f:
    constants = json.load(f)

name_dict = constants["name_dict"]
A4_FREQ = constants["A4_FREQ"]

f = open("./dict.txt", "w")

for i in range(1, 7):
    for j in range(1, 13):
        base = A4_FREQ * (2 ** (i - 4))
        f.write(f'"{name_dict[str(j)]}{i}": {base * (2 ** ((j - 10) / 12))},\n')

f.close()
