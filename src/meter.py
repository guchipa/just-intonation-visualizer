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
        20, 60, 280, 320, start=30, extent=120, style=tk.ARC, width=3, outline="blue"
    )

    # メーターの示す数値を描画
    canvas.create_text(150, 180, text="0", font=("Helvetica", 12))
    canvas.create_text(50, 180, text="-50cents", font=("Helvetica", 12))
    canvas.create_text(250, 180, text="50cents", font=("Helvetica", 12))

    # 目盛りを追加
    for i in range(-10, 11):
        angle = 30 + (120 * (i + 10) / 20)
        radians = math.radians(angle)
        x_start = 150 + 130 * math.cos(radians)
        y_start = 190 - 130 * math.sin(radians)

        # 中心と端点の座標を計算
        if i in [-10, 0, 10]:
            x_end = 150 + 115 * math.cos(radians)
            y_end = 190 - 115 * math.sin(radians)
        else:
            x_end = 150 + 120 * math.cos(radians)
            y_end = 190 - 120 * math.sin(radians)
        canvas.create_line(x_start, y_start, x_end, y_end, width=2)

    # 初期の針の位置を描画
    needle = canvas.create_line(150, 170, 150, 70, width=4, fill="red")

    # 針の角度を計算 (-1 から 1 の範囲で指定)
    def update_needle(position):
        # 更新しない場合
        if position is None:
            return

        angle = 30 + (120 * (position + 1) / 2)
        radians = math.radians(angle)
        x = 150 + 120 * math.cos(radians)
        y = 190 - 120 * math.sin(radians)
        canvas.coords(needle, 150, 170, x, y)

    # 針の位置を更新する関数を返す
    return update_needle
