## Как запустить?

- Перейдя в директорию `/etc/environs` переименуйте файлы `django.env.example` и `postgres.env.example` на `django.env` 
и `postgres.env`
- Заполните .env файлы с данными
- Запустите докер командой:
```bash с
 docker compose up -d --build
```

### Ссылки:

  - Адмиинка: http://127.0.0.1/admin # Админ создайте вручную)
  - Сотрудники: http://127.0.0.1/api/v1/employee/statistics
  - Сотрудник: http://127.0.0.1/api/v1/statistics/employee/<id:uuid>
  - Клиент: http://127.0.0.1/api/v1/statistics/client/<id:uuid>


# Тестовое задание для Backend Разработчиков

## Общее
Азиз имеет свой бизнес и занимается продажей медтехники. Он хочет поощрять своих лучших сотрудников и наблюдать за работой персонала, а также получать статистику по продажам. Сейчас он ведет все данные вручную.

## Задачи
Ваша задача - реализовать REST API на Django Rest Framework, который будет выполнять следующие функции:

- Посчитать статистику отдельного сотрудника.
- Посчитать статистику всех сотрудников.
- Посчитать статистику отдельного клиента.

Статистика сотрудника должна включать:
1. Количество проданных товаров.
2. Количество уникальных клиентов.
3. Общая сумма продаж.

Статистика клиента должна включать:
1. Количество купленных товаров.
2. Общая сумма продаж.

Требования:
- Django Rest Framework (DRF).
- Docker.
- База данных на ваш выбор (рекомендуется использовать PostgreSQL).

## Техническое задание
### Endpoint'ы:
1. `GET /statistics/employee/{id}/?month=1&year=2023` - возвращает статистику по отдельному сотруднику за указанный месяц и год. Включает ФИО сотрудника, количество клиентов, количество товаров и общую сумму продаж.
2. `GET /employee/statistics/?month=1&year=2023` - возвращает статистику всех сотрудников за указанный месяц и год. Включает id сотрудника, ФИО, количество клиентов, количество товаров и общую сумму продаж.
3. `GET /statistics/client/{id}?month=1&year=2023` - возвращает статистику по отдельному клиенту за указанный месяц и год. Включает id клиента, ФИО, количество купленных товаров и общую сумму продаж.

### Сущности:
- **Employee** (сотрудник): 
  - full_name (ФИО).
  - birthdate (дата рождения).
- **Client** (клиент): 
  - full_name (ФИО).
  - birthdate (дата рождения).
- **Product** (продукт): 
  - name (имя продукта).
  - quantity (количество в наличии).
  - price (цена).
- **Order** (заказ): 
  - client (клиент).
  - products (продукты, может быть несколько).
  - employee (сотрудник).
  - price (общая цена заказа).
  - date (дата заказа).

## Замечания
- Для запуска проекта можно использовать Docker-compose.
- Проект должен содержать файл `README.md`, описывающий, как запустить и использовать API.