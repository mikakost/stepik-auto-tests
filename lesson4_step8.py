from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math, time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
WebDriverWait(browser, 12).until(
    ec.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element(By.ID, "book")
button.click()

# говорим WebDriver ждать все элементы в течение секунды
browser.implicitly_wait(1)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

alert_text = browser.switch_to.alert.text
print(alert_text.split(" ")[-1])

browser.quit()
