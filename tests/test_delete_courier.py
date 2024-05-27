import allure
from helper import GenerateRandomCourier
from scooter_api import MethodsCourier


@allure.suite("Ручка /api/v1/orders")
class TestDeleteCourier:
    @allure.description("Успешное уделение курьера. Получаем код 200 и сообщение 'ок':true")
    def test_delete_courier_success(self):
        user_data = GenerateRandomCourier.generate_random_courier_data()
        login_courier = MethodsCourier.create_and_login_courier(user_data)
        id_courier = login_courier.json()['id']
        response = MethodsCourier.delete_courier(id_courier)
        assert response.status_code == 200 and response.json() == {'ok': True}

    @allure.description("Попытка уделения курьера без указания id. Получаем код 400")
    def test_delete_courier_without_id(self):
        id_courier = ""
        response = MethodsCourier.delete_courier(id_courier)
        assert response.status_code == 404

    @allure.description("Попытка уделения курьера c указанием несуществующего id. Получаем код 404")
    def test_delete_courier_with_non_existent_id(self):
        id_courier = "0"
        response = MethodsCourier.delete_courier(id_courier)
        assert response.status_code == 404 and response.json()["message"] == "Курьера с таким id нет."
