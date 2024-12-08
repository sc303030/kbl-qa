from web_Playwright.Pages.base_page import BasePage


class DrawPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.participate = ("button", "참여하기")
        self.confirm = ("button", "확인")

    def select_draw(self, draw_name: str):
        self.select_element_by_text("li", draw_name).get_by_role("paragraph").click()

    def participate_draw(self):
        self.click(self.ROLE, self.participate)
        self.click(self.ROLE, self.confirm)
        self.click(self.ROLE, self.confirm)
