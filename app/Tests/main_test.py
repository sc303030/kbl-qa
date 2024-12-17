from app.TestBase.base_test import BaseTest
from app.Pages.home_page import HomePage
from app.Pages.my_page import MyPage
import os


class MainTest(BaseTest):
    def test_verify_example_element(self):
        home_page = HomePage(self.driver)
        my_page = MyPage(self.driver)

        home_page.close_popup_if_present()
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        home_page.login(email, password)
        home_page.click_user_button()
        my_page_element = my_page.verify_logout_button()
        assert my_page_element.is_displayed()
