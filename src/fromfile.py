import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import just_analyze
import input_pitchname


def open_file(file_path_entry, update_message_window):
    # ファイルダイアログを開いてファイルパスを取得
    file_path = filedialog.askopenfilename()
    if file_path:
        update_message_window(f"ファイルが選択されました: {file_path}")
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)


def read_file(file_path_entry, pitch_list, update_message_window):
    # テキストボックスからファイルパスを取得してファイルを読み込む
    file_path = file_path_entry.get()
    if file_path != "":
        # ファイルに対する処理
        try:
            just_analyze.analyze(file_path, pitch_list)
            update_message_window(f"ファイル '{file_path}' の解析が完了しました。")
        except Exception as e:
            update_message_window(f"エラーが発生しました: {e}")
    else:
        update_message_window("ファイルが選択されていません。")


def build(parent, pitch_list, update_message_window):
    # ファイル入力部分
    frame_inputfile = ttk.Frame(parent)
    frame_inputfile.pack(side=tk.TOP, fill=tk.X)

    # ファイルパスを入力できるテキストボックスを配置
    file_path_entry = ttk.Entry(frame_inputfile, width=50)
    file_path_entry.pack(side=tk.LEFT, padx=(10, 10))

    # 「開く」ボタンを配置
    open_button = ttk.Button(
        frame_inputfile,
        text="参照",
        command=lambda: open_file(file_path_entry, update_message_window),
    )
    open_button.pack(side=tk.LEFT, padx=(0, 10))

    # 「読み込み」ボタンを配置
    read_button = ttk.Button(
        frame_inputfile,
        text="読み込み",
        command=lambda: read_file(file_path_entry, pitch_list, update_message_window),
    )
    read_button.pack(side=tk.LEFT, padx=(0, 10))

    # 演奏音入力部分
    frame_inputchord = ttk.Frame(parent)
    frame_inputchord.pack(side=tk.TOP)

    inputchord_title = tk.Label(frame_inputchord, text="演奏音入力")
    inputchord_title.pack(side=tk.LEFT, fill=tk.X)

    # 音名入力部分
    frame_inputpitchname = ttk.Frame(frame_inputchord)
    frame_inputpitchname.pack(side=tk.LEFT, fill=tk.X)

    input_pitchname.build(frame_inputpitchname, pitch_list)
