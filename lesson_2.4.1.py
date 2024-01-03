import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
text = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element(By.ID, "book").click()

x_value = browser.find_element(By.ID, "input_value").get_property("textContent")
y = calc(x_value)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(float(y))
browser.find_element(By.CSS_SELECTOR, "button#solve").click()

time.sleep(10)
