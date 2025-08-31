import requests
from bs4 import BeautifulSoup
import os

url = "https://1upcloud.tech/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Save HTML
with open("src/index.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# Download all images
img_tags = soup.find_all("img")
os.makedirs("src/images", exist_ok=True)
for img in img_tags:
    src = img.get("src")
    if src and src.startswith("/images/"):
        img_url = url + src.lstrip("/")
        img_name = src.split("/")[-1]
        img_data = requests.get(img_url).content
        with open(f"src/images/{img_name}", "wb") as img_file:
            img_file.write(img_data)

# Download CSS
for link in soup.find_all("link", rel="stylesheet"):
    href = link.get("href")
    if href and href.startswith("/css/"):
        css_url = url + href.lstrip("/")
        css_name = href.split("/")[-1]
        css_data = requests.get(css_url).content
        with open(f"src/css/{css_name}", "wb") as css_file:
            css_file.write(css_data)

# Download JS
for script in soup.find_all("script"):
    src = script.get("src")
    if src and src.startswith("/js/"):
        js_url = url + src.lstrip("/")
        js_name = src.split("/")[-1]
        js_data = requests.get(js_url).content
        with open(f"src/js/{js_name}", "wb") as js_file:
            js_file.write(js_data)

print("Site downloaded.")
