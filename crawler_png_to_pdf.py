from bs4 import BeautifulSoup
import requests
import os
from PIL import Image, ImageFile

os.chdir("C:\\Users\\JOE\\Desktop\\crawler_png_to_pdf")


def download_to_pdf():
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }

    URL = input('請輸入欲下載網址: ')


    response = session.get(URL, headers = headers)

    soup = BeautifulSoup(response.text, "lxml")



    # 由此網址取得圖片連結
    
    results_style = soup.find_all("img", attrs = {'style':'cursor:pointer'})
    results_class = soup.find_all("img", {"class": "zoom"})
    results = results_style + results_class
    
    image_links = [result.get("file") for result in results if result.get("file") is not None]


    name = soup.find(class_ = "title-cont").get_text().split('\n')[2].strip()


    for index, link in enumerate(image_links):
     
        if not os.path.exists(name):
            os.mkdir(name)  # 建立資料夾

        img = requests.get(link)  # 下載圖片

        with open(name+"\\" + str(index) + ".png", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼
            


    file_path = [name + "\\"+ str(i) +".png" for i in range(0, len(image_links))]

    output = Image.open(file_path[0])
    file_path.pop(0)

    source = []
    for i in file_path:
        img = Image.open(i)
        if img.mode == "RGBA":
            img = img.convert("RGB")
        source.append(img)

    output.save(name + "\\" + name + ".pdf", 'pdf', save_all = True, append_images = source)
    print(name+" 下載完成")


download_to_pdf()