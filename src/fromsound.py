import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import numpy as np
import math

import input_pitchname
import just_analyze

# グローバル変数の定義
gauge_windows = []
update_gauges = []
stream = None
_pitch_list = []


# メーターウィンドウを作成する
def create_meter_window(pitch_name):
    # 新しいウィンドウ（Toplevel）を作成
    meter_window = tk.Toplevel()
    meter_window.title(f"メーターウィンドウ - {pitch_name}")
    meter_window.geometry("400x300")

    # メーターを作成
    canvas = tk.Canvas(meter_window, width=300, height=200, bg="white")
    canvas.pack(pady=20)

    # 円弧を描画
    canvas.create_arc(
        20, 20, 280, 280, start=30, extent=120, style=tk.ARC, width=3, outline="blue"
    )

    # 初期の針の位置を描画
    needle = canvas.create_line(150, 150, 150, 50, width=4, fill="red")

    # 針の位置を更新する関数を返す
    def update_needle(position):
        # 針の角度を計算 (-1 から 1 の範囲で指定)
        angle = 30 + (120 * (position + 1) / 2)
        radians = math.radians(angle)
        x = 150 + 100 * math.cos(radians)
        y = 150 - 100 * math.sin(radians)
        canvas.coords(needle, 150, 150, x, y)

    return update_needle


# 音声入力ストリームの起動
def start_audio_stream():
    # サンプリングレートとバッファサイズを設定
    SAMPLE_RATE = 22050
    STREAM_BUFFER_SIZE = 65536

    global stream
    stream = None

    print(f"Audio stream started")

    # 音声入力のコールバック関数
    def audio_callback(indata, frames, time, status):
        # エラーが発生した場合はエラーメッセージを表示
        if status:
            print(f"Error: {status}", flush=True)
        samples = np.squeeze(indata)

        # 音声入力を解析
        try:
            evallist = just_analyze.analyze(samples, SAMPLE_RATE, _pitch_list)

            # 各メーターを更新
            for i, deviation in enumerate(evallist):
                if i < len(update_gauges):
                    update_gauges[i](deviation)

        except Exception as e:
            print(f"Error analyzing pitch: {e}")

    # 音声入力ストリームの作成
    stream = sd.InputStream(
        callback=audio_callback,
        channels=1,
        samplerate=SAMPLE_RATE,
        blocksize=STREAM_BUFFER_SIZE,
    )
    stream.start()


# 音声入力ストリームの停止
def stop_audio_stream():
    global stream
    if stream is not None:
        stream.stop()
        stream.close()
        print("Audio stream stopped.")


# リアルタイム入力タブのビルド
def build(parent, pitch_list):
    global _pitch_list
    _pitch_list = pitch_list

    # メーターウィンドウを作成するボタン
    meter_button = ttk.Button(
        parent, text="メーターを表示", command=lambda: start_meter(pitch_list)
    )
    meter_button.pack(pady=10)

    # リアルタイム音声解析を開始するボタン
    start_button = ttk.Button(
        parent,
        text="リアルタイム解析開始",
        command=start_audio_stream,
    )
    start_button.pack(pady=10)

    # リアルタイム音声解析を停止するボタン
    stop_button = ttk.Button(parent, text="解析停止", command=stop_audio_stream)
    stop_button.pack(pady=10)

    # 演奏音入力部分の作成
    input_pitchname.build_with_title(parent, pitch_list)


# メーターを起動
def start_meter(pitch_list):
    global gauge_windows, update_gauges
    gauge_windows.clear()
    update_gauges.clear()

    # ピッチリストの数だけメーターウィンドウを作成
    for pitch_name in pitch_list:
        update_gauge = create_meter_window(pitch_name)
        update_gauges.append(update_gauge)
