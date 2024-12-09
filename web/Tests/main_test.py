from web.Pages.record_page import RecordPage
from web.TestBase.base_test import BaseTest
from web.Pages.home_page import HomePage


class MainTest(BaseTest):
    def test_visit_kbl_homepage(self):
        self.driver.get("https://kbl.or.kr/")
        home_page = HomePage(self.driver)
        record_page = RecordPage(self.driver)

        self.assertTrue(
            home_page.verify_logo_present(), "홈페이지 로고가 보이지 않습니다."
        )

        home_page.get_text_and_memu_click("기록")
        home_page.hover_after_mouse_move(100, 100)
        record_page.click_record_category("팀기록")
