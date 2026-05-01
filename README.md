# Discord Bot Tutorial

2026 資芽大作業 template

## 環境設定

1. **安裝套件**
   ```bash
   pip install -r requirements.txt
   ```

2. **設定環境變數**
   ```bash
   cp .env.example .env
   # 在 .env 中填入 TOKEN 與 GEMINI_API_KEY
   ```

3. **啟動 Bot**
   ```bash
   python bot.py
   ```

## 專案結構

```
├── bot.py          # Bot 設定
├── core.py         # Cog
├── cmds/
│   ├── chat.py     # Gemini AI 相關指令
│   ├── task.py     # 待辦事項相關指令
│   ├── feature1.py # 自訂功能 1
│   └── feature2.py # 自訂功能 2
└── .env.example    # 環境變數範本
```

## 參考資料

- [教學 HackMD](https://hackmd.io/@gary940610/sprout-hw)
