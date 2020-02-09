import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):

    def test_first_page(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link) 
        # Ваш код, который заполняет обязательные поля
        
        input = browser.find_element_by_css_selector("input.first[required]")
        input.send_keys("Maxec")
        
        input = browser.find_element_by_css_selector("input.second[required]")
        input.send_keys("Alexeev")

        input = browser.find_element_by_css_selector("input.third[required]")
        input.send_keys("max@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)
        print("first OK")
        time.sleep(1.5)
        browser.quit()
        
    def test_second_page(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link) 
        # Ваш код, который заполняет обязательные поля
        
        input = browser.find_element_by_css_selector("input.first[required]")
        input.send_keys("Maxec")
        
        input = browser.find_element_by_css_selector("input.second[required]")
        input.send_keys("Alexeev")

        input = browser.find_element_by_css_selector("input.third[required]")
        input.send_keys("max@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)
        print("second sucsesfull")
        time.sleep(1.5)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
