# Design process
# 1. Open an article
# 2. Find the first article in the page
# 3. Follow the link
# 4. Record the link in article_chain data structure
# 5. Repeat the process until we reach the Philosophy article, or get struck in article cycle

import time
import urllib

import requests
from bs4 import BeautifulSoup


def continue_crawl(search_history_list, target_url="https://en.wikipedia.org/wiki/Philosophy", max_steps=25):
    if len(search_history_list) > max_steps:
        print("Crawl limit exceeding:", max_steps)
        return False
    elif search_history_list[-1] in search_history_list[:-1]:
        print("list has a cycle")
        return False
    elif search_history_list[-1] == target_url:
        print("Target url found")
        return False
    else:
        return True


def find_first_link(url):
    # get the html from the url using requests library
    response = requests.get(url)
    html = response.text
    # feed the html to Beautiful soup library
    soup = BeautifulSoup(html, 'html.parser')

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # find the first link in html
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    # return the first link as a string, or return None if there is no link
    if not article_link:
        return
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link


def web_crawl():
    start_url = "https://en.wikipedia.org/wiki/Special:Random"
    article_chain = [start_url]
    while continue_crawl(article_chain):
        # download html of last article in article_chain
        # find the first link in that html
        print(article_chain[-1])
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        time.sleep(2)


web_crawl()
