import unittest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

USE_DEVICE_FARM = os.getenv("use_device_farm")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv()


class BaseTest(unittest.TestCase):
    IMPLICIT_WAIT_TIME = 10

    def setUp(self):
        desired_caps = {}
        if USE_DEVICE_FARM:
            url = "http://127.0.0.1:4723/wd/hub"
        else:
            url = "http://127.0.0.1:4723"
            desired_caps["platformName"] = "Android"
            desired_caps["deviceName"] = "emulator-5554"
            desired_caps["automationName"] = "uiautomator2"
            desired_caps["app"] = f"{os.getenv('APP_DIR')}"
            desired_caps["autoGrantPermissions"] = True
            desired_caps["newCommandTimeout"] = 3600

        self.driver = webdriver.Remote(
            url, options=UiAutomator2Options().load_capabilities(desired_caps)
        )
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
