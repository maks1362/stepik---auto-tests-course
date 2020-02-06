from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    # Ваш код, который заполняет обязательные поля
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    browser.find_element_by_css_selector(".btn.trollface").click()
    time.sleep(1)

    window_name = browser.window_handles[1]
    btn = browser.switch_to_window(window_name)

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
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()