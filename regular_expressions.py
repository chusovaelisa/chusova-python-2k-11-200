import re
import requests

youtube_regex = r'https://(www\.)?youtu\.be/|https://www\.youtube\.com/watch\?v='
link = input("Введите ссылку на YouTube видео: ")

if re.search(youtube_regex, link):
    print("Ссылка на YouTube видео корректна.")
else:
    print("Некорректная ссылка на YouTube видео.")