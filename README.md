# User app with JWT and DRF

## Development setup
Install Python 3.7.2

Create a virtual environment: <br/>
`python3 -m venv venv`

To activate a venv: <br/>
`source venv/bin/activate`

Install dependencies: <br/>
`pip install -r requirements.txt`

## Migrate db:
`python3 manage.py makemigrations` <br>
`python3 manage.py migrate`

## To create an admin account:

`python manage.py createsuperuser`

## Access API

You may access the API using [Postman](https://www.postman.com/).

**e.g. access API:**

1. Create POST request for `http://127.0.0.1:8000/api/signup`, go to body and select `raw` and the `JSON`.

In the body enter:

```
{
 "email":"ram@gmail.com",
 "password":"123456",
 "profile": {
        "first_name": "ram",
        "last_name": "kumar",
        "phone_number": "1234567891",
        "age": 11,
        "gender": "M"
 }
}
```

Expect:

```
{
"success": "True",
"status code": 201,
"message": "User registered  successfully"
}
```

2. Create POST request for `http://127.0.0.1:8000/api/signin`, go to body and select `raw` and the `JSON`.

In the body put this:

```
{
 "email":"ram@gmail.com",
 "password":"123456"
}
```

Expect:

```
{
"success": "True",
"status code": 200,
"message": "User logged in  successfully",
"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiODY3Y2E3YjAtZDhjNC00ZTdkLWE1NmYtOWRhYWJkOTAwNmQ1IiwidXNlcm5hbWUiOiJyYW1AZ21haWwuY29tIiwiZXhwIjoxNTgwMTA0MDc4LCJlbWFpbCI6InJhbUBnbWFpbC5jb20ifQ.0cCgOlKrYHrouVJEeIEt6TdGyza2C78J5swXFEaLLFM"
}
```

Then copy token.

3. Create GET request for `http://127.0.0.1:8000/api/profile`, go to Authorization and select from type `Bearer Token`, paste copied token and hit the request.

Expect:

```
{
"success": "True",
"status code": 200,
"message": "User profile fetched successfully",
"data": [
    {
       "first_name": "ram",
       "last_name": "kumar",
       "phone_number": "1234567891",
       "age": 11,
       "gender": "M"
    }
   ]
}
```

## Info

The application is inspired by a tutorial from medium.com.