from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    # Ваш код, который заполняет обязательные поля
    browser = webdriver.Chrome()
    browser.get(link)

    input_x = browser.find_element_by_css_selector("#input_value")
    x = input_x.text
    y = calc(x)

    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()


    input_answer = browser.find_element_by_css_selector("#answer[required]")
    input_answer.send_keys(y)
    btn = browser.find_element_by_css_selector(".btn[type='submit']")
    time.sleep(1)
    btn.click()
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()