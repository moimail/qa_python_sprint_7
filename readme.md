# qa_python_sprint_7"

Проект автоматизации тестирования api сайта заказа самокатов https://qa-scooter.praktikum-services.ru/

Основа для написания автотестов — фреймворк pytest, selenium, модуль hhtp
Для отчетов используется Allure
Автотесты написаны в соответствии с паттерном проектирования POM
Установить зависимости — pip install -r requirements.txt
Команда для запуска — pytest -v
Команда для запуска с записью отчета в allure_results: pytest --alluredir=allure_results
Генерация отчета в html страницу (находясь в дирректории allure_results): allure serve allure_results
Директория проекта:
allure_results - папка сожержит отчеты alure
tests - папка тестов
test_accept_order.py - тесты "Принять заказ"
test_create_courier.py - тесты "Создание курьера"
test_create_order.py - тесты "Создание заказа"
test_delete_courier.py - тесты "Удаление заказа"
test_get_order_list.py - тест "Получение списка заказов"
test_get_order_of_his_number.py - тест "Получить заказ по его номеру"
test_login_courier.py - тесты "Логин курьера в системе"
conftest.py - фикстуры
helpers - файл с вспомогательными функциями
README.md - описание проекта
requirements - файл с необходимыми библиотеками
scooter_api.py - файл с методами, вызываемыми в ходе тестов
urls.py - файл c URL