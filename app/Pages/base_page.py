from typing import Tuple, Any
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from typing import Optional
from selenium.webdriver.remote.webelement import WebElement


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

    def swipe_down_w3c(
        self,
        screen_size: dict,
        start_x: float,
        start_y: float,
        end_y: float,
        duration: int = 500,
        origin: Optional[WebElement] = None,
    ):
        width = screen_size["width"]
        height = screen_size["height"]

        start_x = int(width * start_x)
        start_y = int(height * start_y)
        end_y = int(height * end_y)

        actions = ActionBuilder(self.driver, mouse=None)
        finger = actions.add_pointer_input("touch", "finger")

        finger.create_pointer_move(
            duration=0, x=start_x, y=start_y, origin=origin or "viewport"
        )
        finger.create_pointer_down()
        finger.create_pointer_move(
            duration=duration, x=start_x, y=end_y, origin=origin or "viewport"
        )
        finger.create_pointer_up(button=0)

        # 동작 실행
        actions.perform()

    def click_menu(self, locator: Tuple[str, str], menu_name: str):
        elements = self.get_elements(locator)
        for element in elements:
            content_desc = element.get_attribute("content-desc")
            if content_desc == menu_name:
                element.click()
                break
