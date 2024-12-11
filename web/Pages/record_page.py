from web.Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RecordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.record_category = (By.XPATH, '//*[@id="root"]/header/div[3]/div/ul/li/a')

    def click_record_category(self, menu_txt: str):
        self.click_menu(self.record_category, menu_txt)
