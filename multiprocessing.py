import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import threading


def normalize_image_url(image_url, base_url):
    # Проверяем, есть ли протокол в URL
    if not image_url.startswith("http://") and not image_url.startswith("https://"):
        # Если нет, добавляем протокол и домен текущей страницы
        parsed_url = urlparse(base_url)
        image_url = urljoin(parsed_url.scheme + "://" + parsed_url.netloc, image_url)

    return image_url


def download_image(image_url, save_folder):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(image_url, headers=headers)
        response.raise_for_status()

        # Извлекаем имя файла из URL
        filename = os.path.join(save_folder, os.path.basename(urlparse(image_url).path))

        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"Изображение скачано: {image_url}")
    except Exception as e:
        print(f"Ошибка при скачивании изображения {image_url}: {e}")


def download_all_images(page_url, save_folder):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        image_tags = soup.find_all('img')

        threads = []
        for img in image_tags:
            image_url = normalize_image_url(img['src'], page_url)
            thread = threading.Thread(target=download_image, args=(image_url, save_folder))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"Ошибка при загрузке страницы {page_url}: {e}")


if __name__ == "__main__":
    page_url = input("Введите URL страницы: ")
    save_folder = input("Введите папку для сохранения изображений: ")

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    download_all_images(page_url, save_folder)
    print("Завершено.")
