# Learning Log

Learning Log - это веб-приложение, разработанное с использованием Django, которое позволяет пользователям записывать темы, которые они хотят изучить, и делать записи в журнале по мере их изучения.

## Описание приложения

В Learning Log пользователи могут регистрироваться, добавлять темы для изучения и делать записи в журнале для каждой темы. Администраторы имеют доступ к специальному интерфейсу для управления пользователями, темами и записями.

## Требования

- Python 3.x
- Django 3.x

## Установка и запуск

1. Клонируйте репозиторий
    ```sh
    $ git clone https://github.com/Irina-pr98/Learning-log.git
    $ cd learning-log
    ```
    
3. Установите зависимости
   ```sh
   $ pip install -r requirements.txt
   ```
    
4. Выполните миграции базы данных
   ```sh
   $ python manage.py migrate
   ```
   
5. Запустите сервер разработки
   ```sh
   $ python manage.py runserver
   ```
   
6. Откройте приложение в веб-браузере
   ```sh
   http://localhost:8000/
   ```
    
## Структура проекта

- `learning_log/`: основной каталог проекта Django
- `learning_log/settings.py`: настройки проекта
- `learning_log/urls.py`: маршрутизация URL
- `learning_log/wsgi.py`: точка входа для WSGI-совместимых веб-серверов
- `learning_logs/`: приложение для управления записями
- `learning_logs/models.py`: модели данных
- `learning_logs/views.py`: представления
- `learning_logs/urls.py`: маршрутизация URL для приложения
- `learning_logs/templates/`: шаблоны HTML
- `learning_logs/forms.py`: формы для ввода данных
- `learning_logs/admin.py`: регистрация моделей в админке
- `templates/learning_logs/base.html`: базовый шаблон
- `templates/learning_logs/index.html`: домашняя страница
- `templates/learning_logs/topics.html`: страница со списком тем
- `templates/learning_logs/topic.html`: страница с записями по теме
- `templates/learning_logs/new_topic.html`: страница для добавления новой темы
- `templates/learning_logs/new_entry.html`: страница для добавления новой записи
- `templates/learning_logs/edit_entry.html`: страница дляредактирования записи
- `users/`: приложение для управления пользователями
- `users/urls.py`: маршрутизация URL для приложения
- `users/views.py`: представления
- `templates/users/login.html`: страница входа
- `templates/users/logged_out.html`: страница выхода
- `templates/users/register.html`: страница регистрации
- `manage.py`: утилита командной строки для управления проектом
- `requirements.txt`: файл с зависимостями проекта
  
## Управление

- Регистрация пользователя: пользователи могут создавать учетные записи для доступа к приложению.
- Темы: пользователи могут добавлять, просматривать, редактировать и удалять темы.
- Записи в журнале: пользователи могут добавлять, просматривать, редактировать и удалять записи для каждой темы.
- Админ-интерфейс: администраторы могут управлять пользователями, темами и записями через специальный интерфейс.

## Скриншоты

![screenshot_admin](https://github.com/user-attachments/assets/89e73004-d6fd-433f-b1ac-e83d5a469cc1)

![screenshot_topic](https://github.com/user-attachments/assets/96723e91-d3ce-425c-8248-db2597c7034e)

