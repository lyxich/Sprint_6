from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Методы для взаимодействия с элементами
    @allure.step('Нажимаем верхнюю кнопку Заказать')
    def click_order_button_top(self):
        self.click_element(LocatorsMainPage.ORDER_BUTTON_TOP)

    @allure.step('Нажимаем нижнюю кнопку Заказать')
    def click_order_button_bottom(self):
        self.click_element(LocatorsMainPage.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажимаем на слово Самокат')
    def click_logo_scooter(self):
        self.click_element(LocatorsMainPage.LOGO_SCOOTER)

    @allure.step('Нажимаем на слово Яндекс')
    def click_logo_yandex(self):
        self.click_element(self.LOGO_YANDEX)

    @allure.step('Нажимаем на вопрос о важном')
    def click_faq_question(self, index):
        questions = self.find_elements(self.FAQ_QUESTION)
        self.click_on_element(questions[index])

    @allure.step('Получаем текст ответа')
    def get_faq_answer(self, index):
        answers = self.find_elements(LocatorsMainPage.FAQ_ANSWER)
        return answers[index].text

    @allure.step('Закрываем куки баннер')
    def close_cookie_banner(self):
        try:
            cookie_banner = self.driver.find_element(LocatorsMainPage.COOKIE_BANNER)
            close_button = cookie_banner.find_element(LocatorsMainPage.CLOSE_BUTTON)
            close_button.click()
        except:
            pass  # Если баннера нет, ничего не делаем