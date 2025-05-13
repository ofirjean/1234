Passover_Project – Kubernetes Migration Plan
============================================

✅ Phase 1: Core Setup
----------------------

Step 1: Create a Namespace
--------------------------
To organize and isolate the project:

kubectl create namespace passover-api

Step 2: Create a Secret for MongoDB Credentials
-----------------------------------------------
Securely store MONGO_USER and MONGO_PASSWORD:

kubectl create secret generic mongo-secret \
  --from-literal=mongo-user=<your_user> \
  --from-literal=mongo-password=<your_password> \
  -n passover-api

Optional: Store this as a secrets.yaml file for version control.

Step 3: Deploy MongoDB
----------------------
Create a deployment and service for MongoDB using your secret credentials.

File: mongo-deployment.yaml

Includes:
- MongoDB Deployment
- ClusterIP Service named mongo-service

Step 4: Deploy Flask API
------------------------
Deploy the backend container (from Docker Hub), configured to connect to MongoDB.

File: flask-deployment.yaml

Includes:
- Flask Deployment with environment variables
- ClusterIP Service named flask-service

✅ Phase 2: Storage & Frontend
------------------------------

Step 5: Add Persistent Volume for MongoDB
-----------------------------------------
Ensure MongoDB data survives restarts.

File: mongo-pv-pvc.yaml

Includes:
- PersistentVolume using hostPath
- PersistentVolumeClaim

Modify mongo-deployment.yaml:
- Add volumeMounts to container
- Add volumes to pod spec

Step 6: Connect Frontend
------------------------
Deploy a frontend (e.g., HTML via Nginx) to Kubernetes.

File: frontend-deployment.yaml

Includes:
- Frontend Deployment (e.g., with Nginx)
- Service named frontend-service

Connect frontend to backend using internal DNS (flask-service).

✅ Phase 3: Production Readiness
-------------------------------

Step 7: Expose the App via Ingress
----------------------------------
Make your app accessible via a browser.

File: ingress.yaml

Includes:
- Ingress routing to services
- Domain or path routing (e.g., /api)

Note: Requires NGINX Ingress Controller installed in your cluster.

Step 8: Add Health Checks
-------------------------
Improve reliability with probes.

Add livenessProbe and readinessProbe to both:
- flask-deployment.yaml
- mongo-deployment.yaml

Step 9: Use ConfigMaps for Config
---------------------------------
Manage non-sensitive settings like host and port.

File: configmap.yaml

Example:

apiVersion: v1
kind: ConfigMap
metadata:
  name: flask-config
data:
  MONGO_HOST: mongo-service
  MONGO_PORT: "27017"

Reference in Deployment using envFrom.

Step 10: Organize Your YAML Files
---------------------------------
Recommended structure for maintainability:

Passover_Project/
├── k8s/
│   ├── flask-deployment.yaml
│   ├── mongo-deployment.yaml
│   ├── mongo-pv-pvc.yaml
│   ├── secrets.yaml
│   ├── configmap.yaml
│   ├── frontend-deployment.yaml
│   ├── ingress.yaml

✅ What’s Next?
---------------
Let me know if you want to:
- Finalize PersistentVolume and test persistence
- Deploy the frontend
- Set up Ingress
- Add monitoring or auto-scaling

I'll guide you step-by-step.
