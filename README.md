# final-challenge
This repository aims to implement a simple api developed in FastAPI with PostgresSQL simulating a small eccommerce.

## installation
We have 2 options
- Execute project using docker
- Execute project locally


## 1 - Using docker
```
 docker compose up
```


## 2 - Install dependencies locally
We need install project dependencies with `poetry`:
###### obs: Can you install poetry in [this link](https://python-poetry.org/docs/)

1 - Create .env archive with local envirements
```
cp local.env .env
```
obs: you need fill the environments

2 - Execute the virtualenv

```
poetry shell
```

3 Install dependencies
```
poetry install
```

4 - Execute the server api:

```
uvicorn src.main:app --reload
```
