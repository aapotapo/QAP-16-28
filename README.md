Тестовый проект к финальному 28 модулю SkillFactory курса QAP

В директории /tests располагается файл с тестами

В директории /pages лежат объекты [PageObject](https://habr.com/ru/post/472156/)

В корневой директории лежит файл conftest.py с конфигурацией selenuim webdriver для chrome

Для запуска необходимо:

1. Установить зависимости: pip3 install -r requirements

2. Установить [Chromedriver](https://chromedriver.chromium.org/getting-started)

3. Запустить тесты: (python3 или)python -m pytest -v --driver Chrome --driver-path <путь к chromedriver> tests/test_main_page.py

