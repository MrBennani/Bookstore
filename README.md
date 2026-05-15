# Bookstore
Bookstore APP from Backend Python course from EBAC

## Prerequisites
```
Python3.12>
Poetry    
Docker && docker-compose

```

## Quickstart
1. Clone this project
    ```shell
    https://github.com/MrBennani/Bookstore
    ```

2. Install dependecies:
    ```shell
    cd bookstore
    poetry install
    ```

3. Run local dev server:
    ```shell
    poetry run manage.py migrate
    poetry run python manage.py runserver
    ```

4. Run docker dev server enviroment:
    ```shell
    docker-compose up -d --build
    docker-compose exec web python manage.py migrate
    ```

5. Run tests inside of docker:
    ```shell
    docker-compose exec web python manage.py test
    ```