# Yatube api Final
Проект мини-соцсети разрбаботчиков для работы через API

Позволяет быстро развернуть и настроить Backend со следующим функционалом:

* Публикация и просмотр постов
* Публикация и просмотр комментариев к постам
* Наличие авторизации через JWT-токены
* Поиск, сортировка и пангинация результатов

### Установка и запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git](https://github.com/Andrey-Kolchugin/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Теперь можно открыть API в вашем браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/), и увидеть ваше API `'api'`.

Вы можете взаимодействовать с API с помощью инструментов командной строки, оконных менеджеров (например, Postman). 

### Пример

Получение всего списка постов методом GET http://127.0.0.1:8000/api/v1/posts/ выдаст результат:

```
[
    {
        "id": 1,
        "author": "user2",
        "text": "text1",
        "pub_date": "2022-07-20T06:19:25.850002Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "user2",
        "text": "textttt",
        "pub_date": "2022-07-20T06:19:35.907378Z",
        "image": null,
        "group": null
    },
]
```
