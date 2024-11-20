from web.Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logo_locator = (By.CLASS_NAME, "logo")
        self.card_slider_parent_xpath = (
            '//*[@id="root"]/main/div[2]/div[1]/div[1]/div/div[1]/div[1]'
        )

    def verify_logo_present(self):
        logo = self.get_element(self.logo_locator)
        return logo is not None

    def get_slide_card_count(self):
        slide_cards = self.driver.find_elements(
            By.XPATH, f"{self.card_slider_parent_xpath}/*"
        )
        return len(slide_cards)
