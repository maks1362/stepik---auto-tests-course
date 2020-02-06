from selenium import webdriver
import time

import math


link = "http://suninjuly.github.io/selects2.html"

try:
    # Ваш код, который заполняет обязательные поля
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    
    y = num1 + num2

    select = webdriver.support.ui.Select(browser.find_element_by_css_selector(".custom-select"))
    select.select_by_visible_text(str(y))
    
    btn = browser.find_element_by_css_selector(".btn[type='submit'].btn-default")
    time.sleep(1)
    btn.click()
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()