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

        self.menus = (
            By.XPATH,
            '//*[@id="root"]/header/div[2]/div/div[2]/nav/ul/li/a',
        )

        self.login_button = (
            By.XPATH,
            '//*[@id="root"]/header/div[2]/div/div[3]/button[2]',
        )

        self.id_input = (By.XPATH, '//*[@id="id"]')
        self.password_input = (By.XPATH, '//*[@id="pwd"]')

        self.login_confirm_button = (By.XPATH, '//*[@id="loginButton"]')

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

    def get_text_and_memu_click(self, menu_txt: str):
        elements = self.get_elements(self.menus)
        for element in elements:
            if element.text == menu_txt:
                element.click()
                break

    def login(self, email: str, password: str):
        self.click(self.login_button)
        self.enter_text(self.id_input, email)
        self.enter_text(self.password_input, password)
        self.click(self.login_confirm_button)

    def hover_after_mouse_move(self, x: int, y: int):
        self.mouse_move(x, y)
