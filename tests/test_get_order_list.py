import allure
from scooter_api import MethodsOrder


@allure.suite("Ручка /api/v1/orders")
class TestGetListOfOrder:

    @allure.title("Проверка получения списка заказов.")
    @allure.description(' Получаем код 200 и список (не пустой)')
    def test_get_list_of_order(self):
        orders = MethodsOrder.get_list_order()
        assert orders.status_code == 200 and orders.json()["orders"] != []
