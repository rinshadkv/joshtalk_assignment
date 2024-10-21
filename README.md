# Task Management API

## Overview

This project is a Django-based API for managing tasks, including creating tasks, assigning them to users, and retrieving tasks for specific users. The application is containerized using Docker Compose for easy setup and deployment.
### Prerequisites
You do not need to install Python or PostgreSQL locally, as the application runs within Docker containers. However, you should have the following installed on your machine:

* Docker: Install Docker
* Docker Compose: Install Docker Compose

### Getting Started
1. Clone the Repository

   ````
   git clone <repository-url> 
   ````

   ````
   cd <repository-directory>
   ````
2. Build and Start the Containers

    Run the following command to build the Docker images and start the containers:
    ```` docker-compose up --build````
3. Testing the API

    The API will be accessible at http://localhost:8000/api/. You can use tools like Postman or curl to interact with the endpoints.


###   Api Endpoints
1. Create a Task
   Endpoint: POST /api/tasks/

   Request Body:

   ```` 
   {
   "name": "Task Name",
   "description": "Task Description",
   "task_type": "Task Type"
   } 
   ````

   Response :

   ````
   {
   "id": 1,
   "name": "Task Name",
   "description": "Task Description",
   "created_at": "2024-10-22T00:00:00Z",
   "task_type": "Task Type",
   "status": "PENDING",
   "assigned_users": []
   }
   ````
   
2. Assign Users to a Task
   Endpoint: POST /api/tasks/<task_id>/assign/

   Request Body:
    ````
   {
    "user_ids": [1, 2, 3]
   }
   ````
   Response :

   ````
   {
    "status": "Task assigned successfully!"
   }

   ````
   
3. Get Tasks for a Specific User
   Endpoint: GET /api/users/<user_id>/tasks/

   Response:

   ````
   [
    {
        "id": 1,
        "name": "Task 1",
        "description": "This is task 1.",
        "created_at": "2024-10-21T21:27:08.082051",
        "task_type": "SIMPLE",
        "status": "PENDING"
    },
    {
        "id": 2,
        "name": "Task 2",
        "description": "This is task 2.",
        "created_at": "2024-10-22T00:00:00Z",
        "task_type": "COMPLEX",
        "status": "COMPLETED"
    }
   ]

   ````


### Directory Structure
* docker-compose.yml: Configuration file for Docker Compose.
* Dockerfile: Dockerfile for the Django application.
* app/: Directory containing the Django application code.
* dbmigration.sh: Script for managing database migrations.
### Notes
* Ensure Docker is running.
* Fake Data: The application is initialized with fake data for all fields upon startup to facilitate testing and development.
*  Migrations Management: All database migrations are managed by Docker. You can check the dbmigration.sh script for details.
* All operations and configurations are handled within Docker, eliminating the need for local installations of Python and PostgreSQL.
*  You can find a postman collection file with repo located in root folder  [Josh_Assignment.postman_collection.json]