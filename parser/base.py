import requests
from bs4 import BeautifulSoup as BS



def parse_cars():
    """
        Функция парсит сайт "cars.kg"
    """
    url = "https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c08b0"
    response = requests.get(url, timeout=15)
    print(response)
    print(response.status_code == 200)
    # print(response.text[:200])
    cars = []
    soup = BS(response.text, "html.parser")
    table = soup.find("div", class_="main catalog")
    obyavlenia = table.find_all("a", class_="catalog-list-item")
    for data in obyavlenia:
        car = {}
        car['title'] = data.find("span", class_="catalog-item-caption").text.strip()
        car['price'] = data.find("span",class_= "catalog-item-price").text.strip()
        car['photo'] = data.find("img",class_= "catalog-item-cover-img").get("src")
        cars.append(car)
    return cars


