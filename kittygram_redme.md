# Установка и настройка проекта Kittygram.

***
*Этот репозиторий содержит инструкции по установке и настройке проекта Kittygram на удаленном сервере. Проект Kittygram является мессенджером для обмена фотографиями котиков.*

***

## Техническое описание проекта деплоя Kittygram. ##

### Шаг 1: Получение доменного имени ###

Для доступа к приложению вам понадобится доменное имя. Вы можете использовать любой сервис, выдающий доменные имена, чтобы получить его. Пожалуйста, укажите полную ссылку (https://доменное_имя) на ваш проект Kittygram.

### Шаг 2: Клонирование репозитория ###

Клонируйте репозиторий **infra_sprint1** с проектом Kittygram с вашего аккаунта на GitHub на удаленный сервер. Используйте следующую команду:
```angular2html
git clone <ссылка_на_репозиторий>
```
### Шаг 3: Установка зависимостей ###

На удаленном сервере установим следующие зависимости:

    venv: Виртуальная среда для изоляции проекта.
    pip: Установщик пакетов Python.

Выполните следующие команды для установки зависимостей:
```angular2html
sudo apt update
sudo apt install python3-venv python3-pip
```

### Шаг 4: Создание виртуальной среды ### 

Создайте виртуальную среду для проекта Kittygram, используя следующую команду:

```angular2html
python3 -m venv venv
```

### Шаг 5: Активация виртуальной среды ###

```python
source env/bin/activate
```
### Шаг 6: Установка зависимостей проекта ###

```python
pip install -r requirements.txt
```

### Шаг 7: Настройка Gunicorn ###

Создаём файл конфигураций с условиями:

* *запуска WSGI сервера*
* *имя пользователя (от кого запуск)*
* *путь к директории бэкенда*
* *команду запуска WSGI*

Запуск и установку и просмотр статуса осуществляем с помощью утилиты **systemctl**

```python
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```
Добавление процесса в список автозапуска ОС на сервере:

```python
sudo system enable gunicorn
```

### Шаг 8: Настройка Nginx ### 

Установим NGINX 

```python
sudo apt install nginx -y
```
Запускаем его:

```python
sudo systemctl start nginx
```

* **Собираем статику фронтенда и копируем её в системную директорию проекта**

```markdown
npm run build
sudo cp -r ~/yc-user/infra_sprint1/frontend/build /var/www/kittygram/
```
