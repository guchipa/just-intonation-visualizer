import tkinter as tk
from tkinter import ttk

import fromfile
import configuration
import fromsound

# 演奏音を格納するリスト
pitch_list = []


def main():
    try: 
        # メッセージウィンドウの更新関数
        def update_message_window(message):
            message_window.configure(state="normal")  # 編集可能にする
            message_window.insert(tk.END, message + "\n")  # メッセージを追加
            message_window.configure(state="disabled")  # 編集不可に戻す

        # メインウィンドウの作成
        root = tk.Tk()
        title_text = "純正律 判定"
        root.title(title_text)
        iconfile = "./myfavicon.ico"
        root.iconbitmap(default=iconfile)
        root.geometry("500x500")

        # notebook ウィジェットを作成
        # 複数タブの切り替えを実現（ファイル読み込みモード, 聞き取りモード）
        notebook = ttk.Notebook(root)

        # タブの作成
        tab_fromfile = tk.Frame(notebook)
        tab_fromsound = tk.Frame(notebook)
        tab_configuration = tk.Frame(notebook)

        # notebook へタブを追加
        notebook.add(tab_fromfile, text="ファイル読み込み")
        notebook.add(tab_fromsound, text="音声入力")
        notebook.add(tab_configuration, text="設定")
        notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # ファイル読み込みモードの作成
        fromfile.build(tab_fromfile, pitch_list, update_message_window)

        # 音声入力モードの作成
        fromsound.build(tab_fromsound, pitch_list)

        # 設定タブの作成
        configuration.build(tab_configuration)

        # メッセージラベルのフレームを作成
        frame_message_label = tk.Frame(root)
        frame_message_label.pack(anchor="w", padx=10)  # 左寄せ

        message_label = tk.Label(frame_message_label, text="メッセージ")
        message_label.pack(anchor="w")  # 左寄せ

        # メッセージウィンドウのフレームを作成し、中央に配置
        frame_message_text = tk.Frame(root)
        frame_message_text.pack(fill=tk.X, padx=10, pady=10)

        # メッセージウィンドウを作成
        message_window = tk.Text(frame_message_text)
        message_window.pack(anchor="w")
        message_window.configure(state="disabled")

        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
