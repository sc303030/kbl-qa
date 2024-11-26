from web.Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logo_locator = (By.CLASS_NAME, "logo")
        self.card_slider_parent_xpath = (
            '//*[@id="root"]/main/div[2]/div[1]/div[1]/div/div[1]/div[1]'
        )
        self.team_select_div_xpath = (
            By.XPATH,
            '//*[@id="root"]/header/div[2]/div/div[2]/div',
        )

    def verify_logo_present(self):
        logo = self.get_element(self.logo_locator)
        return logo is not None

    def get_slide_card_count(self):
        slide_cards = self.driver.find_elements(
            By.XPATH, f"{self.card_slider_parent_xpath}/*"
        )
        return len(slide_cards)

    def hover_team_select_div(self):
        self.hover_on_element(self.team_select_div_xpath)
