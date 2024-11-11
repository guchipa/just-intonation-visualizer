import tkinter as tk
import math


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
