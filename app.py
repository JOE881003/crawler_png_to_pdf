import streamlit as st
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageFile
import os
import io
import zipfile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def fetch_image_links(url: str) -> tuple[str, list]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    results_style = soup.find_all("img", attrs = {'style':'cursor:pointer'})
    results_class = soup.find_all("img", {"class": "zoom"})
    results = results_style + results_class

    image_links = [result.get("file") for result in results if result.get("file")]
    name = soup.find(class_="title-cont").get_text().split('\n')[2].strip()
    return name, image_links

def create_pdf_from_images(name: str, image_links: list) -> bytes:
    images = []
    for link in image_links:
        response = requests.get(link)
        img = Image.open(io.BytesIO(response.content))
        if img.mode == "RGBA":
            img = img.convert("RGB")
        images.append(img)

    buffer = io.BytesIO()
    images[0].save(buffer, format="PDF", save_all=True, append_images=images[1:])
    buffer.seek(0)
    return buffer.read()

st.title("📄 圖片轉 PDF 下載器")
url = st.text_input("請輸入圖片網站連結：")

if st.button("開始下載") and url:
    try:
        with st.spinner("抓取中，請稍候..."):
            name, image_links = fetch_image_links(url)
            pdf_bytes = create_pdf_from_images(name, image_links)

        st.success(f"✅ {name}.pdf 建立完成！")
        st.download_button(
            label="📥 下載 PDF",
            data=pdf_bytes,
            file_name=f"{name}.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"❌ 發生錯誤：{e}")
