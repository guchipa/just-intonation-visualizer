import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import librosa
import numpy as np
import math

import input_pitchname


def create_meter_window():
    # 新しいウィンドウ（Toplevel）を作成
    meter_window = tk.Toplevel()
    meter_window.title("メーターウィンドウ")
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

    def update_needle(position):
        # 針の角度を計算 (-1 から 1 の範囲で指定)
        angle = 30 + (120 * (position + 1) / 2)
        radians = math.radians(angle)
        x = 150 + 100 * math.cos(radians)
        y = 150 - 100 * math.sin(radians)
        canvas.coords(needle, 150, 150, x, y)

    return update_needle


def start_audio_stream(update_gauge):
    # サンプリングレートとバッファサイズを設定
    sample_rate = 22050
    buffer_size = 1024

    global stream
    stream = None

    print(f"Audio stream started")

    def audio_callback(indata, frames, time, status):
        if status:
            print(f"Error: {status}", flush=True)
        samples = np.squeeze(indata)

        try:
            pitches, magnitudes = librosa.core.piptrack(y=samples, sr=sample_rate)
            pitch = 0
            if magnitudes.any():
                index = magnitudes.argmax()
                pitch = pitches[
                    index // magnitudes.shape[1], index % magnitudes.shape[1]
                ]

            if pitch > 0:
                reference_pitch = 440.0
                deviation = (pitch - reference_pitch) / reference_pitch
                deviation = max(-1, min(1, deviation))

                # メーターを更新
                update_gauge(deviation)

        except Exception as e:
            print(f"Error analyzing pitch: {e}")

    stream = sd.InputStream(
        callback=audio_callback,
        channels=1,
        samplerate=sample_rate,
        blocksize=buffer_size,
    )
    stream.start()


def stop_audio_stream():
    global stream
    if stream is not None:
        stream.stop()
        stream.close()
        print("Audio stream stopped.")


def build(parent, pitch_list):
    frame_inputsound = ttk.Frame(parent)
    frame_inputsound.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    frame_inputchord = ttk.Frame(parent)
    frame_inputchord.pack(side=tk.TOP)

    inputchord_title = tk.Label(frame_inputchord, text="演奏音入力")
    inputchord_title.pack(side=tk.LEFT, fill=tk.X)

    frame_inputpitchname = ttk.Frame(frame_inputchord)
    frame_inputpitchname.pack(side=tk.LEFT, fill=tk.X)

    input_pitchname.build(frame_inputpitchname, pitch_list)

    # メーターウィンドウを作成するボタン
    meter_button = ttk.Button(
        frame_inputsound, text="メーターを表示", command=lambda: start_meter()
    )
    meter_button.pack(pady=10)

    # ボタンを作成してリアルタイム音声解析を開始
    start_button = ttk.Button(
        frame_inputsound,
        text="リアルタイム解析開始",
        command=lambda: start_audio_stream(update_gauge),
    )
    start_button.pack(pady=10)

    stop_button = ttk.Button(
        frame_inputsound, text="解析停止", command=stop_audio_stream
    )
    stop_button.pack(pady=10)


def start_meter():
    global update_gauge
    update_gauge = create_meter_window()
