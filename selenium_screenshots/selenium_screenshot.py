# -*- coding: utf-8 -*-
"""
Selenium Screenshot Demonstration

@author: high_ticket
"""


# Import Modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up driver and navigate
driver = webdriver.Chrome()
driver.get('https://finance.yahoo.com/')

# Take a screenshot
driver.get_screenshot_as_file(r'C:\Users\test_user\Documents\output\screenshot1.png')


# Search for Ticker
ticker_input = driver.find_element(by='id', value='ybar-sbq')
ticker_input.send_keys('IBM')
ticker_search = driver.find_element(By.CLASS_NAME, value='_yb_636id0')
ticker_search.click()

# Get Ticker Screenshot
body = driver.find_element(By.ID, value='atomic')
body.send_keys(Keys.PAGE_DOWN)
driver.get_screenshot_as_file(r'C:\Users\test_user\Documents\output\screenshot2.png')
