Project Progress
The idea of this project was to be a educational and practicing challenge for the holiday, it started as a
containerized Flask app connected to MongoDB, running locally with Docker. In the recent steps, I've transitioned the application to Kubernetes, taking it from simple containerization to orchestrating it within Kubernetes Pods.

I began by deploying the Flask API and MongoDB as separate containers in Kubernetes, using Secrets for MongoDB credentials. The Flask app is now successfully running in Kubernetes, connected to a MongoDB service within the cluster. Persistent storage for MongoDB is planned next to ensure data durability.
Many updated are coming soon, until i'll be more decisive in the future on the project purpose.