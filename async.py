import asyncio
import os

import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


async def download_image(session, image_url, save_folder):
    try:
        async with session.get(image_url) as response:
            response.raise_for_status()
            image_data = await response.read()
            filename = os.path.join(save_folder, os.path.basename(urlparse(image_url).path))
            with open(filename, 'wb') as file:
                file.write(image_data)
            print(f"Изображение скачано: {image_url}")
    except Exception as e:
        print(f"Ошибка при счачивании изображения {image_url}: {e}")


async def download_all_images(page_url, save_folder):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(page_url) as response:
                response.raise_for_status()
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                image_tags = soup.find_all('img')
                base_url = urlparse(page_url).scheme + "://" + urlparse(page_url).netloc
                image_urls = [urljoin(base_url, img['src']) for img in image_tags if 'src' in img.attrs]
                tasks = [download_image(session, url, save_folder) for url in image_urls]
                await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Ошибка при загрузке страницы {page_url}: {e}")


async def main():
    page_url = input("Введите URL страницы: ")
    save_folder = input("Введите папку для сохранения изображений: ")

    if not await aio_exists(save_folder):
        os.makedirs(save_folder)

    await download_all_images(page_url, save_folder)
    print("Завершено.")


async def aio_exists(path):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, os.path.exists, path)
if __name__ == "__main__":
    asyncio.run(main())
