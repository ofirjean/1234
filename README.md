# Passover_Project - Dockerized Flask + MongoDB App

## Step 1: Create the Project Directory
A project directory named `Passover_Project` was created to organize all related files.

## Step 2: Create the Flask Application
A simple Flask API was built that:
- Receives first name and last name via a POST request.
- Stores the data in a database.

## Step 3: Connect to MongoDB
Using the `pymongo` library, the Flask app connects to a MongoDB database where the data is stored.

## Step 4: Create a Dockerfile
A `Dockerfile` was created that:
- Installs all necessary dependencies.
- Builds a Docker image for the Flask application.

## Step 5: Create docker-compose.yml
A `docker-compose.yml` file was written to:
- Run both the Flask application and MongoDB as separate services.
- Define the dependencies and networking between services.

## Step 6: Build and Run the System
The system was run using `docker-compose up --build`. Functionality was tested by:
- Sending POST requests with data.
- Retrieving the stored data via a GET endpoint.

## Step 7: Verify Everything Works
The application and database services were verified to run in containers, and communication between them was successful via the API.
