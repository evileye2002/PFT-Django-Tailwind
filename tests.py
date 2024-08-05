import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


# class HostTest(LiveServerTestCase):
#     def test_home_page(self):
#         driver = webdriver.Chrome()
#         driver.get("http://localhost:8000/")
#         assert "ExMoney" in driver.title


class SignInTest(LiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.timeout = 10
        self.options = Options()
        # self.options.add_argument("--headless")

        self.selenium = webdriver.Chrome(self.options)
        self.selenium.implicitly_wait(self.timeout)

    def test_case_01(self):
        self.selenium.get("http://localhost:8000/account/sign-in")

        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")
        sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

        username_input.send_keys("admin")
        password_input.send_keys("kh@nh2002")
        sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Số dư" in driver.page_source
        )

    def test_case_02(self):
        self.selenium.get("http://localhost:8000/account/sign-out")
        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Đăng nhập" in driver.page_source
        )

        self.selenium.get("http://localhost:8000/account/sign-in")

        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")
        sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

        username_input.send_keys("admin")
        password_input.send_keys("kh@nh2001")
        sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Vui lòng điền vào Tên đăng nhập và mật khẩu chính xác"
            in driver.page_source
        )

    def test_case_03(self):
        self.selenium.get("http://localhost:8000/account/sign-out")
        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Đăng nhập" in driver.page_source
        )

        self.selenium.get("http://localhost:8000/account/sign-in")

        sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")
        sign_in_btn.click()

        is_disabled = sign_in_btn.get_attribute("disabled") == "true" or False
        assert not is_disabled
