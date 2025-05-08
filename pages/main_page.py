from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Методы для взаимодействия с элементами
    def click_order_button_top(self):
        self.click_element(LocatorsMainPage.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(LocatorsMainPage.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click_element(LocatorsMainPage.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_element(self.LOGO_YANDEX)

    def click_faq_question(self, index):
        questions = self.find_elements(self.FAQ_QUESTION)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(questions[index])
        )
        questions[index].click()

    def get_faq_answer(self, index):
        answers = self.find_elements(LocatorsMainPage.FAQ_ANSWER)
        return answers[index].text

    def close_cookie_banner(self):
        try:
            cookie_banner = self.driver.find_element(By.CLASS_NAME, "cookie-banner")
            close_button = cookie_banner.find_element(By.CLASS_NAME, "close-button")
            close_button.click()
        except:
            pass  # Если баннера нет, ничего не делаем