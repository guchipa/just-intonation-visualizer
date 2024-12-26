import json

def make_freq_list():
    with open("../config/constants.json", "r") as f:
        constants = json.load(f)
        A4_FREQ = constants["a4_freq"]

    freq_list = []
    for i in range(1, 7):
        for j in range(1, 13):
            base = A4_FREQ * (2 ** (i - 4))
            freq = base * (2 ** ((j - 10) / 12))
            freq_list.append(freq)

    # Write frequency list to constants.json
    with open("../config/constants.json", "r") as json_file:
        data = json.load(json_file)

    data["freq_list"] = freq_list

    with open("../config/constants.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
