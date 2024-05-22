import allure
import pytest
from helper import GenerateRandomCourier
from scooter_api import MethodsCourier


@allure.title("Ручка /api/v1/courier/login")
class TestLoginCourier:
    @allure.description("Проверка успешного логина курьера. Получаем статус 200 и id курьера")
    def test_login_courier_success(self, create_and_delete_account_courier):
        login_courier = MethodsCourier.create_and_login_courier(create_and_delete_account_courier)
        assert login_courier.status_code == 200 and login_courier.json()['id'] != 0

    @allure.title('Проверка, что если не передано поле логина или пароля, запрос возвращает ошибку 400')
    @pytest.mark.parametrize('field_key, field_value', [('login', ''), ('password', '')])
    def test_login_courier_empty_field_error(self, field_key, field_value):
        user_data = GenerateRandomCourier.generate_random_courier_data()
        payload = user_data.copy()
        payload[field_key] = field_value
        response = MethodsCourier.create_and_login_courier(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.description('Проверка невозможности залогиниться с несуществующим аккаунтом. Получаем ошибку 404')
    def test_no_such_login(self):
        user_data = GenerateRandomCourier.generate_random_courier_data()
        response = MethodsCourier.login_courier(user_data)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'
