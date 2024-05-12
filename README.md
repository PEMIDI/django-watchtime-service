

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

```swagger codegen
{
  "swagger": "2.0",
  "info": {
    "title": "Snippets API",
    "description": "Test description",
    "termsOfService": "https://www.google.com/policies/terms/",
    "contact": {
      "email": "contact@snippets.local"
    },
    "license": {
      "name": "BSD License"
    },
    "version": "v1"
  },
  "host": "127.0.0.1:8000",
  "schemes": [
    "http"
  ],
  "basePath": "/",
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "securityDefinitions": {
    "Basic": {
      "type": "basic"
    }
  },
  "security": [
    {
      "Basic": []
    }
  ],
  "paths": {
    "/": {
      "post": {
        "operationId": "_create",
        "summary": "📣 Event API: Receive data and publish to RabbitMQ",
        "description": "This API endpoint receives data from the request and publishes it to RabbitMQ.\n\n**HTTP Method:** POST\n**Request Body:** JSON data\n**Response:** \"ok\" with HTTP 200 OK status",
        "parameters": [],
        "responses": {
          "201": {
            "description": ""
          }
        },
        "tags": [
          ""
        ]
      },
      "parameters": []
    },
    "/movies/{id}/total-watch-time/": {
      "get": {
        "operationId": "movies_total-watch-time_read",
        "summary": "🎥 Movie Total Watch Time API: Retrieve total watch time for a movie",
        "description": "This API endpoint retrieves the total watch time for a movie.\n\n**HTTP Method:** GET\n**Path Parameter:** `pk` (integer)\n**Response:** JSON data with total watch time",
        "parameters": [],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/MovieTotalWatchTime"
            }
          }
        },
        "tags": [
          "movies"
        ]
      },
      "parameters": [
        {
          "name": "id",
          "in": "path",
          "description": "A unique integer value identifying this movie.",
          "required": true,
          "type": "integer"
        }
      ]
    },
    "/users/{username}/total-watch-time/": {
      "get": {
        "operationId": "users_total-watch-time_read",
        "summary": "🕒️ User Total Watch Time API: Retrieve total watch time for a user",
        "description": "This API endpoint retrieves the total watch time for a user.\n\n**HTTP Method:** GET\n**Path Parameter:** `username` (string)\n**Response:** JSON data with total watch time",
        "parameters": [],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/UserTotalWatchTime"
            }
          }
        },
        "tags": [
          "users"
        ]
      },
      "parameters": [
        {
          "name": "username",
          "in": "path",
          "description": "Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.",
          "required": true,
          "type": "string"
        }
      ]
    },
    "/{username}/{movie_pk}/total-watch-time/": {
      "get": {
        "operationId": "total-watch-time_read",
        "summary": "👥 User Movie Watch Time API: Retrieve watch time for a user and movie",
        "description": "This API endpoint retrieves the watch time for a user and a movie.\n\n**HTTP Method:** GET\n**Path Parameters:** `username` (string), `pk` (integer)\n**Response:** JSON data with watch time",
        "parameters": [],
        "responses": {
          "200": {
            "description": "",
            "schema": {
              "$ref": "#/definitions/UserMovieTotalWatchTime"
            }
          }
        },
        "tags": [
          "total-watch-time"
        ]
      },
      "parameters": [
        {
          "name": "username",
          "in": "path",
          "required": true,
          "type": "string"
        },
        {
          "name": "movie_pk",
          "in": "path",
          "required": true,
          "type": "string"
        }
      ]
    }
  },
  "definitions": {
    "MovieTotalWatchTime": {
      "required": [
        "slug"
      ],
      "type": "object",
      "properties": {
        "title": {
          "title": "Title",
          "description": "Optional. 100 characters or fewer.",
          "type": "string",
          "maxLength": 100,
          "x-nullable": true
        },
        "slug": {
          "title": "Slug",
          "description": "Required. Unique slug for the movie.",
          "type": "string",
          "format": "slug",
          "pattern": "^[-a-zA-Z0-9_]+$",
          "maxLength": 50,
          "minLength": 1
        },
        "total_watch_time": {
          "title": "Total watch time",
          "type": "string",
          "readOnly": true
        }
      }
    },
    "UserTotalWatchTime": {
      "required": [
        "username"
      ],
      "type": "object",
      "properties": {
        "username": {
          "title": "Username",
          "description": "Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.",
          "type": "string",
          "maxLength": 100,
          "minLength": 1
        },
        "total_watch_time": {
          "title": "Total watch time",
          "type": "string",
          "readOnly": true
        }
      }
    },
    "UserMovieTotalWatchTime": {
      "type": "object",
      "properties": {
        "get_total_watch_time_per_user_movie": {
          "title": "Get total watch time per user movie",
          "type": "string",
          "readOnly": true
        }
      }
    }
  }
}
```


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

