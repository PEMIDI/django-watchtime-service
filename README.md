

**Django Watch Time Service 🎥📺**
================

**Overview 📚👀**
------------

The Service is a Django-based service that tracks and manages events, including user watch times and movie metadata 🎬. The project provides a RESTful API for retrieving and manipulating event data 💻.

**Motivation 💡💻**
-------------

The Events API was designed to provide a scalable and efficient solution for tracking user watch times and movie metadata 📊. By using Django and its built-in ORM, we can leverage the power of Python and the simplicity of Django's ORM to build a robust and maintainable API 💪.

**Technical Choices 🤔💭**
--------------------

### Django 🐍💻

Django was chosen as the framework for this project due to its robustness, scalability, and ease of use 😊. Django provides a built-in ORM, authentication and authorization systems, and a flexible project structure that makes it ideal for building complex web applications 🌐.

### RESTful API 📱📲

A RESTful API was chosen to provide a flexible and scalable interface for interacting with the Events API 📊. By using REST, we can decouple the API from the underlying implementation and provide a simple, intuitive interface for clients to interact with 📈.

### RabbitMQ 🐰💨

RabbitMQ was chosen as the message broker for this project due to its reliability, scalability, and ease of use 💯. RabbitMQ provides a robust and fault-tolerant message queue that allows us to decouple the API from the underlying database and provide a scalable solution for handling high volumes of traffic 🚀.

**Project Structure 🗂️📁**
---------------------

The project is structured as follows:

* `events`: The main Django app for the project 📊
* `events/serializers`: Django serializers for the API 📝
* `events/models`: Django models for the database 📚
* `events/views`: Django views for the API 📊
* `events/urls`: Django URL configurations for the API 📈
* `rabbitmq`: The RabbitMQ client for publishing and consuming messages 🐰

**How to Run the Project 🚀💻**
-------------------------

### Prerequisites 📝👀

* Python 3.8+ 🐍
* Django 3.2+ 📊
* RabbitMQ 3.8+ 🐰

### Installation 💻🔧

1. Clone the repository: `git clone https://github.com/PEMIDI/django-watchtime-service.git` 📂
2. Install the dependencies: `pip install -r requirements.txt` 📦
3. Create the database: `python manage.py migrate` 📈
4. Start the RabbitMQ server: `rabbitmq-server` 🐰
5. Start the Django server: `python manage.py runserver` 🚀
6. Start RabbitMQ consumer: `python manage.py consume_rabbitmq`



**API Endpoints 📊📈**
-----------------

### Event API

* `GET /`: Retrieve the list of events 📊
* `GET /users/<str:username>/total-watch-time/`: Retrieve the total watch time of a user 👨‍💻
* `GET /movies/<int:pk>/total-watch-time/`: Retrieve the total watch time of a movie 🎥
* `GET /<str:username>/<int:movie_pk>/total-watch-time/`: Retrieve the total watch time of a movie for a specific user 👨‍💻

### Serializers 📝💻

* `EventSerializer`: Validates incoming data for the Event API 📊
* `UserTotalWatchTimeSerializer`: Serializer for CustomUser model to retrieve total watch time 👨‍💻
* `MovieTotalWatchTimeSerializer`: Serializer for Movie model to retrieve total watch time 🎥
* `UserMovieTotalWatchTimeSerializer`: Serializer for WatchTime model to retrieve total watch time for a user and movie 👨‍💻



**Models 📚👀**
-------------

### CustomUser 👨‍💻

Custom user model.

**Attributes:**

* `username` (str): Username of the user 👨‍💻
* `total_watch_time` (int): Total watch time of the user in seconds ⏱️

### Movie 🎥

Movie model.

**Attributes:**

* `title` (str): Title of the movie 🎥
* `slug` (str): Slug of the movie 📊
* `total_watch_time` (int): Total watch time of the movie in seconds ⏱️

### WatchTime ⏱️

Watch time model.

**Attributes:**

* `user` (CustomUser): The user who watched the movie 👨‍💻
* `movie` (Movie): The movie that was watched 🎥
* `last_moment` (int): The last moment the user watched the movie ⏱️
* `total` (int): The total watch time for the movie ⏱️

**RabbitMQ Client 🐰💻**
---------------------

The RabbitMQ client is used for publishing and consuming messages to/from RabbitMQ.

**Methods:**

* `publish(message)`: Publish a message to the RabbitMQ queue 📣
* `consume()`: Consume messages from the RabbitMQ queue 📊
* `consume_and_save()`: Consume messages from the RabbitMQ queue and save watch times to the database 💻
* `close()`: Close the connection to RabbitMQ 👋

