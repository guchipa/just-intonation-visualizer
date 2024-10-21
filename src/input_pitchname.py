import tkinter as tk
from tkinter import ttk

import dict
import main


def addbutton_handler(pitch_list, pitch_name, is_root):
    pitch_list.append((pitch_name, is_root))
    # main.print_message(f"add: {(pitch_name, is_root)}", text_widget)
    # main.print_message(f"now: {pitch_list}", text_widget)
    print(f"add: {(pitch_name, is_root)}")
    print(f"now: {pitch_list}")


def clearbutton_handler(pitch_list):
    pitch_list.clear()
    print("clear", f"now: {pitch_list}")


def build(parent, pitch_list):
    pitchname = tk.StringVar()
    combo_pitchname = ttk.Combobox(
        parent, values=dict.pitchname_list, textvariable=pitchname, state="readonly"
    )
    combo_pitchname.pack(side=tk.LEFT)

    is_root = tk.BooleanVar()
    is_root.set(False)
    check_isroot = tk.Checkbutton(parent, text="root", variable=is_root)
    check_isroot.pack(side=tk.LEFT)

    addbutton = tk.Button(parent, text="追加")
    addbutton.pack(side=tk.LEFT)
    addbutton.bind(
        "<Button-1>",
        lambda e: addbutton_handler(pitch_list, pitchname.get(), is_root.get()),
    )

    clearbutton = tk.Button(parent, text="クリア")
    clearbutton.pack(side=tk.LEFT)
    clearbutton.bind("<Button-1>", lambda _: clearbutton_handler(pitch_list))

    return
