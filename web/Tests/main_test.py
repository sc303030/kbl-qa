from web.TestBase.base_test import BaseTest
from web.Pages.home_page import HomePage
import time


class MainTest(BaseTest):
    def test_visit_kbl_homepage(self):
        self.driver.get("https://kbl.or.kr/")
        home_page = HomePage(self.driver)

        self.assertTrue(
            home_page.verify_logo_present(), "홈페이지 로고가 보이지 않습니다."
        )

        slide_card_count = home_page.get_slide_card_count()
        self.assertEqual(
            slide_card_count,
            9,
            f"슬라이드 카드의 개수는 9개가 아닙니다. 현재 개수: {slide_card_count}",
        )
        time.sleep(3)
        home_page.hover_team_select_div()
