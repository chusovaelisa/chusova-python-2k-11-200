import requests
from bs4 import BeautifulSoup

url = "https://meteoinfo.ru/forecasts/russia/republic-tatarstan/kasan"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    temperature_elements = soup.find_all(class_="fc_temp_short")
    today_weather = temperature_elements[0].get_text()  

    print(f"Погода на сегодня: {today_weather}")

    for element in temperature_elements[1:]:  
        print(element.get_text())
else:
    print("Не удалось получить доступ к странице")
