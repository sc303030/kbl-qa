from app.TestBase.base_test import BaseTest
from app.Pages.home_page import HomePage
import os


class MainTest(BaseTest):
    def test_verify_example_element(self):
        home_page = HomePage(self.driver)

        home_page.close_popup_if_present()
        home_page.click_schedules_version_button("default")
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        home_page.login(email, password)
