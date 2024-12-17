from appium.webdriver.common.appiumby import AppiumBy
from app.Pages.base_page import BasePage


class MyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.my_page = (AppiumBy.XPATH, '//android.widget.TextView[@text="My Page"]')

    def verify_logout_button(self):
        return self.get_element(self.my_page)
