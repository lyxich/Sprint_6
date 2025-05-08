from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators_order_page import LocatorsOrderPage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Методы для заполнения формы
    def fill_order_form(self, name, lastname, address, metro_station, phone):
        self.enter_text(LocatorsOrderPage.NAME_INPUT, name)
        self.enter_text(LocatorsOrderPage.LASTNAME_INPUT, lastname)
        self.enter_text(LocatorsOrderPage.ADDRESS_INPUT, address)
        self.select_metro_station(metro_station)  # Выбираем станцию метро
        self.enter_text(LocatorsOrderPage.PHONE_INPUT, phone)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    # Метод для выбора станции метро
    def select_metro_station(self, station_name):
        self.click_element(self.METRO_STATION_INPUT)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.METRO_STATION_DROPDOWN_ITEM)
        )
        dropdown_items = self.find_elements(self.METRO_STATION_DROPDOWN_ITEM)
        for item in dropdown_items:
            if station_name.lower() in item.text.lower():  # Игнорируем регистр
                item.click()
                return
        raise ValueError(f"Станция метро '{station_name}' не найдена в списке")

    # Метод для проверки успешного сообщения
    def is_success_message_displayed(self):
        return self.is_element_visible(LocatorsOrderPage.SUCCESS_MESSAGE)