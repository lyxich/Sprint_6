import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-scooter.praktikum-services.ru/")  # Замените на реальный URL
    yield driver
    driver.quit()

@pytest.mark.parametrize("order_data", [
    {
        "name": "Иван",
        "lastname": "Иванов",
        "address": "Москва, Красная площадь",
        "metro_station": "Красные ворота",  # Станция метро
        "phone": "+79991234567"
    },
    {
        "name": "Мария",
        "lastname": "Петрова",
        "address": "Санкт-Петербург, Невский проспект",
        "metro_station": "Площадь Восстания",  # Станция метро
        "phone": "+79997654321"
    }
])
def test_order_flow(driver, order_data):
    main_page = MainPage(driver)
    main_page.click_order_button_top()
    order_page = OrderPage(driver)
    order_page.fill_order_form(
        order_data["name"],
        order_data["lastname"],
        order_data["address"],
        order_data["metro_station"],
        order_data["phone"]
    )
    assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не отображается"