import librosa
import matplotlib.pyplot as plt
import numpy as np


import dict


def eval(spec, freq, t, pitch_name_list, EVAL_RANGE=5):
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

    if est_freqs == "":
        return

    # 各演奏ピッチに対して評価
    # eval_list: 演奏音が評価範囲のどこに位置するかを格納
    # center_freq_list: 評価範囲の中心のindex を格納
    eval_list = []
    center_index_list = []
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
        # 中心から ± EVAL_RANGE の範囲を評価
        eval_range_min = target_idx - EVAL_RANGE
        eval_range_max = target_idx + EVAL_RANGE + 1
        center = (eval_range_max - eval_range_min) / 2
        around_spec = spec[eval_range_min:eval_range_max]

        # np.argmax で最も強いスペクトルをもつもののindex を取得
        # (-1, 1) に丸めてリストに追加
        eval_list.append((np.argmax(around_spec) - center) / EVAL_RANGE)

        # if np.argmax(around_spec) == EVAL_RANGE:
        #     print(f"{pitch_name_list[count]}: ok")
        # if np.argmax(around_spec) > EVAL_RANGE:
        #     print(f"{pitch_name_list[count]}: high")
        # if np.argmax(around_spec) < EVAL_RANGE:
        #     print(f"{pitch_name_list[count]}: low")

        count += 1

    return eval_list


# ファイル入力での解析
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


# データを受け取って解析
def analyze(y, sr, pitch_list, show=False):
    spec, freq, t, im = plt.specgram(y, Fs=sr, NFFT=65536)

    return eval(spec=spec, freq=freq, t=t, pitch_name_list=pitch_list)

    if show == True:
        plt.show()
        print(f"spec = {spec}\nfreq = {freq}\nt = {t}\nim = {im}")
