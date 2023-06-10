import json
import requests
from bs4 import BeautifulSoup

from app.scrape_medium import scrape_medium_user_blog 
from .models import Stats
 


def scrap_leetcode():
    response = requests.get("https://leetcode.com/mukeremali112/")
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find_all(
        "div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")[0]

    rank_element = soup.find_all(
        "span", class_="ttext-label-1 dark:text-dark-label-1 font-medium")[0]

    score = score_element.text.strip() if score_element else "N/A"
    rank = rank_element.text.strip() if rank_element else ""

    Stats.objects.filter(site="leetcode").update(rank=rank, score=score)


def scrap_codeforces():
    url = "https://codeforces.com/api/user.info?handles=mukeremali"
    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json()['result'][0]
        print(data)
        rating = str(data["maxRating"])
        rank = data["maxRank"]
        print(rank, rating)
        Stats.objects.filter(site="codeforces").update(
            rank=rating, score=str(rank))


def scrap_kattis():
    url = f"https://open.kattis.com/users/mukerem"
    data = {"script": "true"}
    page_content = requests.get(url=url, data=data)
    soup = BeautifulSoup(page_content.text, "html.parser")

    infos = soup.find_all('div', attrs={'class': 'divider_list-item'})
    data = {}
    for info in infos:
        spans = info.find_all('span')
        if spans:
            key = spans[0].get_text()
            value = spans[1].get_text()
            data[key] = value
    rank = data["Rank"]
    score = data["Score"]
    Stats.objects.filter(site="kattis").update(rank=rank, score=score)
 
def stat_update():
    scrap_kattis()
    scrap_codeforces()
    scrap_leetcode()
    scrape_medium_user_blog()
