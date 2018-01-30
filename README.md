<h2>Read me</h2>
Виртуальное оркужение, в котором я разрабатывал приложение, находтся в папке "my_env". Для вхождения в окружение используйте команду
<strong><p>source bin/activate</p></strong>
Зависимости записаны в файле "requirements.txt".
<br>
<h3> Запуск сервера </h3>
Для запуска встроенного сервера необходимо зайти в папку приложения "Image" и использовать команду 
<strong><p>python3 manage.py runserver</p></strong>
<h3>Проблемы с БД и миграциями</h3>
В случае возникновения ошибок, связанных с БД, необходимо произвести миграции.
<strong><p>python3 manage.py makemigrations</p></strong>
<strong><p>python3 manage.py migrate</p></strong>

