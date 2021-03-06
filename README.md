# BUILD A PRODUCT: MOVIEWORLD API
## Introduction
* An API for movies crud management.

## Technologies used.
* **[Python](https://www.python.org/downloads/)**
* **[Django](https://www.django-rest-framework.org/)**
* **[Django Rest Framework](https://www.django-rest-framework.org/)** 
* **[Docker](https://www.docker.com/)**


## Installation Using Virtual Environment

 #### **Download the repo.**
 ```
    $ git clone https://github.com/kiburualex/MovieWorld
```
 #### **Create virtual environment & Activate.**
 ```
    $ virtualenv -p python3 venv 
    $ source venv/bin/activate
```
 #### **Install Dependancies.**
 ```
    (myenv)$ pip install -r requirements.txt
```
  #### **Make migrations**
```
    (myenv)$ python manage.py makemigrations
    (myenv)$ python manage.py migrate
```
#### **Run the app**
   ```
    (myenv)$ python manage.py runserver
```
#### **Run Tests**
  ```
  (myenv)$ python manage.py test
```


## Installation Using Docker

 #### **Unzip the downloaded folder.**
   ```
    $ unzip movieworld.zip
  ```
 #### **Run docker (Ensure docker is installed locally).**
 ```
    $ docker-compose up
```
#### **Run Tests**
  ```
  $ docker-compose run web python manage.py test
```
  ## Installation Using Docker
  #### **Swagger Api Url**
 ```
  http://127.0.0.1:8000/
  ```
   #### **Health Check Url**
 ```
  http://127.0.0.1:8000/ht/
  ```
