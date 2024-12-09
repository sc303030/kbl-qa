from web.Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RecordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.record_category = (By.XPATH, '//*[@id="root"]/header/div[3]/div/ul/li/a')

    def click_record_category(self, category_name: str):
        elements = self.get_elements(self.record_category)
        for element in elements:
            if element.text == category_name:
                element.click()
                break
