from appium.webdriver.common.appiumby import AppiumBy
from app.Pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.popup_close_button_locator = (AppiumBy.XPATH, "//android.webkit.WebView")

    def close_popup_if_present(self):
        try:
            popup_close_button = self.get_element(self.popup_close_button_locator)
            popup_close_button.click()
        except:
            pass
