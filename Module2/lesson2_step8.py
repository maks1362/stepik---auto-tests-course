from selenium import webdriver
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    # Ваш код, который заполняет обязательные поля
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_css_selector(".form-group [name='firstname']")
    input_name.send_keys('Maxec')
    input_name = browser.find_element_by_css_selector(".form-group [name='lastname']")
    input_name.send_keys('smir')
    input_name = browser.find_element_by_css_selector(".form-group [name='email']")
    input_name.send_keys('@aaaa')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    input_name = browser.find_element_by_css_selector("#file[accept='.txt'][name='file']")
    input_name.send_keys(file_path)

    btn = browser.find_element_by_css_selector("button.btn[type='submit']")

    time.sleep(1)
    btn.click()
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()