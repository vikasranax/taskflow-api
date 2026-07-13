# TaskFlow API

A simple REST API for managing tasks, built with FastAPI and containerized with Docker.

## What it does

Basic CRUD - Create, Read, Update and Delete

## Tech used

- Python / FastAPI
- Uvicorn
- Docker and docker Compose
- Pydantic for data validation

```

## How to run it

You need Docker installed. Then:

```bash
git clone https://github.com/vikasranax/taskflow-api.git
cd taskflow-api
docker-compose up --build
```

API runs on `http://localhost:8000`


## API endpoints

| Method | Endpoint | What it does |
|--------|----------|---------------|
| GET | /api/tasks | List all tasks |
| POST | /api/tasks | Create a task |
| PUT | /api/tasks/{id} | Update a task |
| DELETE | /api/tasks/{id} | Delete a task |


## Author

Vikas — [GitHub](https://github.com/vikasranax)
