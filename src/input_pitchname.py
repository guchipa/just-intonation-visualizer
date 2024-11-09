import tkinter as tk
from tkinter import ttk

import dict
import main


# 演奏音リストに音を追加する
def addbutton_handler(pitch_list, pitch_name, is_root):
    pitch_list.append((pitch_name, is_root))
    # main.print_message(f"add: {(pitch_name, is_root)}", text_widget)
    # main.print_message(f"now: {pitch_list}", text_widget)
    print(f"add: {(pitch_name, is_root)}")
    print(f"now: {pitch_list}")


# 演奏音リストをクリアする
def clearbutton_handler(pitch_list):
    pitch_list.clear()
    print("clear", f"now: {pitch_list}")


def build(parent, pitch_list):
    # 演奏音を選択するコンボボックス（プルダウンメニュー）を作成
    pitchname = tk.StringVar()
    combo_pitchname = ttk.Combobox(
        parent, values=dict.pitchname_list, textvariable=pitchname, state="readonly"
    )
    combo_pitchname.pack(side=tk.LEFT)

    # コンボボックスで選択した音が根音であるかを決めるチェックボックスを作成
    is_root = tk.BooleanVar()
    is_root.set(False)
    check_isroot = tk.Checkbutton(parent, text="root", variable=is_root)
    check_isroot.pack(side=tk.LEFT)

    # 追加ボタンとクリアボタンを作成
    addbutton = tk.Button(parent, text="追加")
    addbutton.pack(side=tk.LEFT)
    addbutton.bind(
        "<Button-1>",
        lambda e: addbutton_handler(pitch_list, pitchname.get(), is_root.get()),
    )

    clearbutton = tk.Button(parent, text="クリア")
    clearbutton.pack(side=tk.LEFT)
    clearbutton.bind("<Button-1>", lambda _: clearbutton_handler(pitch_list))


# 演奏音入力部分の作成
def build_with_title(parent, pitch_list):
    frame_inputchord = ttk.Frame(parent)
    frame_inputchord.pack(side=tk.TOP)

    inputchord_title = tk.Label(frame_inputchord, text="演奏音入力")
    inputchord_title.pack(side=tk.LEFT, fill=tk.X)

    frame_inputpitchname = ttk.Frame(frame_inputchord)
    frame_inputpitchname.pack(side=tk.LEFT, fill=tk.X)

    build(frame_inputpitchname, pitch_list)
