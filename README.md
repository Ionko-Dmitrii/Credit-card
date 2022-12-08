# Credit card

# Описание проекта

Веб-приложение для управления базой данных бонусных карт (карт лояльности, кредитный карт и т.д)

В приложении используется crontab для проверки каждый час срока активности кард и деактивации их

# Команда генерации новых кард
```
$ python manage.py generate_card -s=Visa -c=2 (-s - Серия, -c - Колличество генерируемых кард)
```

# Как поднять локально проект?

Зависимости:

- PostgreSQL
- Python 3.7
- Django 2.2

## Последовательность действий

```.bash
    $ python3.7 -m venv venv
    $ source venv/bin/activate/
    $ pip install -r requirements.txt
    $ создать файл .env (сделать копию .env-example)
    $ создать файл settings_local.py для переопределения настроек
```

## Переменные окружения для продакшена и локальной разработки:
| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | secret key  | secret-key              |
| `DJANGO_DEBUG`  | Debug mode True or False  | True              |
| `DJANGO_ALLOWED_HOST`| Allowed host | [] |
| `DEFAULT_DATABASE_URL`  | postgres://user:password@host:port/database_name | postgres://db_user:db_password@localhost:5432/db_name |


Необходимо создать в PostgreSQL создать БД:

```.bash
    $ sudo -u postgres psql
    $ create database card_db encoding 'UTF-8';
    $ \q
```

После создания БД, необходимо применить миграцию, после запуск тестового
сервера:

```.bash
    $ python manage.py migrate
    $ python manage.py runserver
    $ python manage.py crontab add 
```

Если все успешно то переходите по ссылке ==> `http://locahost:8000`
