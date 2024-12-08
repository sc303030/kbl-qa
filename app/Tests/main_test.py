from app.TestBase.base_test import BaseTest
from app.Pages.home_page import HomePage
from app.Pages.draw_page import DrawPage
import os


class MainTest(BaseTest):
    def test_verify_example_element(self):
        home_page = HomePage(self.driver)
        draw_page = DrawPage(self.driver)

        home_page.close_popup_if_present()
        home_page.click_schedules_version_button("default")
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        home_page.login(email, password)
        home_page.click_draw()

        draw_page.select_draw()
