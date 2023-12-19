import requests


def get_country_by_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            return data['country']
        else:
            return "Ошибка: Неверный IP или невозможно определить страну."
    except requests.exceptions.RequestException:
        return "Ошибка: Невозможно выполнить запрос к сервису."


if __name__ == "__main__":
    ip = input("Введите IP-адрес: ")
    country = get_country_by_ip(ip)
    print(f"Страна: {country}")

