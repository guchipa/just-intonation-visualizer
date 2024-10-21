import librosa
import matplotlib.pyplot as plt
import numpy as np


import dict


def eval(spec, freq, t, pitch_name_list, THRESFOLD=5):
    # STFT に対する評価
    # spec: 各周波数に対するスペクトル（強さ）
    # freq: 周波数ビン（sr = 22050, NFFT = 65536 で 0.336Hz 刻み  sr / NFFT で計算できる）
    # pitch_name_list: 演奏される音の音名と根音の情報 (pitch, is_root) のタプル

    # -前処理
    # -複数セグメントある場合に足し合わせる
    if len(t) > 1:
        spec = np.sum(spec, axis=1)

    # dict より音名から freq を取得
    est_freqs = dict.get_freqs(pitch_name_list)
    # est_freqs = []
    # for p, is_root in pitch_root_list:
    #     est_freqs.append(dict.freq_dict[p])

    # est_freqs = [440.0, 440 * (5 / 4), 440 * (3 / 2)]

    # 各演奏ピッチに対して評価
    evallist = []
    count = 0
    for est_f in est_freqs:
        target_freq = 1e10
        target_idx = -1

        # 周波数ビンの中から最も近いものを探索
        for f in freq:
            if abs(est_f - f) < abs(est_f - target_freq):
                target_freq = f
                target_idx += 1
            else:
                break

        # 近傍の周波数スペクトルを評価
        tmp = spec[target_idx - THRESFOLD : target_idx + THRESFOLD + 1]
        print(tmp)
        print(np.argmax(tmp))
        if np.argmax(tmp) == THRESFOLD:
            evallist.append(f"{pitch_name_list[count]}: ok")
        if np.argmax(tmp) > THRESFOLD:
            evallist.append(f"{pitch_name_list[count]}: high")
        if np.argmax(tmp) < THRESFOLD:
            evallist.append(f"{pitch_name_list[count]}: low")

        count += 1

    return evallist


def analyze(file_path, pitch_list, show=False):
    print("file loading...")
    y, sr = librosa.load(file_path, sr=22050)
    print("ok")
    print(f"sampling rate: {sr}")
    print("analyzing...")
    spec, freq, t, im = plt.specgram(y, Fs=sr, NFFT=65536)
    print(freq)

    print(eval(spec=spec, freq=freq, t=t, pitch_name_list=pitch_list))

    if show == True:
        plt.show()
        print(f"spec = {spec}\nfreq = {freq}\nt = {t}\nim = {im}")
