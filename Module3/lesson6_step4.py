import pytest
import time
import math

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('link', links)
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, link):
        # link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        inp_answer = browser.find_element_by_css_selector("#ember67.string-quiz__textarea")
        answer = math.log(int(time.time()))
        inp_answer.send_keys(str(answer))
        btn_submit = browser.find_element_by_css_selector(".submit-submission")
        btn_submit.click()
        result = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        assert result == "Correct!"




