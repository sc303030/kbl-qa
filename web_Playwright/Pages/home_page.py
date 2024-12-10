from web_Playwright.Pages.base_page import BasePage
from playwright.sync_api import expect


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_button = ("button", "로그인")
        self.id_input = "통합 아이디(이메일)"
        self.password_input = "비밀번호"
        self.login_confirm_button = '//*[@id="loginButton"]'
        self.draw_button = ("link", "Draw")

    def login(self, email: str, password: str):
        self.click(self.ROLE, self.login_button)
        self.input_text(self.PLACEHOLDER, self.id_input, email)
        self.input_text(self.PLACEHOLDER, self.password_input, password)
        self.click(self.XPATH, self.login_confirm_button)

    def click_menu(self, role_type: str, menu_name: str):
        self.click(self.ROLE, (role_type, menu_name))

    def click_draw(self):
        self.click(self.ROLE, self.draw_button)
