import allure
from scooter_api import MethodsOrder


@allure.title("Ручка /api/v1/orders")
class TestGetListOfOrder:

    @allure.description('Проверка получения списка заказов. Получаем код 200 и список (не пустой)')
    def test_get_list_of_order(self):
        orders = MethodsOrder.get_list_order()
        assert orders.status_code == 200 and orders.json()["orders"] != []
