name_dict = {
    1: "C",
    2: "C#",
    3: "D",
    4: "D#",
    5: "E",
    6: "F",
    7: "F#",
    8: "G",
    9: "G#",
    10: "A",
    11: "A#",
    12: "B",
}

f = open("./name_list.txt", "w")

for i in range(1, 7):
    for j in range(1, 13):
        f.write(f'"{name_dict[j]}{i}",\n')

f.close()
