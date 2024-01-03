import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


x_value = browser.find_element(By.ID, "input_value").get_property("textContent")
y = calc(x_value)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(float(y))
browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

time.sleep(10)
