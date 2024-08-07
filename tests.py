import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


# class HostTest(LiveServerTestCase):
#     def test_home_page(self):
#         driver = webdriver.Chrome()
#         driver.get("http://localhost:8000/")
#         assert "ExMoney" in driver.title


class SignUpTest(LiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.timeout = 10
        self.options = Options()
        self.options.add_argument("--headless")

        self.selenium = webdriver.Chrome(self.options)
        self.selenium.implicitly_wait(self.timeout)

    def test_case_01(self):
        self.selenium.get("http://localhost:8000/account/sign-up")

        last_name_input = self.selenium.find_element(By.NAME, "last_name")
        first_name_input = self.selenium.find_element(By.NAME, "first_name")
        email_input = self.selenium.find_element(By.NAME, "email")
        username_input = self.selenium.find_element(By.NAME, "username")
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password2_input = self.selenium.find_element(By.NAME, "password2")
        sign_up_btn = self.selenium.find_element(By.ID, "btn-sign-up")

        last_name_input.send_keys("Hoàng Dương")
        first_name_input.send_keys("Khánh")
        email_input.send_keys("hdk2002@gmail.com")
        username_input.send_keys("hdkhanh2002")
        password1_input.send_keys("kh@nh2oo2")
        password2_input.send_keys("kh@nh2oo2")
        sign_up_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Đăng nhập vào tài khoản" in driver.page_source
        )

    def test_case_02(self):
        self.selenium.get("http://localhost:8000/account/sign-up")

        last_name_input = self.selenium.find_element(By.NAME, "last_name")
        first_name_input = self.selenium.find_element(By.NAME, "first_name")
        email_input = self.selenium.find_element(By.NAME, "email")
        username_input = self.selenium.find_element(By.NAME, "username")
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password2_input = self.selenium.find_element(By.NAME, "password2")
        sign_up_btn = self.selenium.find_element(By.ID, "btn-sign-up")

        last_name_input.send_keys("Hoàng Dương")
        first_name_input.send_keys("Khánh")
        email_input.send_keys("hdk3003@gmail.com")
        username_input.send_keys("hdkhanh3003")
        password1_input.send_keys("kh@nh3oo3")
        password2_input.send_keys("kh@nh3oo3")
        sign_up_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Tên đăng nhập đã được sử dụng" in driver.page_source
        )

    def test_case_03(self):
        self.selenium.get("http://localhost:8000/account/sign-up")

        last_name_input = self.selenium.find_element(By.NAME, "last_name")
        first_name_input = self.selenium.find_element(By.NAME, "first_name")
        email_input = self.selenium.find_element(By.NAME, "email")
        username_input = self.selenium.find_element(By.NAME, "username")
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password2_input = self.selenium.find_element(By.NAME, "password2")
        sign_up_btn = self.selenium.find_element(By.ID, "btn-sign-up")

        last_name_input.send_keys("Hoàng Dương")
        first_name_input.send_keys("Khánh")
        email_input.send_keys("hdk2002@gmail.com")
        username_input.send_keys("hdkhanh2002")
        password1_input.send_keys("abcd1234")
        password2_input.send_keys("abcd1234")
        sign_up_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Mật khẩu này quá phổ biến" in driver.page_source
        )

    def test_case_04(self):
        self.selenium.get("http://localhost:8000/account/sign-up")

        last_name_input = self.selenium.find_element(By.NAME, "last_name")
        first_name_input = self.selenium.find_element(By.NAME, "first_name")
        email_input = self.selenium.find_element(By.NAME, "email")
        username_input = self.selenium.find_element(By.NAME, "username")
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password2_input = self.selenium.find_element(By.NAME, "password2")
        sign_up_btn = self.selenium.find_element(By.ID, "btn-sign-up")

        last_name_input.send_keys("Hoàng Dương")
        first_name_input.send_keys("Khánh")
        email_input.send_keys("hdk2002@gmail.com")
        username_input.send_keys("hdkhanh2004")
        password1_input.send_keys("hdkhanh2004")
        password2_input.send_keys("hdkhanh2004")
        sign_up_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Mật khẩu quá giống với Tên đăng nhập" in driver.page_source
        )

    def test_case_05(self):
        self.selenium.get("http://localhost:8000/account/sign-up")

        last_name_input = self.selenium.find_element(By.NAME, "last_name")
        first_name_input = self.selenium.find_element(By.NAME, "first_name")
        email_input = self.selenium.find_element(By.NAME, "email")
        username_input = self.selenium.find_element(By.NAME, "username")
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password2_input = self.selenium.find_element(By.NAME, "password2")
        sign_up_btn = self.selenium.find_element(By.ID, "btn-sign-up")

        last_name_input.send_keys("Hoàng Dương")
        first_name_input.send_keys("Khánh")
        email_input.send_keys("hdk2002@gmail.com")
        username_input.send_keys("hdkhanh2002")
        password1_input.send_keys("hdkhanh2002")
        password2_input.send_keys("hdkhanh1001")
        sign_up_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Hai trường mật khẩu không giống nhau" in driver.page_source
        )

    def test_case_06(self):
        self.selenium.get("http://localhost:8000/account/sign-up")

        last_name_input = self.selenium.find_element(By.NAME, "last_name")
        first_name_input = self.selenium.find_element(By.NAME, "first_name")
        email_input = self.selenium.find_element(By.NAME, "email")
        username_input = self.selenium.find_element(By.NAME, "username")
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password2_input = self.selenium.find_element(By.NAME, "password2")
        sign_up_btn = self.selenium.find_element(By.ID, "btn-sign-up")

        last_name_input.send_keys("Hoàng Dương")
        first_name_input.send_keys("Khánh")
        email_input.send_keys("hdk2002gmail.com")
        username_input.send_keys("hdkhanh2002")
        password1_input.send_keys("kh@nh2oo2")
        password2_input.send_keys("kh@nh2oo2")
        sign_up_btn.click()

        is_disabled = sign_up_btn.get_attribute("disabled") == "true" or False
        assert not is_disabled

    def test_case_07(self):
        self.selenium.get("http://localhost:8000/account/sign-up")

        sign_up_btn = self.selenium.find_element(By.ID, "btn-sign-up")
        sign_up_btn.click()

        is_disabled = sign_up_btn.get_attribute("disabled") == "true" or False
        assert not is_disabled


class SignInTest(LiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.timeout = 10
        self.options = Options()
        self.options.add_argument("--headless")

        self.selenium = webdriver.Chrome(self.options)
        self.selenium.implicitly_wait(self.timeout)

    def test_case_08(self):
        self.selenium.get("http://localhost:8000/account/sign-in")

        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")
        sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

        username_input.send_keys("hdkhanh3003")
        password_input.send_keys("kh@nh3oo3")
        sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Số dư" in driver.page_source
        )

    def test_case_09(self):
        self.selenium.get("http://localhost:8000/account/sign-out")
        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Đăng nhập vào tài khoản" in driver.page_source
        )

        self.selenium.get("http://localhost:8000/account/sign-in")

        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")
        sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

        username_input.send_keys("hdkhanh3003")
        password_input.send_keys("kh@nh1oo1")
        sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Vui lòng điền vào Tên đăng nhập và mật khẩu chính xác"
            in driver.page_source
        )

    def test_case_10(self):
        self.selenium.get("http://localhost:8000/account/sign-out")
        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Đăng nhập vào tài khoản" in driver.page_source
        )

        self.selenium.get("http://localhost:8000/account/sign-in")

        sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")
        sign_in_btn.click()

        is_disabled = sign_in_btn.get_attribute("disabled") == "true" or False
        assert not is_disabled


class CategoryTest(LiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.timeout = 10
        self.options = Options()
        self.options.add_argument("--headless")

        self.selenium = webdriver.Chrome(self.options)
        self.selenium.implicitly_wait(self.timeout)

    def test_case_11(self):
        self.selenium.get("http://localhost:8000/category")

        if "Hạng mục cá nhân" not in self.selenium.page_source:
            username_input = self.selenium.find_element(By.NAME, "username")
            password_input = self.selenium.find_element(By.NAME, "password")
            sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

            username_input.send_keys("hdkhanh3003")
            password_input.send_keys("kh@nh3oo3")
            sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Hạng mục cá nhân" in driver.page_source
        )

        open_add_category_modal_btn = self.selenium.find_element(
            By.ID,
            "open-add-category-modal-btn",
        )
        category_name_input = self.selenium.find_element(By.NAME, "name")
        category_type_select = self.selenium.find_element(By.NAME, "type")
        select = Select(category_type_select)
        expense_option = self.selenium.find_element(
            By.CSS_SELECTOR,
            "option[value='2']",
        )
        add_category_btn = self.selenium.find_element(
            By.ID,
            "add-category-btn",
        )

        open_add_category_modal_btn.click()
        time.sleep(2)

        category_name_input.send_keys("Quần Áo")
        select.select_by_visible_text("Chi tiêu")
        assert expense_option.is_selected()
        add_category_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Thêm hạng mục thành công" in driver.page_source
        )

    def test_case_12(self):
        self.selenium.get("http://localhost:8000/category")

        if "Hạng mục cá nhân" not in self.selenium.page_source:
            username_input = self.selenium.find_element(By.NAME, "username")
            password_input = self.selenium.find_element(By.NAME, "password")
            sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

            username_input.send_keys("hdkhanh3003")
            password_input.send_keys("kh@nh3oo3")
            sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Hạng mục cá nhân" in driver.page_source
        )

        open_add_category_modal_btn = self.selenium.find_element(
            By.ID,
            "open-add-category-modal-btn",
        )
        add_category_btn = self.selenium.find_element(By.ID, "add-category-btn")

        open_add_category_modal_btn.click()
        time.sleep(2)
        add_category_btn.click()

        is_disabled = add_category_btn.get_attribute("disabled") == "true" or False
        assert not is_disabled


class TransactionTest(LiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.timeout = 10
        self.options = Options()
        self.options.add_argument("--headless")

        self.selenium = webdriver.Chrome(self.options)
        self.selenium.implicitly_wait(self.timeout)

    def test_case_13(self):
        self.selenium.get("http://localhost:8000/transaction")

        if "Lịch sử giao dịch" not in self.selenium.page_source:
            username_input = self.selenium.find_element(By.NAME, "username")
            password_input = self.selenium.find_element(By.NAME, "password")
            sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

            username_input.send_keys("hdkhanh3003")
            password_input.send_keys("kh@nh3oo3")
            sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Lịch sử giao dịch" in driver.page_source
        )

        open_add_transaction_modal_btn = self.selenium.find_element(
            By.ID,
            "open-add-transaction-modal-btn",
        )
        transaction_name_input = self.selenium.find_element(By.NAME, "name")
        transaction_type_select = self.selenium.find_element(By.NAME, "category")
        transaction_amount_input = self.selenium.find_element(By.NAME, "amount")
        transaction_date_input = self.selenium.find_element(By.NAME, "date")
        select = Select(transaction_type_select)
        food_expense_option = self.selenium.find_element(
            By.CSS_SELECTOR,
            "option[value='12']",
        )
        # tourism_expense_option = self.selenium.find_element(
        #     By.CSS_SELECTOR,
        #     "option[value='13']",
        # )
        add_transaction_btn = self.selenium.find_element(
            By.ID,
            "add-transaction-btn",
        )

        open_add_transaction_modal_btn.click()
        time.sleep(2)

        transaction_name_input.send_keys("Ăn trưa 06 th8")
        select.select_by_visible_text("Ăn Uống")
        assert food_expense_option.is_selected()
        transaction_amount_input.send_keys("50000")
        transaction_date_input.send_keys("06-08-2024")
        add_transaction_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Thêm giao dịch thành công" in driver.page_source
        )

    def test_case_14(self):
        self.selenium.get("http://localhost:8000/transaction")

        if "Lịch sử giao dịch" not in self.selenium.page_source:
            username_input = self.selenium.find_element(By.NAME, "username")
            password_input = self.selenium.find_element(By.NAME, "password")
            sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

            username_input.send_keys("hdkhanh3003")
            password_input.send_keys("kh@nh3oo3")
            sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Lịch sử giao dịch" in driver.page_source
        )

        open_add_transaction_modal_btn = self.selenium.find_element(
            By.ID,
            "open-add-transaction-modal-btn",
        )
        transaction_name_input = self.selenium.find_element(By.NAME, "name")
        transaction_type_select = self.selenium.find_element(By.NAME, "category")
        transaction_amount_input = self.selenium.find_element(By.NAME, "amount")
        transaction_date_input = self.selenium.find_element(By.NAME, "date")
        select = Select(transaction_type_select)
        # food_expense_option = self.selenium.find_element(
        #     By.CSS_SELECTOR,
        #     "option[value='12']",
        # )
        tourism_expense_option = self.selenium.find_element(
            By.CSS_SELECTOR,
            "option[value='13']",
        )
        add_transaction_btn = self.selenium.find_element(
            By.ID,
            "add-transaction-btn",
        )

        open_add_transaction_modal_btn.click()
        time.sleep(2)

        transaction_name_input.send_keys("Du lịch T8")
        select.select_by_visible_text("Du Lịch")
        assert tourism_expense_option.is_selected()
        transaction_amount_input.send_keys("-5000000")
        transaction_date_input.send_keys("06-08-2024")
        add_transaction_btn.click()

        is_disabled = add_transaction_btn.get_attribute("disabled") == "true" or False
        assert not is_disabled

    def test_case_15(self):
        self.selenium.get("http://localhost:8000/transaction")

        if "Lịch sử giao dịch" not in self.selenium.page_source:
            username_input = self.selenium.find_element(By.NAME, "username")
            password_input = self.selenium.find_element(By.NAME, "password")
            sign_in_btn = self.selenium.find_element(By.ID, "btn-sign-in")

            username_input.send_keys("hdkhanh3003")
            password_input.send_keys("kh@nh3oo3")
            sign_in_btn.click()

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: "Lịch sử giao dịch" in driver.page_source
        )

        open_add_transaction_modal_btn = self.selenium.find_element(
            By.ID,
            "open-add-transaction-modal-btn",
        )
        add_transaction_btn = self.selenium.find_element(
            By.ID,
            "add-transaction-btn",
        )

        open_add_transaction_modal_btn.click()
        time.sleep(2)
        add_transaction_btn.click()

        is_disabled = add_transaction_btn.get_attribute("disabled") == "true" or False
        assert not is_disabled
