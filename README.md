# poetry のサンプル開発環境

## 詳細

```
.
├── app                 # アプリケーション
│   ├── app1.py
│   ├── app2            # 親であるapp1.pyを呼び出せる
│   ├── definition      # 型定義ファイル
│   └── services        # ビジネスロジック
└── tests               # テスト
    ├── fixture         # fixtureを用いたテストコード
    └── simple          # テストコード
```
