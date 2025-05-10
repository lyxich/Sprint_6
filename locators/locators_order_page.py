from selenium.webdriver.common.by import By

class LocatorsOrderPage:
    # Локаторы для формы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.CLASS_NAME, "select-search__input")  # Поле "Станция метро"
    METRO_STATION_DROPDOWN_ITEM = (By.CLASS_NAME, "select-search__row")  # Элементы выпадающего списка
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локатор для сообщения об успешном заказе
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")