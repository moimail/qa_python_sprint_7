import allure
import pytest
from helper import DataGenerationOrder
from scooter_api import MethodsOrder


@allure.title("Ручка /api/v1/orders")
class TestOrders:
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    @allure.description('Проверка, что можно создать заказ с указанием любого цвета')
    def test_create_order_with_color(self, color):
        order_data = DataGenerationOrder.generate_order_data(color)
        response = MethodsOrder.create_order(order_data)
        assert response.status_code == 201 and response.json()['track'] != 0
