import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

selector_value = "img#treasure"
x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.get_attribute("valuex")
y = calc(x)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(float(y))
browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()

time.sleep(10)