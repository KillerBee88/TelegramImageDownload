# Telegram Image Download Bot

# Бот для загрузки изображений космоса в телеграмм канал

## Инструкция по запуску и установке:

1. Для начала нужно скачать репозиторий.

2. Далее установить зависимости:

```shell
pip install -r requirements.txt
```
## Настройка

1. Создать '.env' файл в корне проекта.

2. Добавить в него следующие переменные:

```shell
TG_BOT_API='API ключ Telegram бота'
NASA_API_KEY='API ключ от NASA'
```

## Скрипты 

1. fetch_nasa_apod_images.py

Скрипт скачивает изображения с сервиса NASA APOD (Astronomy Picture of the Day). Для использования скрипта вам понадобится ключ API NASA.

Пример использования:

```shell
python fetch_nasa_apod_images.py --count 5
```

Аргумент --count опционален и обозначает количество изображений, которые будут скачаны. По умолчанию равен 10.

2. fetch_nasa_epic_images.py

Скрипт скачивает изображения с сервиса NASA EPIC (Earth Polychromatic Imaging Camera). Для использования скрипта вам понадобится ключ API NASA.

Пример использования:

```shell
python fetch_nasa_epic_images.py --days 3
```

Аргумент --days опционален и обозначает количество прошедших дней, за которые будут скачаны изображения. По умолчанию равен 10.

3. fetch_spacex_last_launch.py

Скрипт скачивает изображения с последнего запуска SpaceX.

Пример использования:

```shell
python fetch_spacex_last_launch.py --id 132
```

Аргумент --id опционален и обозначает ID запуска, для которого будут скачаны изображения. Если не указан, будут скачаны изображения с последнего запуска.

4. publish_photos.py

Скрипт публикует все изображения из указанной директории в указанный канал Telegram через указанные промежутки времени.

Пример использования:

```shell
python publish_photos.py images --hours 2
```

Первый аргумент — обязательный, это путь до директории с изображениями. Аргумент --hours опционален и обозначает количество часов между публикациями. По умолчанию равен 4.

5. bot.py

Скрипт Telegram бота, который скачивает изображения с различных космических сервисов и публикует их в указанный Telegram канал.

Пример использования:

```shell
python bot.py
```

## Примечания:

Сначала запустите скрипты для скачивания изображений (fetch_nasa_apod_images.py, fetch_nasa_epic_images.py, fetch_spacex_last_launch.py), затем publish_photos.py для автоматической публикации изображений в канале.
