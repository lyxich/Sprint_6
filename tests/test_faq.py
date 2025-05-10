import pytest
from selenium import webdriver
from pages.main_page import MainPage

@allure.feature("FAQ")
class TestFAQ:

    @allure.title("FAQ: Проверка ответа на вопрос №{question_index}")
    @pytest.mark.parametrize("question_index, expected_answer", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат."),
        (2, "Допустим, вы оформляете заказ на 8 мая."),
        (3, "Только начиная с завтрашнего дня."),
        (4, "Пока что нет! Но если что-то срочное"),
        (5, "Самокат приезжает к вам с полной зарядкой."),
        (6, "Да, пока самокат не привезли."),
        (7, "Да, обязательно. Всем самокатов!")
    ])
    def test_faq(driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()  # Закрываем баннер, если он есть
        main_page.click_faq_question(question_index)
        answer = main_page.get_faq_answer(question_index)
        assert expected_answer in answer, f"Ответ на вопрос {question_index} не совпадает"