from base_test import BaseTest
from typing import Tuple, Any
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(BaseTest):
    """The basis for all pages."""

    IMPLICIT_WAIT_TIME = 10
    TIMEOUT = 30

    def __init__(self, driver: Any):
        """
        base constructor.
        Sets driver, implicit wait, and timeout.
        """
        super().__init__()
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.timeout = self.TIMEOUT

    def click(self, by_locator: Tuple[str, str], timeout: int = 10):
        return (
            WebDriverWait(self.driver, timeout)
            .until(EC.visibility_of_element_located(by_locator))
            .click()
        )

    def get_element(self, by_locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

    def send_keys(self, by_locator: Tuple[str, str], text: str):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text)
