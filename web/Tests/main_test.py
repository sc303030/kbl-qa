from web.Pages.record_page import RecordPage
from web.Pages.ticket_page import TicketPage
from web.TestBase.base_test import BaseTest
from web.Pages.home_page import HomePage
import os


class MainTest(BaseTest):
    def test_visit_kbl_homepage(self):
        self.driver.get("https://kbl.or.kr/")
        home_page = HomePage(self.driver)
        ticket_page = TicketPage(self.driver)

        self.assertTrue(
            home_page.verify_logo_present(), "홈페이지 로고가 보이지 않습니다."
        )

        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        home_page.login(email, password)
        home_page.get_text_and_memu_click("티켓")
        home_page.hover_after_mouse_move(100, 100)
        ticket_page.click_price_or_booking("티켓예매")
