# PizzaStore
CRUD operation for a pizza store in django rest framework.


# Development Setup

## Windows 64 bit

1. Install these tools
    * [Python v3.6.2 64 bit](https://www.python.org/downloads/)
    * [Git](https://git-scm.com/download/win)


1. Upgrade pip

    ```bash
    python -m pip install --upgrade pip
    ```

1. Setup virtualenv

    ```bash
    python -m venv venv
    venv\ Scripts\ activate.bat
    ```


1. Download backendApp repository

    ```bash
    https://github.com/Gopinathpanda/PizzaStore.git
    ```

1. Install project dependencies

    ```bash
    Go to the folder where requirements.txt present and run command
    pip install -r requirements.txt
    ```
1. To store Data in DataBase

     ```bash
    python manage.py runserver
    ```

# API Endpoints and Responses

## GET API

1. API- http://localhost:8000/pizza/getpizza
2. Method - get
3.  Success Response - 200 ok
      [
    {
        "pizza_type": "Regular",
        "pizza_size": "Small",
        "toppings": "Onions"
    },
    {
        "pizza_type": "Regular",
        "pizza_size": "Medium",
        "toppings": "Paneer"
    },
    {
        "pizza_type": "Square",
        "pizza_size": "Large",
        "toppings": "Mushrooms"
    },
    {
        "pizza_type": "Regular",
        "pizza_size": "Medium",
        "toppings": "Cheese"
    }
]
4. Error Response - 400 Bad Request

1. API- http://localhost:8000/pizza/getpizza/pizza_type/piza_typeName
   Ex- http://localhost:8000/pizza/getpizza/pizza_type/Regular
   Method- get
   Success Resposnse- 200 ok
   [
    {
        "pizza_type": "Regular",
        "pizza_size": "Small",
        "toppings": "Onions"
    },
    {
        "pizza_type": "Regular",
        "pizza_size": "Medium",
        "toppings": "Paneer"
    },
    {
        "pizza_type": "Regular",
        "pizza_size": "Medium",
        "toppings": "Cheese"
    }
]
Error Response - 400 Bad Request


1. API - http://localhost:8000/pizza/getpizza/pizza_size/piza_sizeName
   Ex - http://localhost:8000/pizza/getpizza/pizza_size/Medium
   method - get
  Success Response - 200 ok
   [
    {
        "pizza_type": "Regular",
        "pizza_size": "Medium",
        "toppings": "Paneer"
    },
    {
        "pizza_type": "Regular",
        "pizza_size": "Medium",
        "toppings": "Cheese"
    }
]

Error Response - 400 Bad Request
## Create Api

1. API - http://localhost:8000/pizza/addpizza
   Method - post
   media_type- application/json
   Request Body -
      {
      "pizza_type":"Square",
      "pizza_size":"Large",
      "toppings":"onions"
      }
     Success Response- Redirect to Get Api
     Error Response - 400 Bad Request
     
  ## Edit Api
  1. API - http://localhost:8000/pizza/editpizza/id
     Ex - http://localhost:8000/pizza/editpizza/4
     Method - put
     media_type- application/json
      Request Body -
      {
      "pizza_type":"Square",
      "pizza_size":"Large",
      "toppings":"Jalapeno"
      }
     Success Response- 200 ok
     Error Response - 400 Bad Request
   
   ## Delete Api
   1. API - http://localhost:8000/pizza/editpizza/id
     Ex - http://localhost:8000/pizza/editpizza/4
     Method - delete
     Success Response- 200 ok
     Error Response - 400 Bad Request



