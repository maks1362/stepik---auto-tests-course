from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    # Ваш код, который заполняет обязательные поля
    browser = webdriver.Chrome()
    browser.get(link)

    input_x = browser.find_element_by_id("treasure")
    x = input_x.get_attribute("valuex")
    y = calc(x)

    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()

    people_radio = browser.find_element_by_id("robotCheckbox")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

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