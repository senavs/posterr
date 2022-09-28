# Posterr

## Description
The Project Manager you work with wants to build a new product, a new social media application called Posterr. 
Posterr is very similar to Twitter, but it has far fewer features.

Posterr only has two pages, the homepage, and the user profile page, which are described below. Other data and actions are also detailed below. 

## Set up
The project was built using Python as programming language and Docker to deploy. 
To setup locally, you only need [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

If you prefer to not use Docker, you will need to install Python and its all dependencies locally.

After install Docker and clone the project, you run the following command to start up the application

```sh
cd posterr
docker compose up
```

**Note:** If you are using a older Docker Compose version, run `docker-compose` instead of `docker compose`

If the application was built successfully, you will see something like in the terminal:

```
...
postter-database  | 2022-09-28 21:13:01.660 UTC [25] LOG:  database system was shut down at 2022-09-26 22:32:56 UTC
postter-database  | 2022-09-28 21:13:01.695 UTC [1] LOG:  database system is ready to accept connections
poster-backend    | INFO:     Will watch for changes in these directories: ['/posterr']
poster-backend    | INFO:     Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)
poster-backend    | INFO:     Started reloader process [1] using StatReload
poster-backend    | INFO:     Started server process [8]
poster-backend    | INFO:     Waiting for application startup.
poster-backend    | INFO:     Application startup complete.
```

Now open your browser at http://0.0.0.0:8888/docs to access the Swagger and test it.


## Test
To run the tests in your local machine, please install all dependencies in [requirements.txt](https://github.com/senavs/posterr/blob/master/posterr/requirements.txt) file.

After that, you can execute the following command to run all tests cases:
```sh
cd posterr/posterr
DATABASE_URI=sqlite:///./tst.db coverage run -m pytest tst && coverage report -m
```

All tests run successfully and you will be able to see the test coverage:
```
---------------------------------------------------------
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
__init__.py                     0      0   100%
src/__init__.py                 6      0   100%
src/config.py                  12      0   100%
src/database/__init__.py        8      0   100%
src/database/client.py         36      0   100%
src/database/loader.py         13      0   100%
src/models/__init__.py          2      0   100%
src/models/base.py             22      3    86%   9, 18, 31
src/models/post.py             25      0   100%
src/models/user.py             12      0   100%
src/modules/__init__.py         0      0   100%
src/modules/post.py            61      4    93%   34, 36, 42, 51
src/modules/user.py             9      1    89%   11
src/payloads/__init__.py        0      0   100%
src/payloads/post.py           26      0   100%
src/payloads/user.py            4      0   100%
src/routes/__init__.py          4      0   100%
src/routes/post.py             17      0   100%
tst/__init__.py                 0      0   100%
tst/conftest.py                 5      0   100%
tst/e2e/__init__.py             0      0   100%
tst/e2e/test_app.py             9      0   100%
tst/e2e/test_post.py           51      0   100%
tst/e2e/utils/__init__.py       0      0   100%
tst/e2e/utils/post.py           8      0   100%
---------------------------------------------------------
TOTAL                         330      8    98%
```


## Critique
What could be improved?

- Code:
  - Implement unit tests. Since the idea was to test the whole application functionality, only integration (e2e) tests were created.
  - Comment code functions and each swagger http method.
  - Use raw SQL queries instead of SQLAlchemy query objects to increase performance.

- Architecture:
  - A full cloud native application, instead of one machine hosting the whole service.
  - Add an API Gateway to route, authenticate and cache the requests.
  - Even if it was deployed using AWS Lambdas or AWS EC2, for example, add a load balance to scale the application when needed
  - Implement a server side cache to not query the database each search request.
  - Change the database to a NoSQL database to increase performance and scalability.
  - Depending on how big was the database, implement a Data Warehouse to search and query posts efficiently.

## Links:
- [Requirements](https://onstrider.notion.site/Strider-Web-Back-end-Assessment-3-0-9dc16f041f5e4ac3913146bd7a8467c7)
