from base_test import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
from selenium.webdriver.common.by import By

"""
TC ID : 홈_002
When: 홈페이지에 있는 스케줄 카드 호버 시 3가지 엘레멘트가 보여지는지
Then: 티켓예매, 프리뷰, Challenge 3가지 버튼이 정상적으로 보여짐
"""


class Home002(BaseTest):
    def event(self):
        self.driver.get(self.kbl_domain)
        schedule_card_elements = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/main/div[1]/div[2]/div[1]/div/div[1]'
        )
        actions = ActionChains(self.driver)
        time.sleep(2)
        actions.move_to_element(schedule_card_elements).perform()

    def test_all(self):
        self.event()


if __name__ == "__main__":
    unittest.main()
