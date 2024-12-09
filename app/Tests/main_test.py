from app.TestBase.base_test import BaseTest
from app.Pages.home_page import HomePage
from app.Pages.record_page import RecordPage


class MainTest(BaseTest):
    def test_verify_example_element(self):
        home_page = HomePage(self.driver)
        record_page = RecordPage(self.driver)

        home_page.close_popup_if_present()
        home_page.click_tab()
        home_page.click_menu("Record")
        record_page.click_sub_menu("Team record")
