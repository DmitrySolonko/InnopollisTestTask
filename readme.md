<h1 align="center">Задание </h1>



Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price) 
API с двумя методами:
GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Залить решение на Github, описать запуск в Readme.md

Опубликовать свое решение чтобы его можно было быстро и легко протестировать. Решения доступные только в виде кода на Github получат низкий приоритет при проверке.


<h1 align="center">Запуск </h1>


``` [python]
   git clone https://github.com/DmitrySolonko/InnopollisTestTask 
   python -m venv venv
   venv\Scripts\activate.bat - для Windows;
   source venv/bin/activate - для Linux и MacOS.
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser #необходимо в панеле администратора создать пару объектов
   python manage.py runserver
```

<h1 align="center">Маршрутизация</h1>

<b>/item/№id - просмотр товара </b>

<b>/success - уведомление в случае успешной покупки </b>

<b>/cancel - уведомление в случае неудачи</b>

<h1 align="center">Примечание </h1>

Похоже, что тестовое задание старого образца и документация stripe успела обновиться. Теперь данное задание можно выполнить без использвания кода javascript'а.

