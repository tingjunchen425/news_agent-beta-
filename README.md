# news_agent-beta
## 測試版自動新聞統整
### 簡述
- 自動新聞收集
- 由gemini-2.0-flash進行統整撰寫

### 系統需求(建議)
1. python 3.11
2. gemini api key
3. tavily api key

### 安裝步驟
1. 克隆專案
```bash
git clone https://github.com/tingjunchen425/news_agent-beta-.git
```
2. 安裝相依套件
```bash
pip install -r requirements.txt
``` 
3. 設定環境變數：
    1. 複製.env.example為.env
        ```bash
        copy .env.example .env
        ```
    2. 填入以下資訊：
        - gemini api key
        - tavily api key

### 版本紀錄
- v2.0.0
    - 新增web_ui功能
    - 調整搜尋輪次

### api key取得
1. gemini
    - 至[google ai studio](https://aistudio.google.com/apikey)申請
2. tavily
    - 至[tavily](https://app.tavily.com/home)申請