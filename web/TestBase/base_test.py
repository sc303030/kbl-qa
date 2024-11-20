import unittest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()


class BaseTest(unittest.TestCase):
    KBL_DOMAIN = "https://www.kbl.or.kr/"
    IMPLICIT_WAIT_TIME = 3

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")

        env = os.getenv("ENV")
        if env == "production":
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--user-data-dir=/tmp/selenium/user-data-dir")

        self.driver = webdriver.Chrome(options=options)
        self.driver.start_client()
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
