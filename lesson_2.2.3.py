import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
browser.switch_to.alert.accept()

time.sleep(10)
