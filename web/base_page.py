class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text
