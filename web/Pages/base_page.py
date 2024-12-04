from typing import Tuple

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def get_element(self, locator: Tuple[str, str], timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator: Tuple[str, str], timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click(self, locator):
        return self.get_element(locator).click()

    def enter_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def hover_on_element(self, locator):
        element = self.get_element(locator)
        self.action.move_to_element(element).perform()
