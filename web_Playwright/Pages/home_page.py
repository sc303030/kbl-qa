from web_Playwright.Pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_button = '//*[@id="root"]/header/div[2]/div/div[3]/button[2]'
        self.id_input = '//*[@id="id"]'
        self.password_input = '//*[@id="pwd"]'
        self.login_confirm_button = '//*[@id="loginButton"]'

    def login(self, email: str, password: str):
        self.click(self.login_button)
        self.input_text(self.id_input, email)
        self.input_text(self.password_input, password)
        self.click(self.login_confirm_button)
