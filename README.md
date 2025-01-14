# FastAPI + Firebase Firestore Example

This repository demonstrates how to build a FastAPI application connected to Firebase Firestore, with Docker and Docker Compose for containerization and scalability. It also includes a Makefile to streamline tasks such as installing dependencies, building images, or running tests.

Demo URL: https://bati-predictor.vercel.app/

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Firebase Setup](#firebase-setup)
- [Installation and Local Development](#installation-and-local-development)
- [Running with Docker](#running-with-docker)
- [Using Docker Compose](#using-docker-compose)
- [Using the Makefile](#using-the-makefile)
- [Endpoints](#endpoints)
- [Roadmap & Future Improvements](#roadmap--future-improvements)
- [License](#license)

## Features
- FastAPI application with automatic interactive docs (OpenAPI & ReDoc).
- Firebase Firestore for data persistence, using the official Firebase Admin SDK.
- Dockerfile for containerizing the application.
- `docker-compose.yml` for multi-service orchestration (if needed).
- Makefile with convenient commands: installing dependencies, running locally, building Docker images, pushing to a registry, etc.
- Seed endpoint to populate Firestore with sample data (handy when you don’t have real data on hand).

## Project Structure
```bash
.
├── main.py                   # FastAPI application (entry point)
├── firebase_credentials.json # Firebase service account credentials (example - do not commit in real projects)
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker build instructions
├── docker-compose.yml        # Docker Compose orchestration
├── Makefile                  # Make commands for building, running, etc.
└── README.md                 # This file
```
> **Note:** For production, avoid storing `firebase_credentials.json` directly in the repository. Use environment variables or a secret manager.

## Requirements
- Python 3.7+
- pip or pipenv (for local installation)
- Docker (for containerization)
- Docker Compose (optional, for multi-container orchestration)
- A Firebase project with Firestore enabled.

## Firebase Setup
1. Go to Firebase Console, create (or use an existing) project.
2. Enable Firestore under Build > Firestore Database.
3. In Project Settings, go to Service accounts and generate a new private key in JSON format.
4. Save the file as `firebase_credentials.json` (or any name you prefer).
5. Keep this file private. In real scenarios, do not push it to public repos.

## Installation and Local Development
Clone the repository:
```bash
git clone https://github.com/math1761/price-bati.git
cd fastapi-firebase-example
```
Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
Run the API in development mode (with auto-reload):
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Access the docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## Running with Docker
Build the Docker image:
```bash
docker build -t fastapi-firebase:latest .
```
Run the container:
```bash
docker run -d --name fastapi-firebase -p 8000:8000 fastapi-firebase:latest
```
The application should be accessible at [http://localhost:8000](http://localhost:8000).

## Using Docker Compose
The project includes a `docker-compose.yml` which can help orchestrate multiple services (if needed) and is convenient for local development.

Start everything in detached mode:
```bash
docker-compose up -d --build
```
Stop the services:
```bash
docker-compose down
```
Check logs:
```bash
docker-compose logs -f
```

## Using the Makefile
We provide a Makefile with several helpful targets:
- `make install`: Installs Python dependencies from `requirements.txt`.
- `make dev`: Runs the FastAPI app in development mode (auto-reload).
- `make run`: Runs the FastAPI app in standard mode (no auto-reload).
- `make test`: Runs unit tests (configure as needed).
- `make lint`: Lints the code (configure for flake8, black, etc.).
- `make format`: Formats the code (e.g., black, isort).
- `make docker-build`: Builds the Docker image.
- `make docker-run`: Runs the container in detached mode.
- `make docker-rm`: Stops and removes the running container.
- `make docker-push`: Pushes the built image to a Docker registry.
- `make docker-compose-up`: Launches Docker Compose in detached mode.
- `make docker-compose-down`: Stops Docker Compose services.
- `make docker-compose-logs`: Shows logs in real-time from Docker Compose.
- `make clean`: Cleans up temporary files, Docker dangling images/volumes, etc.

Use `make help` to see all available commands.

## Endpoints
- `GET /`: Returns a welcome message.
- `POST /seed`: Inserts sample data into Firestore (useful for testing when no real data is available).
- `GET /items`: Returns the list of all items (projects) from Firestore.

Additional endpoints can be added in `main.py` as needed.

## Roadmap & Future Improvements
- **Authentication / Authorization:** Secure your endpoints with Firebase Auth or OAuth2.
- **CI/CD:** Set up automated builds, tests, and deployments (e.g., GitHub Actions, GitLab CI).
- **Logging / Monitoring:** Integrate better logging (e.g., using Google Cloud Logging) and application performance monitoring (e.g., Sentry, Datadog).
- **Load Testing:** Use a tool like Locust or k6 to ensure the app scales with Firestore.
- **Secrets Management:** Use a vault or secret manager for the Firebase credentials, rather than embedding them in the image or source code.

## License
This project is licensed under the MIT License. Feel free to use and modify it for your own needs.
