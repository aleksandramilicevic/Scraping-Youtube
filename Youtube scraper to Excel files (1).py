#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

#from bs4 import BeautifulSoup
#import requests



options = webdriver.ChromeOptions()
#All are optional
options.add_experimental_option("detach", True)
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
options.add_argument("--disable-Advertisement")
options.add_argument("--disable-popup-blocking")
options.add_argument("start-maximized")

driver= webdriver.Chrome(options=options)


#driver = webdriver.Chrome() 
#driver.implicitly_wait(10)

path = "https://youtube.com"
driver.get(path)

#xpath for search box
x_path_for_box = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"
searching_point_box = driver.find_element(By.XPATH, value=x_path_for_box)

#user manual input
search_word = input("Enter the search keyword: ")
searching_point_box.send_keys(search_word)

#xpath for search button
x_path_search_button= "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button"
searchButton = driver.find_element(By.XPATH, value=x_path_search_button)
searchButton.click()

new_path ="https://www.youtube.com/results?search_query=" + search_word
driver.get(new_path)

item = []
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.documentElement.scrollHeight")

item_count = 0

while item_count < 10:
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height
    


links = driver.find_elements(By.TAG_NAME, value = "a")

links


list_of_links = []
for link in links:
    #print(link.get_attribute("href"))
    href = link.get_attribute("href")
    list_of_links.append(href)
    
list_of_links
    
    
    

#print(list_of_links)


#turl = driver.find_element(By.CSS_SELECTOR,'a#video-title-link').get_attribute('href')
#title_list = []

#for title in turl:
#    title_list.append(title)

#print(turl)
#print(new_path)

    
#title_list




# 
# 

# In[ ]:




