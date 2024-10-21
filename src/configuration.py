import tkinter as tk
from tkinter import ttk


# 設定タブの実装
def build(parent):

    # ログファイルを残すか
    frame_log_toggle = ttk.Frame(parent)
    frame_log_toggle.pack(side=tk.TOP, padx=30, pady=10)

    label_log = tk.Label(frame_log_toggle, text="ログを保存")
    label_log.pack(side=tk.LEFT, fill=tk.X)

    take_log = tk.BooleanVar()
    take_log.set(False)

    checkbox_log = tk.Checkbutton(frame_log_toggle, text="", variable=take_log)
    checkbox_log.pack(side=tk.RIGHT, fill=tk.X)

    # A4 の周波数定義
