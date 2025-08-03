# 📥 圖片下載器 (PNG to PDF)

這是一個用 Python 製作的簡易爬蟲工具，可以將網站中的圖片自動下載，並合併為一份 PDF 檔案。

## 🔧 功能說明

- 自動擷取貼文內的圖片連結
- 批次下載圖片至資料夾中
- 將圖片合併轉存為 PDF
- 支援處理截斷圖片（防止損壞）

## 📦 使用套件

- `requests`：發送網頁請求
- `beautifulsoup4`：解析 HTML
- `lxml`：HTML 解析器
- `Pillow`：圖片處理與 PDF 合併

## ▶️ 使用方式

1. 安裝所需套件（如尚未安裝）：

    ```bash
    pip install requests beautifulsoup4 lxml pillow
    ```

2. 將程式碼存為 `crawler.py`，並確保你有設定好儲存資料夾：

    ```python
    os.chdir("C:\\Users\\JOE\\Desktop\\crawler_png_to_pdf")
    ```

    如需更換下載位置，可修改此路徑。

3. 執行程式：

    ```bash
    python crawler.py
    ```

4. 輸入需要下載圖片網址

5. 程式會自動建立資料夾、下載圖片並產出 PDF 檔案！

## 📁 產出說明

- 圖片與 PDF 將會儲存在以貼文標題命名的資料夾中
- 例如：
  
```
小狗圖片集/
├── 0.png
├── 1.png
├── ...
└── 小狗圖片集.pdf
```
