import allure
from helper import DataGenerationOrder
from scooter_api import MethodsOrder


@allure.suite("Ручка /api/v1/orders/track")
class TestGetOrder:
    @allure.title("Успешное получение заказа по его номеру.")
    @allure.description(" Получаем код 200 и данные с заказом")
    def test_get_order_of_his_number_success(self):
        order_data = DataGenerationOrder.generate_order_data('BLACK')
        create_order = MethodsOrder.create_order(order_data)
        track_number = create_order.json()['track']
        response = MethodsOrder.get_order(track_number)
        assert response.status_code == 200 and response.json()["order"] is not None

    @allure.title("Проверка невозможности получить заказ, если не отправить его номер.")
    @allure.description(" Получаем код 400 и сообщение: Недостаточно данных для поиска")
    def test_get_order_of_his_number_without_number_error(self):
        response = MethodsOrder.get_order('')
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Проверка невозможности получить заказ, если отправить несуществующий номер.")
    @allure.description("Получаем код 404 и сообщение: Заказ не найден")
    def test_get_order_of_his_number_with__non_existent_error(self):
        response = MethodsOrder.get_order('0')
        assert response.status_code == 404 and response.json()["message"] == "Заказ не найден"
