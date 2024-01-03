import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.CSS_SELECTOR, "#num1").get_property("textContent")
y = browser.find_element(By.CSS_SELECTOR, "#num2").get_property("textContent")
summa = int(x) + int(y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(summa))
browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()

time.sleep(10)