import json

import sol_path

with open(sol_path.resolve("config/constants.json"), "r") as f:
    constants = json.load(f)

name_dict = constants["name_dict"]

name_list = []

for i in range(1, 7):
    for j in range(1, 13):
        name_list.append(f"{name_dict[str(j)]}{i}")

constants["name_list"] = name_list

with open(sol_path.resolve("config/constants.json"), "w") as f:
    json.dump(constants, f, indent=4)
