from multiprocessing import Pool
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup


def download_image(image_url, save_folder):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(image_url, headers=headers)
        response.raise_for_status()

        filename = os.path.join(save_folder, os.path.basename(urlparse(image_url).path))

        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"Изображение скачано: {image_url}")
    except Exception as e:
        print(f"Ошибка при скачивании изображения {image_url}: {e}")


def download_all_images(page_url, save_folder):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        image_tags = soup.find_all('img')

        base_url = urlparse(page_url).scheme + "://" + urlparse(page_url).netloc
        image_urls = [urljoin(base_url, img['src']) for img in image_tags]
        save_folders = [save_folder] * len(image_urls)

        with Pool(processes=4) as pool:
            pool.starmap(download_image, zip(image_urls, save_folders))

    except Exception as e:
        print(f"Ошибка при загрузке страницы {page_url}: {e}")


if __name__ == "__main__":
    page_url = input("Введите URL страницы: ")
    save_folder = input("Введите папку для сохранения изображений: ")

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    download_all_images(page_url, save_folder)
    print("Завершено.")
