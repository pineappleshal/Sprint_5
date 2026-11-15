# Sprint_5

UI-автотесты для учебного сервиса объявлений «Доска»
(https://qa-desk.stand.praktikum-services.ru/). Стек: Python, pytest, Selenium, Google Chrome.

## Что покрыто

| Модуль | Класс | Проверки |
|---|---|---|
| `tests/test_registration.py` | `TestRegistration` | успешная регистрация; email не по маске; уже существующий пользователь |
| `tests/test_login.py` | `TestLogin` | вход под существующим пользователем |
| `tests/test_logout.py` | `TestLogout` | выход из аккаунта |
| `tests/test_ad_creation.py` | `TestAdCreation` | объявление без авторизации; создание объявления авторизованным пользователем |

## Структура проекта

- `tests/` — тесты, по одному модулю на функциональность
- `conftest.py` — фикстуры: `driver`, `wait`, `authorized_driver`
- `locators.py` — локаторы элементов
- `data.py` — адрес стенда, тестовые данные и ожидаемые значения
- `helpers.py` — генерация уникального email для регистрации
- `requirements.txt` — зависимости

## Запуск

```
pip install -r requirements.txt
pytest tests -v
```

Нужен установленный Google Chrome; драйвер Selenium подбирает сам.
Логин, логаут и создание объявления выполняются под заранее созданным
пользователем из `data.py`.
