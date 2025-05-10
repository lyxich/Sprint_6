from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод для поиска элемента
    @allure.step('Ищем элемент')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    # Метод для поиска нескольких элементов
    @allure.step('Ищем несколько элементов')
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы {locator} не найдены"
        )

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # Метод для клика по элементу
    @allure.step('Кликаем по элементу')
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Метод для ввода текста в поле
    @allure.step('Вводим текст в поле')
    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # Метод для проверки видимости элемента
    @allure.step('Проверяем видимость элемента')
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step('Проверяем урл')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Новое окно')
    def switch_to_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])