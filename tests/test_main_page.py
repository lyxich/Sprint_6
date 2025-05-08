import pytest
from selenium import webdriver
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

def test_logo_navigation(driver):
    main_page = MainPage(driver)

    # Переход по логотипу "Самокат"
    main_page.click_logo_scooter()
    assert "https://qa-scooter.praktikum-services.ru/" in driver.current_url, "Переход по логотипу 'Самокат' не выполнен"

    # Переход по логотипу Яндекса
    main_page.click_logo_yandex()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])  # Переключаемся на новое окно
    assert "https://dzen.ru" in driver.current_url, "Переход по логотипу Яндекса не выполнен"