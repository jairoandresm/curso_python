import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

def find_hashtags(hashtag):
    driver = webdriver.Chrome()
    driver.get('https://twitter.com/hashtag/' + hashtag + '?src=hash')
    for i in range(100):
        print(i)
        driver.execute_script("window.scrollTo(0, 100000)")
        time.sleep(1.5)