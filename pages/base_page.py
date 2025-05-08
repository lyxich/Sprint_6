from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод для поиска элемента
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    # Метод для поиска нескольких элементов
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы {locator} не найдены"
        )

    # Метод для клика по элементу
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Метод для ввода текста в поле
    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # Метод для проверки видимости элемента
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False