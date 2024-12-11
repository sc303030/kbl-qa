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
        self.click_menu(self.sub_menu, sub_menu_name)
