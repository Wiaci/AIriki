from bs4 import BeautifulSoup
import requests
import re

base = []
path = "https://losyash-library.fandom.com/ru/wiki/Скамейка"

for i in range(50):
    r = requests.get(path)
    soup = BeautifulSoup(r.text)

    s = soup.select("td > div[style]")
    used = 0

    cites = soup.select("cite")

    for cite in cites:
        bs = cite.select("b")
        i += 1
        reg = ': |'.join([b.text for b in bs]) + ': '
        parts = re.split(reg, cite.text)
        
        if len(bs) == 0:
            base.append([s[used].text[2:], parts[0]])
            used += 1
        else:
            for j in range(len(parts) - 1):
                base.append([bs[j].text, parts[j + 1]])

    url = "" + soup.select("table.wikitable td[style] > a")[-1]['href']
    if url == "":
        break
    path = "https://losyash-library.fandom.com" + url

    print(len(base), path)

#[print(i) for i in base]

kiki = ['Нюша', 'Бараш', 'Кар-Карыч', 'Рассказчик', 'Крош', 'Ёжик', 'Совунья', 'Лосяш', 'Копатыч', 'Пин']
for k in kiki:
    i = 0
    for b in base:
        if b[0] == k:
            i += 1
    print(k + ":", i)

