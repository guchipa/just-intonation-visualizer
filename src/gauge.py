import tkinter as tk
import math


def create_canvas_gauge(root):
    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=20)

    # 円弧を描画
    canvas.create_arc(
        20, 20, 280, 280, start=30, extent=120, style=tk.ARC, width=3, outline="blue"
    )

    # 初期の針の位置
    needle = canvas.create_line(150, 150, 150, 50, width=4, fill="red")

    def update_needle(position):
        # 針の角度を計算 (-1 から 1 の範囲)
        angle = 30 + (120 * (position + 1) / 2)
        radians = math.radians(angle)
        x = 150 + 100 * math.cos(radians)
        y = 150 - 100 * math.sin(radians)
        canvas.coords(needle, 150, 150, x, y)

    return update_needle


root = tk.Tk()
root.title("音程評価メーター")
root.geometry("400x400")

# メーターを作成し、針を操作する関数を取得
update_canvas_gauge = create_canvas_gauge(root)

# ボタンで針を更新する例
frame = tk.Frame(root)
frame.pack(pady=20)

# フラット方向に針を動かすボタン
btn_flat = tk.Button(frame, text="フラット", command=lambda: update_canvas_gauge(-0.5))
btn_flat.pack(side=tk.LEFT, padx=10)

# シャープ方向に針を動かすボタン
btn_sharp = tk.Button(frame, text="シャープ", command=lambda: update_canvas_gauge(0.5))
btn_sharp.pack(side=tk.LEFT, padx=10)

# 針を中央に戻すボタン
btn_reset = tk.Button(frame, text="リセット", command=lambda: update_canvas_gauge(0))
btn_reset.pack(side=tk.LEFT, padx=10)

root.mainloop()
