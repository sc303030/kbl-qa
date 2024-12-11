from web.Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TicketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ticket_category = (By.XPATH, '//*[@id="root"]/header/div[3]/div/ul/li/a')
        self.price_or_booking = (
            By.XPATH,
            '//*[@id="root"]/main/div/div[1]/div[2]/ul/li[1]/div/div/button',
        )

    def click_ticket_sub_menu(self, menu_txt: str):
        self.click_menu(self.ticket_category, menu_txt)

    def click_price_or_booking(self, type_name: str):
        elements = self.get_elements(self.price_or_booking)
        if type_name == "가격안내":
            elements[0].click()
        else:
            elements[1].click()
