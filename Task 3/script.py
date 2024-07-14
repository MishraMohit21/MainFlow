import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def download_image(img_url, folder_name):
    try:
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        img_name = os.path.basename(img_url)
        img_path = os.path.join(folder_name, img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_response.content)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image {img_url}: {e}")


def create_folder(url):
    parsed_url = urlparse(url)
    folder_name = parsed_url.netloc.replace('.', '_')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


url = 'https://gruev.space/'


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    folder_name = create_folder(url)
    
    
    page_text = soup.get_text()
    with open(os.path.join(folder_name, 'page_text.txt'), 'w', encoding='utf-8') as file:
        file.write(page_text)
    
    
    links = soup.find_all('a')
    with open(os.path.join(folder_name, 'links.txt'), 'w', encoding='utf-8') as file:
        for link in links:
            href = link.get('href')
            link_text = link.get_text()
            file.write(f"Text: {link_text}, URL: {href}\n")
    
    
    images = soup.find_all('img')
    with open(os.path.join(folder_name, 'images.txt'), 'w', encoding='utf-8') as file:
        for img in images:
            src = img.get('src')
            alt = img.get('alt')
            img_url = urljoin(url, src)  # Create absolute URL for the image
            file.write(f"Alt: {alt}, Source: {img_url}\n")
            download_image(img_url, folder_name)
    
    print(f"Data extracted and saved in folder: {folder_name}")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
