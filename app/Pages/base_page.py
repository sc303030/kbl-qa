from typing import Tuple, Any
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: Any):
        self.driver = driver

    def click(self, locator: Tuple[str, str], timeout: int = 10):
        return (
            WebDriverWait(self.driver, timeout)
            .until(EC.visibility_of_element_located(locator))
            .click()
        )

    def get_element(self, locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def enter_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)
