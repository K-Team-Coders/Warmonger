# Warmonger

*Доброго времен суток, всем кто это читает. Вашему вниманию представляется автоматизированная система сбора и обработки информации под названием "**Warmonger" (пер. англ. Милитарист)***

# Требования к эксплуатации

1) PostgreSQL => 10.0
2) Python => 3.8.5
3) Библиотеки из backend/requirements.txt (для работы парсера - также библиотеки из parser/requirements.txt)
4) Широкополосное подключение к ИТКС "Интернет"

# Установка

#### Подключение к БД

создайте файл CREDENTIALS.env в корне проекта, напишите в нем данные для подключения к БД PostgreSQL

`PORT = port `

`USER = user `

`PASSWORD = password `

`HOST = localhost \ ip `

`NAME = name`

Скачайте репозиторий из *GitHub: https://github.com/K-Team-Coders/AfterburnerSQL* или *GitLab: https://git.codenrock.com/skolkovo-hack-2022/cnrprod-team-23883/rostelekom-task/-/tree/lead/*

# Запуск приложения через Docker (в процессе)

Откройте терминал в корне проекта, пропишите команду `docker-compose up -d`

Через некоторое время можно зайти в браузер по адресу *http://localhost:8080/*

# Запуск приложения вручную

#### Backend

Откройте терминал в папке ***backend***, выполните команды:

`python -m venv venv`

`venv\Scripts\activate`

`pip install -r requirements.txt`

Вы создали виртуальное окружение и загрузили необходимые библиотеки, теперь можно запустить backend-часть этого проекта

В папке backend, выполнить

Для создания моделей django в БД:

`python manage.py makemigrations`

`python manage.py migrate`

Для запуска приложения:

`python manage.py runserver`

#### Frontend

Откройте терминал в папке ***frontend***, выполните команды:

`npm install`

`npm run serve`

После этого frontend-часть этого проекта будет доступна либо на http://localhost:8080/, либо на http://localhost:8081/

### Математическая составляющая проекта и как это работает (в процессе)

### Выводы по работе и дальнейшие перспективы

## API

Весь API представлен в файлах **views.py** и **urls.py** Django - приложения.

API к моделям предполагает передачу собранной инфомации от парсера в POST-запросе по адресу:

1) *http://127.0.0.1/main/addNews/*

То есть приложение можно использовать в любых проектах
