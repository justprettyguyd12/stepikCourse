import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

selector_value = "#input_value"
x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.text
y = calc(x)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(float(y))
browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()

time.sleep(10)