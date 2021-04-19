from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#scapes https://redplanetscience.com/ and finds a title and a paragraph
def scrape_mars():
    
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://redplanetscience.com/"
    browser.visit(url)
    
    #time.sleep(1)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    news = {}
    news["title"] = soup.find("div", class_="content_title").get_text()
    news["parag"] = soup.find("div", class_="article_teaser_body").get_text()
    
    browser.quit()
    
    return news

# scrapes https://spaceimages-mars.com/ to find featured image url
def feature_img():
    
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    
    #time.sleep(1)
    

    html = browser.html
    soup = bs(html, "html.parser")
    
    featured_image_url = soup.find("img", class_="headerimage fade-in")['src']
    complete_img_url = url + featured_image_url
    ft_image = dict({"img_url": complete_img_url})
    
    browser.quit()
    
    return ft_image

# scrapes https://galaxyfacts-mars.com/ to find Mar's facts table
def table_facts():
    
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    
    #time.sleep(1)
    
    facts = pd.read_html(url)

    table = facts[1]    
    html_string = table.to_html(header=False, index=False)  
    html_str = html_string.replace('table border="1" class="dataframe"', 'table class="table table-striped table-dark table-hover"')
    
    
    browser.quit()
    
    return html_str

# scrapes https://marshemispheres.com/ to find high definition images from Mar's hemispheres

def hemispheres_images():
    
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://marshemispheres.com/"
    urls = ["cerberus.html", "schiaparelli.html", "syrtis.html", "valles.html"]
    
    img_titles = []
    img_urls = []
    hemispheres_images_urls = []
    
    for i in urls:
        
        browser.visit(url + i)
    
        html = browser.html
        soup = bs(html, "html.parser")
        
        img_title = soup.find("h2", class_="title").get_text()
        img_url = soup.find("img", class_="wide-image")['src']
        complete_url = url + img_url
        img_titles.append(img_title)
        img_urls.append(complete_url)
        dic = dict({"title": img_title, "im_url": complete_url})
        hemispheres_images_urls.append(dic)
        
    # zero = hemispheres_images_urls[0]
    # one = hemispheres_images_urls[1]
    # two = hemispheres_images_urls[2]  
    # three =  hemispheres_images_urls[3]
    
    browser.quit()
    
    return hemispheres_images_urls



