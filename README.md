# 実行
1. https://github.com/MoriguchiHinata/just-intonation-visualizer/releases より最新版のzipファイルをダウンロード
2. zipファイルを解凍
3. 回答先の`JustInTone.exe`をダブルクリック

# 環境構築

- 仮想環境の作成
Python3.9.* をインストールしたうえで以下を実行
```
py -3.9 -m venv [envname]
```

- 仮想環境を有効化

```
.\[envname]\Scripts\activate
```

- パッケージのインストール
  **仮想環境を有効化した状態で**以下を実行

```
pip install -r requirements.txt
```

- 仮想環境を終了

```
deactivate
```

# 実行ファイル（.exe）の作成
```
pyinstaller --icon=sample.ico test.py
```

---

# トラブルシューティング
#### `main.py` を実行してもウィンドウが表示されない
カレントディレクトリが`main.py`を含む場所にあるかを確認する．<br>
`python .\path\to\main\main.py`のような実行は現状できない．
