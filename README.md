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
