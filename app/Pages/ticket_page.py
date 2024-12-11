from appium.webdriver.common.appiumby import AppiumBy
from app.Pages.base_page import BasePage


class TicketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sub_menu = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View',
        )

        self.price_or_booking = (
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="root"]/android.view.View[2]/android.widget.ListView[2]/android.view.View[1]/android.widget.Button',
        )

    def click_sub_menu(self, sub_menu_name: str):
        self.click_menu(self.sub_menu, sub_menu_name)

    def click_price_or_booking(self, price_or_booking_name: str):
        elements = self.get_elements(self.price_or_booking)
        if price_or_booking_name == "가격안내":
            elements[0].click()
        else:
            elements[1].click()
