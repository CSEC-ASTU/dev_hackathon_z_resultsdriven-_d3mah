
import requests
from bs4 import BeautifulSoup
from .models import *


def scrape_medium_user_blog():
    url = 'https://medium.com/@mukeremali112'
    # url = 'https://medium.com/@cole_ruche'

    # Send a GET request to the Medium user's profile page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the blog post titles and URLs
        # post_links = soup.find_all('div')["aria-label"]
        post_links = soup.findAll(lambda tag: tag.name ==
                                  "a" and "aria-label" in tag.attrs)
        print(post_links)
        Blog.objects.all().delete()
        for link in post_links:
            if link["aria-label"] == "Post Preview Title":
                post_title = link.find("h2").text
                post_desc = link.find("p").text
                post_url = link['href']
                ff = soup.findAll(lambda tag: tag.name ==
                                  "a" and tag.attrs["href"] == link['href'])
                length = ff[-1].find("span").text
                date = ff[0].find("p").text
                print(post_desc)
                Blog.objects.create(date=date, length=length,
                                    title=post_title, description=post_desc, url=post_url)

        return
    return None


# scrape_medium_user_blog()
