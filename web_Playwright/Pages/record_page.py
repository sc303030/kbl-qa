from web_Playwright.Pages.base_page import BasePage


class RecordPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def click_sub_menu(self, role_type: str, sub_menu_name: str):
        self.mouse_move(10, 10)
        self.click(self.ROLE, (role_type, sub_menu_name))
