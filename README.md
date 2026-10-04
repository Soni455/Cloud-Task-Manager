# Cloud Task Manager API

A simple REST API built with Flask and containerized using Docker. The project demonstrates basic cloud and distributed-system concepts through containerization, automated testing, and CI/CD.

## Project Overview

The Cloud Task Manager API allows users to create, view, update, and delete tasks through HTTP REST API endpoints.

The project was developed as a small cloud technology project using:

* Python
* Flask
* REST API
* Docker
* pytest
* GitHub
* GitHub Actions
* Amazon ECR
* Amazon EC2

## Features

* Health-check endpoint
* Create tasks
* View all tasks
* Update tasks
* Delete tasks
* Input validation
* Automated API testing
* Docker containerization
* Continuous Integration using GitHub Actions
* Cloud deployment using AWS ECR and EC2

## Architecture

### Application Architecture

```text
Client / Browser
       |
       | HTTP Request
       v
Docker Container
       |
       v
Flask REST API
       |
       v
Task Management Logic
       |
       v
JSON Response
```

### CI/CD and Cloud Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----> Run Tests
    |
    +----> Build Docker Image
    |
    v
Amazon ECR
    |
    v
Amazon EC2
    |
    v
Docker Container
    |
    v
Flask REST API
```

## Technology Stack

| Technology     | Purpose                        |
| -------------- | ------------------------------ |
| Python         | Application programming        |
| Flask          | REST API framework             |
| pytest         | Automated testing              |
| Docker         | Application containerization   |
| GitHub         | Source code management         |
| GitHub Actions | Continuous Integration / CI/CD |
| Amazon ECR     | Docker image storage           |
| Amazon EC2     | Cloud deployment               |

## API Endpoints

| Method | Endpoint      | Description              |
| ------ | ------------- | ------------------------ |
| GET    | `/`           | Check application status |
| GET    | `/health`     | Health check             |
| GET    | `/tasks`      | Get all tasks            |
| POST   | `/tasks`      | Create a new task        |
| PATCH  | `/tasks/<id>` | Update a task            |
| DELETE | `/tasks/<id>` | Delete a task            |

### Example: Create a Task

```json
{
  "title": "Learn Docker"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Learn Docker",
  "completed": false
}
```

## Running the Project Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd Cloud-Task-Manager
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run tests

```bash
python -m pytest -q
```

### 6. Start the application

```bash
python -m app.main
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Running with Docker

### Build the Docker image

```bash
docker build -t cloud-task-manager .
```

### Run the container

```bash
docker run -d --name cloud-task-manager -p 5000:5000 cloud-task-manager
```

### Check the running container

```bash
docker ps
```

The application can then be accessed at:

```text
http://127.0.0.1:5000
```

Health check:

```text
http://127.0.0.1:5000/health
```

## Testing

The project contains 6 automated tests covering:

1. Home endpoint
2. Health endpoint
3. Task creation
4. Empty-title validation
5. Task update
6. Task deletion

Run all tests using:

```bash
python -m pytest -q
```

## Continuous Integration

GitHub Actions is configured to automatically:

1. Checkout the source code
2. Set up Python
3. Install project dependencies
4. Run the automated tests

This helps ensure that changes do not break the application.

## AWS Deployment

The Docker image is intended to be stored in **Amazon Elastic Container Registry (ECR)** and deployed on an **Amazon EC2** instance.

The planned deployment architecture is:

```text
GitHub
   |
   v
GitHub Actions
   |
   v
Docker Image
   |
   v
Amazon ECR
   |
   v
Amazon EC2
   |
   v
Docker Container
   |
   v
Flask API
```

AWS deployment details will be added after the ECR and EC2 deployment is completed.

## Project Limitations

* Tasks are stored in application memory.
* Data is lost when the application/container restarts.
* The project is intended as a small academic demonstration rather than a production task-management system.
* Authentication and database persistence are not included.

## Future Improvements

* Add a database such as PostgreSQL or Amazon RDS
* Add user authentication
* Add HTTPS
* Add persistent task storage
* Add monitoring and logging
* Deploy using Amazon ECS instead of a single EC2 instance
* Add automated Docker image deployment through GitHub Actions

## Conclusion

The Cloud Task Manager API demonstrates how a small REST application can be containerized and prepared for cloud deployment. It combines Flask, automated testing, Docker, GitHub Actions, Amazon ECR, and Amazon EC2 to demonstrate a basic cloud-based application workflow.
