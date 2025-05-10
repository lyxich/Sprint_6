import pytest
from selenium import webdriver
from pages.main_page import MainPage

@allure.feature("Логотипы")
class TestLogoNavigation:

    @allure.title("Проверка перехода по логотипу 'Самокат'")
    def test_click_logo_scooter_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_logo_scooter()
        assert "https://qa-scooter.praktikum-services.ru/ " in main_page.get_current_url(), \
            "Не произошёл переход на главную страницу после клика по логотипу 'Самокат'"

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_click_logo_yandex_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_logo_yandex()
        main_page.wait_for_new_window()
        main_page.switch_to_new_window()
        assert "https://dzen.ru " in main_page.get_current_url(), \
            "Не открылась страница Дзен после клика по логотипу Яндекса"