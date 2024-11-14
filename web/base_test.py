import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    KBL_DOMAIN = "https://www.kbl.or.kr/"
    IMPLICIT_WAIT_TIME = 3

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.driver.start_client()
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.kbl_domain = self.KBL_DOMAIN

    def tearDown(self):
        pass
        # self.driver.quit()
