import requests
import allure
from helper import DataGenerationOrder
from urls import Urls


class MethodsCourier:
    @staticmethod
    @allure.step("Создание нового курьера в системе")
    def create_courier(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        return response

    @staticmethod
    @allure.step("Создание курьера c одинаковыми данными")
    def duplicate_create_courier(payload):
        requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        response_two = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        return response_two

    @staticmethod
    @allure.step("Создание и Логин курьера в системе")
    def create_and_login_courier(payload):
        requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        response = requests.post(Urls.URL_MAIN + Urls.URL_LOGIN_COURIER, data=payload)
        return response

    @staticmethod
    @allure.step("Логин курьера в системе")
    def login_courier(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_LOGIN_COURIER, data=payload)
        return response

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(id_courier):
        response = requests.delete(Urls.URL_MAIN + Urls.URL_CREATE_COURIER + str(id_courier))
        return response


class MethodsOrder:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_ORDER, data=payload)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_list_order():
        response = requests.get(Urls.URL_MAIN + Urls.URL_ORDER)
        return response

    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(id_order, id_courier):
        response = requests.put(Urls.URL_MAIN + Urls.URL_ACCEPT_ORDER + str(id_order) + '?courierId=' +
                                str(id_courier))
        return response

    @staticmethod
    @allure.step("Получить заказ по его номеру")
    def get_order(track_number):
        response = requests.get(Urls.URL_MAIN + Urls.URL_GET_ORDER_BY_NUMBER + '?t=' + str(track_number))
        return response

    @staticmethod
    @allure.step("Принять заказ и получить его id")
    def accept_order_and_take_id():
        order_data = DataGenerationOrder.generate_order_data('BLACK')
        track_number = MethodsOrder.create_order(order_data).json()['track']
        id_order = MethodsOrder.get_order(track_number).json()["order"]['id']
        return id_order
