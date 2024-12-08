from appium.webdriver.common.appiumby import AppiumBy
from app.Pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.popup_close_button_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@text="Close"]',
        )
        self.team_select_button_locator = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View',
        )

        self.schedules_version_button = (
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="root"]/android.view.View/android.view.View[1]/android.view.View',
        )

        self.user_icon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[4]',
        )

        self.id_edit_text = (
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="id"]',
        )

        self.password_edit_text = (
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="pwd"]',
        )

        self.login_confirm_button = (
            AppiumBy.XPATH,
            '//android.widget.Button[@resource-id="loginButton"]',
        )

        self.tab_button = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[1]',
        )

        self.event = (AppiumBy.XPATH, '//android.view.View[@content-desc="Event"]')
        self.draw = (AppiumBy.XPATH, '//android.view.View[@content-desc="Draw"]')

    def close_popup_if_present(self):
        try:
            popup_close_button = self.get_element(self.popup_close_button_locator)
            popup_close_button.click()
        except:
            pass

    def click_team_select_button(self):
        team_select_button = self.get_element(self.team_select_button_locator)
        team_select_button.click()

    def click_schedules_version_button(self, button_text: str):
        button_elements = self.get_elements(self.schedules_version_button)
        for element in button_elements:
            if element.text == button_text:
                element.click()
                break

    def login(self, email: str, password: str):
        self.click(self.user_icon)
        self.enter_text(self.id_edit_text, email)
        self.enter_text(self.password_edit_text, password)
        self.click(self.login_confirm_button)

    def click_draw(self):
        self.click(self.tab_button)
        self.click(self.event)
        self.click(self.draw)
