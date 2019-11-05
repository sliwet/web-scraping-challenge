from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # NASA Mars News
    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)
    time.sleep(3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    slides = soup.find_all('li', class_='slide')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    content_title = slides[0].find('div', class_='content_title')
    news_title = content_title.text.strip()

    article_teaser_body = slides[0].find('div', class_='article_teaser_body')
    news_p = article_teaser_body.text.strip()

    # JPL Mars Space Images

    base_url = 'https://www.jpl.nasa.gov'
    url = base_url + '/spaceimages/?search=&category=Mars'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = base_url + soup.find('a',class_='button fancybox')['data-fancybox-href']    

    # Mars Weather

    url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    streamitems = soup.find_all('li', class_='js-stream-item stream-item stream-item')

    i = 0
    while streamitems[i].find('strong',class_='fullname').text.strip() != 'Mars Weather':
        i = i+1
    mars_weather = streamitems[i].find('div',class_='js-tweet-text-container')
    mars_weather = mars_weather.find('p').text

    # Mars facts

    url = 'https://space-facts.com/mars/'

    df = pd.read_html(url)[1]
    df = df.rename(columns={0:"Description", 1:"Value"})
    df = df.set_index("Description")
    marsfacts_html = df.to_html().replace('\n', '')

    # Assigning scraped data to a page

    marspage = {}
    marspage["news_title"] = news_title
    marspage["news_p"] = news_p
    marspage["featured_img"] = featured_image_url
    marspage["mars_weather"] = mars_weather
    marspage["mars_facts"] = marsfacts_html

    return marspage
    
