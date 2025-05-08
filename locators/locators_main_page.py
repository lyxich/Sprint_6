from selenium.webdriver.common.by import By

class LocatorsMainPage:
    # Локаторы для кнопок "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать'][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[text()='Заказать'][2]")

    # Локаторы для логотипов
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Локаторы для раздела "Вопросы о важном"
    FAQ_QUESTION = (By.CLASS_NAME, "accordion__button")
    FAQ_ANSWER = (By.CLASS_NAME, "accordion__panel")