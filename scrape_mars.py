import requests
import pymongo
import pandas as pd

   
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver


def scrape():
    # Set up Splinter
    executable_path = {'executable_path': '/Users/amybednarz/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

#NASA Mars News 

    mars_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_url)

    html = browser.html
    mars_news_soup= bs(html,'html.parser')

#find title and paragraph

    mars_title = mars_news_soup.body.find("div", class_= "content_title")
    mars_paragraph = mars_news_soup.body.find("div", class_= "article_teaser_body")
    print(mars_title)
    print(mars_paragraph)


    #JPL Mars Space Images - Featured Image
    mars_image_url = "https://spaceimages-mars.com/"
    browser.visit(mars_image_url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html
    mars_image_soup= bs(html,'html.parser')
    mars_image_url = mars_image_soup.body.find("img", class_= "fancybox-image")
    mars_image_url['src']

    
    # Mars Facts
    mars_facts_url = "https://galaxyfacts-mars.com/"
    mars_table =  pd.read_html(mars_facts_url)
    mars_table
    #time.sleep(5)

    mars_table_df = mars_table[1]

    mars_table_df.columns = ['Describe', 'Values']
    mars_table_df

    mars_table_html = mars_table_df.to_html()
    print(mars_table_html)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Mars Hemispheres
    mars_hemisphere_url = "https://marshemispheres.com/"
    browser.visit(mars_hemisphere_url)

    # Mars Dictionary 
    mars_hemisphere_url_dict = [
        {"title": "Valles Marineris Hemisphere", "img_url_vm": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
         {"title": "Cerberus Hemisphere", "img_url_ch": "https://marshemispheres.com/images/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url_sh": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url-smh": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
    ]

    #quit browser
    browser.quit()
    return mars_hemisphere_url_dict 
    