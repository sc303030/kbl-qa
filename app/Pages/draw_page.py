from appium.webdriver.common.appiumby import AppiumBy
from app.Pages.base_page import BasePage


class DrawPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.content = (
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="root"]/android.view.View[2]/android.widget.ListView[2]/android.view.View',
        )

        self.participate = (
            AppiumBy.XPATH,
            '//android.widget.Button[@text="Participate"]',
        )

        self.confirm = (
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="root"]/android.view.View/android.view.View[3]/android.view.View/android.view.Button',
        )

    def select_draw(self):
        self.click(self.content)
        self.swipe_down_w3c(
            self.driver.get_window_size(),
            start_x=0.5,
            start_y=0.8,
            end_y=0.2,
            duration=1000,
        )
        self.swipe_down_w3c(
            self.driver.get_window_size(),
            start_x=0.5,
            start_y=0.8,
            end_y=0.2,
            duration=1000,
        )
        self.swipe_down_w3c(
            self.driver.get_window_size(),
            start_x=0.5,
            start_y=0.8,
            end_y=0.2,
            duration=1000,
        )
        self.click(self.participate)
