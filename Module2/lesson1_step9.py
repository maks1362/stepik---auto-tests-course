from selenium import webdriver
import time

import math


link = "http://suninjuly.github.io/selects1.html"

try:
    from selenium import webdriver

    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()