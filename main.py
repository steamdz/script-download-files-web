import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_website(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Create a folder named 'website_download' inside your project directory
            project_dir = os.path.dirname(os.path.abspath(__file__))
            download_dir = os.path.join(project_dir, 'website_download')
            os.makedirs(download_dir, exist_ok=True)

            with open(os.path.join(download_dir, 'index.html'), 'w', encoding='utf-8') as file:
                file.write(response.text)

            for script in soup.find_all('script', src=True):
                download_file(urljoin(url, script['src']), download_dir)

            for link in soup.find_all('link', rel='stylesheet'):
                download_file(urljoin(url, link['href']), download_dir)

            print("Website downloaded successfully!")
        else:
            print(f'Failed {response.status_code}')
    except Exception as e:
        print(f'Error : {str(e)}')

def download_file(url, folder):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            filename = os.path.join(folder, os.path.basename(urlparse(url).path))

            with open(filename, 'wb') as file:
                file.write(response.content)
        else:
            print(f'Failed to download: {response.status_code}')

    except Exception as e:
        print(f'Error: {str(e)}')

website_url = "https://www.example.com/"
download_website(website_url)
