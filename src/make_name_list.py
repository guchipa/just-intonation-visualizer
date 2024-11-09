name_dict = {
    1: "C",
    2: "C#(D♭)",
    3: "D",
    4: "D#(E♭)",
    5: "E",
    6: "F",
    7: "F#(G♭)",
    8: "G",
    9: "G#(A♭)",
    10: "A",
    11: "A#(B♭)",
    12: "B",
}

f = open("./name_list.txt", "w")

for i in range(1, 7):
    for j in range(1, 13):
        f.write(f'"{name_dict[j]}{i}",\n')

f.close()
