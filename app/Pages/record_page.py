from appium.webdriver.common.appiumby import AppiumBy
from app.Pages.base_page import BasePage


class RecordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sub_menu = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View',
        )

    def click_sub_menu(self, sub_menu_name: str):
        elements = self.get_elements(self.sub_menu)
        for element in elements:
            content_desc = element.get_attribute("content-desc")
            if content_desc == sub_menu_name:
                element.click()
                break
