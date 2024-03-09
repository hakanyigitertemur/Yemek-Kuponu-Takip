import requests
from bs4 import BeautifulSoup
import time
import random



son_kayitlar = []


def kayit_control(a):
    if a not in son_kayitlar:
        son_kayitlar.append(a)
        return True
    else:
        return False


while True:
    url = "https://www.technopat.net/sosyal/bolum/indirim-koesesi.257/?prefix_id=30"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0',
               "Referer": "https://www.google.com/"}

    response = requests.get(url, headers=headers)

    yemek_adlari = ["getir", "Carrefoursa", "Yemeksepeti", "yemek", "Trendyol", "yemek", "Pizza", "yemek sepeti",
                    "Migros", "amazon", "dominos", "domino's","getiryemek"]

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        a_all = soup.find_all("a")
        for i in a_all:
            a_str = i.text
            spliter = a_str.split()
            for yemeks in yemek_adlari:
                for split in spliter:
                    if yemeks.lower() == split.lower():
                        if kayit_control(i.text):
                            print(f"{i.text}: https://www.technopat.net{i['href']}")
    else:
        print(response.status_code, response.reason)
    time.sleep(random.randint(2, 5))
