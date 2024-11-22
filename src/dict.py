import json
import math

# Load constants
with open('constants.json', 'r') as f:
    constants = json.load(f)

just_ratios = constants["just_ratios"]
pitchname_list = constants["pitchname_list"]
freq_dict = constants["freq_dict"]


# 純正律の周波数を計算
def get_freqs(pitch_root_tuple):
    root_name = ""
    est_freqs = []

    # 根音を探す
    for pitch, is_root in pitch_root_tuple:
        if is_root:
            root_name = pitch
            break

    # 根音が設定されていない場合
    if root_name == "":
        print("ERROR: 根音が設定されていません")
        return []

    # 根音を基準に純正律の周波数を計算
    root_idx = pitchname_list.index(root_name)

    # pitchname_list.index(pitch) - root_idx で根音から何半音離れているか計算
    for pitch, _ in pitch_root_tuple:
        # 12半音周期で根音に純正律の比率をかける
        semitone_distance = pitchname_list.index(pitch) - root_idx

        # 12半音周期を超える場合は2の何乗かを計算
        if semitone_distance > 0:
            est_freqs.append(
                freq_dict[root_name]
                * just_ratios[semitone_distance % 12]
                * (2 ** (semitone_distance // 12))
            )
        else:
            est_freqs.append(
                freq_dict[root_name]
                * (just_ratios[semitone_distance % 12])
                * (2 ** math.ceil(semitone_distance // 12))
            )

    return est_freqs
