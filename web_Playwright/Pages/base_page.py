from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def get_element(self, xpath: str):
        self.page.wait_for_selector(f"xpath={xpath}")
        return self.page.locator(f"xpath={xpath}")

    def click(self, xpath: str):
        element = self.get_element(xpath)
        element.click()

    def input_text(self, xpath: str, text: str):
        element = self.get_element(xpath)
        element.fill(text)

    def check_text(self, xpath: str, expected_text: str):
        element = self.get_element(xpath)
        expect(element).to_have_text(expected_text)
