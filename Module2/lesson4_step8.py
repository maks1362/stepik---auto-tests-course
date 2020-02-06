from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # Ваш код, который заполняет обязательные поля
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    is_cheap = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    #if (is_cheap):
    print(is_cheap)
    browser.find_element_by_css_selector(".btn#book").click()

    input_x = browser.find_element_by_css_selector(".nowrap#input_value")
    x = input_x.text
    y = calc(int(x))
    time.sleep(1)

    input_answer = browser.find_element_by_css_selector("#answer[required]")
    input_answer.send_keys(str(y))

    btn = browser.find_element_by_css_selector(".btn.btn-primary[type='submit']")
  
    time.sleep(1)
    btn.click()
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()