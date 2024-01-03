import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_value = browser.find_element(By.ID, "input_value").get_property("textContent")
y = calc(x_value)

target = browser.find_element(By.CSS_SELECTOR, "#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", target)
target.send_keys(float(y))

target = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", target)
target.click()

target = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", target)
target.click()

target = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", target)
target.click()

time.sleep(10)
