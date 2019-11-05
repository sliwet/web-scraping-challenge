from splinter import Browser
from bs4 import BeautifulSoup

def scrape():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # NASA Mars News
    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)
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

    marspage = {}
    marspage["news_title"] = news_title
    marspage["news_p"] = news_p
    marspage["featured_img"] = featured_image_url

    return marspage
    
