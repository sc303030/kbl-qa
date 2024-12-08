from playwright.sync_api import Page, expect
from typing import Union, Tuple, Callable


class BasePage:
    XPATH = "xpath"
    ROLE = "role"
    PLACEHOLDER = "placeholder"

    def __init__(self, page: Page):
        self.page = page
        self.method_map = {
            self.XPATH: self.get_element_by_xpath,
            self.ROLE: self.get_element_by_role,
            self.PLACEHOLDER: self.get_element_by_placeholder,
        }

    def goto(self, url: str):
        self.page.goto(url)

    def get_element(self, method: str, element_name: Union[str, Tuple[str, str]]):
        if method not in self.method_map:
            raise ValueError(f"Unsupported method: {method}")
        handler: Callable = self.method_map[method]
        return (
            handler(*element_name)
            if isinstance(element_name, tuple)
            else handler(element_name)
        )

    def get_element_by_role(self, role: str, name: str):
        return self.page.get_by_role(role, name=name)

    def get_element_by_placeholder(self, name: str):
        return self.page.get_by_placeholder(name)

    def get_element_by_xpath(self, xpath: str):
        self.page.wait_for_selector(f"xpath={xpath}")
        return self.page.locator(f"xpath={xpath}")

    def click(self, method: str, element_name: Union[str, Tuple[str, str]]):
        element = self.get_element(method, element_name)
        element.click()

    def hover(self, method: str, element_name: Union[str, Tuple[str, str]]):
        element = self.get_element(method, element_name)
        element.hover()

    def input_text(self, method: str, element_name: str, text: str):
        element = self.get_element(method, element_name)
        element.fill(text)

    def check_text(self, method: str, xpath: str, expected_text: str):
        element = self.get_element(method, xpath)
        expect(element).to_have_text(expected_text)

    def select_element_by_text(self, tag: str, text: str):
        return self.page.locator(tag).filter(has_text=text)
