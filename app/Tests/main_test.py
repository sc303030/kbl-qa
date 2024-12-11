from app.TestBase.base_test import BaseTest
from app.Pages.home_page import HomePage
from app.Pages.ticket_page import TicketPage
import os


class MainTest(BaseTest):
    def test_verify_example_element(self):
        home_page = HomePage(self.driver)
        ticket_page = TicketPage(self.driver)

        home_page.close_popup_if_present()
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        home_page.login(email, password)
        home_page.click_tab()
        home_page.change_language()
        home_page.click_tab_menu("티켓")
        ticket_page.click_sub_menu("정규시즌")
        ticket_page.click_price_or_booking("티켓예매")
