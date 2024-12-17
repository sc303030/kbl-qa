import time

from web.Pages.record_page import RecordPage
from web.Pages.ticket_page import TicketPage
from web.TestBase.base_test import BaseTest
from web.Pages.home_page import HomePage
import os


class MainTest(BaseTest):
    def test_visit_kbl_homepage(self):
        self.driver.get("https://kbl.or.kr/")
        home_page = HomePage(self.driver)

        self.assertTrue(
            home_page.verify_logo_present(), "홈페이지 로고가 보이지 않습니다."
        )

        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        home_page.login(email, password)
        time.sleep(1)
        assert (
            home_page.verify_logout_button()
        ), "로그인 후 로그아웃 버튼이 표시되지 않았습니다."
