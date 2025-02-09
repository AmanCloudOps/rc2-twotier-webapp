# Flask App with MySQL Docker Setup

This is a simple Flask app that interacts with a MySQL database.

## Project Setup

### Step 1: Create Project Directory
```sh
mkdir docker_project
cd docker_project
```

### Step 2: Create `app.py`
This file contains the Flask application logic.

### Step 3: Create `Dockerfile`
```sh
vim Dockerfile
```
Define the necessary instructions to build the Flask app image.

## Running Without Docker Compose

### Step 4: Build the Docker Image
```sh
docker build -t flask-app .
```

### Step 5: Create a Network
```sh
docker network create -d bridge mynetwork
```

### Step 6: Run Containers
```sh
docker run -d --name mysql-container --network mynetwork -e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=test_db -p 3306:3306 mysql:8

docker run -d --name flask-container --network mynetwork -p 5000:5000 flask-app
```

### Step 7: Access the Application
Open your browser and go to:
```
http://localhost:5000
```

## Running with Docker Compose

### Step 8: Create `docker-compose.yml`
```sh
vim docker-compose.yml
```
Define services for both Flask and MySQL in this file.

### Step 9: Start Containers
```sh
docker compose up -d
```

### Step 10: Access the Flask App
- **Frontend (Web):** `http://localhost:5000/`
- **Backend (MySQL):** `http://localhost:5000/db`

## Notes
- Replace placeholders (e.g., `your_username`, `your_password`, `your_database`) with actual MySQL configurations.
- This setup is for demonstration purposes. Follow best practices for security and performance in production.
- If you encounter issues, check Docker logs and error messages for troubleshooting:
```sh
docker logs flask-container
docker logs mysql-container
```

