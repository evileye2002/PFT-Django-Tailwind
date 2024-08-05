import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# class HostTest(LiveServerTestCase):
#     def test_home_page(self):
#         driver = webdriver.Chrome()
#         driver.get("http://localhost:8000/")
#         assert "ExMoney" in driver.title


class SignInTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    def test_form(self):
        self.selenium.get("http://localhost:8000/account/sign-in")

        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")
        sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

        username_input.send_keys("admin")
        password_input.send_keys("kh@nh2002")
        sign_in_btn.click()

        WebDriverWait(self.selenium, 15).until(
            lambda driver: "Số dư" in driver.page_source
        )
