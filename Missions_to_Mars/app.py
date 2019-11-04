from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/dbname"
mongo = PyMongo(app)

@app.route("/")
def index():
    listings = mongo.db.collname.find_one()
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scraper():
    listings = mongo.db.collname
    listings_data = scrape_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)



# from splinter import Browser
# from splinter.exceptions import ElementDoesNotExist
# from bs4 import BeautifulSoup

# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)

# url = 'http://books.toscrape.com/'
# browser.visit(url)

# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')

# sidebar = soup.find('ul', class_='nav-list')

# categories = sidebar.find_all('li')

# category_list = []
# url_list = []
# book_url_list = []
# for category in categories:
#     title = category.text.strip()
#     category_list.append(title)
#     book_url = category.find('a')['href']
#     url_list.append(book_url)

# book_url_list = ['http://books.toscrape.com/' + url for url in url_list]

# titles_and_urls = zip(category_list, book_url_list)

# try:
#     for title_url in titles_and_urls:
#         browser.click_link_by_partial_text('next')
# except ElementDoesNotExist:
#     print("Scraping Complete")
    
# book_url_list

