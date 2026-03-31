# 🚀 YOLOv8 MLOps Project — Production Deployment on AWS ECS

![AWS](https://img.shields.io/badge/AWS-ECS%20%7C%20Fargate-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-623CE4)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-black)
![Model](https://img.shields.io/badge/Model-YOLOv8-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> Production-grade MLOps system deploying an object detection model using Docker, Terraform, AWS ECS (Fargate), and CI/CD with full HTTPS support.

---

## 📌 Project Overview

This project is an end-to-end MLOps application that deploys a YOLOv8 object detection model as a production-ready web service on AWS.

Users can upload an image through a frontend interface, which sends the request to a Flask-based API. The API performs inference using a pre-trained YOLOv8 model and returns detected objects with bounding boxes and confidence scores.

The application is fully containerised using Docker and deployed on AWS ECS (Fargate) behind an Application Load Balancer with HTTPS enabled via AWS Certificate Manager and Route53.

All infrastructure is provisioned using Terraform, and deployments are automated through a CI/CD pipeline using GitHub Actions.

This project demonstrates real-world MLOps practices, including model serving, container orchestration, infrastructure as code, and automated deployments.

This project demonstrates a **real-world MLOps workflow**, taking a machine learning model from:

**Local Development → Containerisation → Cloud Deployment → Infrastructure as Code → CI/CD Automation**

Unlike traditional ML projects, this focuses on **deployment, scalability, and production readiness**.

---

## 🧠 Key Features

- YOLOv8 object detection API  
- Full-stack application (Frontend + Flask backend)  
- Dockerised services (production-ready)  
- AWS ECS (Fargate) deployment  
- HTTPS with custom domain (Route53 + ACM)  
- Infrastructure as Code using Terraform  
- CI/CD pipeline with GitHub Actions  
- Health checks and automated deployments  

---

## 🏗️ Architecture

### 🔁 System Flow

```mermaid
flowchart LR
    A[User Browser] --> B[Frontend UI]
    B --> C[ALB HTTPS]
    C --> D[ECS Fargate Service]
    D --> E[Flask API]
    E --> F[YOLOv8 Model]
    F --> E
    E --> B
```

## 📁 Project Structure

```
.
├── app/
│   ├── frontend/
│   ├── backend/
│   ├── Dockerfile(s)
│   └── .dockerignore
│
├── infra/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── modules/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── README.md
└── .gitignore

```


## 🖥️ Application
Backend (Flask API)
- Health → Service health check
- Predict → Object detection endpoint
- Loads YOLOv8 model (yolov8n.pt)
- Returns:
- Bounding boxes
- Labels
- Confidence scores

### Application

#### Health Check Endpoint

The `/health` endpoint verifies that the Flask API is running correctly.

```bash
curl http://localhost:5001/health
```
{"status":"ok"}

<p align="left">
  <img src="docs/health-check.png" width="800"/>
</p>

### Application — Object Detection

The `/predict` endpoint performs real-time object detection using the YOLOv8 model.


```bash
curl -X POST -F "image=@test.jpg" http://localhost:5001/predict
```

[
  {
    "bbox": [130.57, 129.97, 3687.63, 1657.32],
    "confidence": 0.88,
    "label": 2
  }
]

<p align="left">
  <img src="docs/predict-output.png" width="800"/>
</p>



Frontend
- Image upload interface
- Sends requests to /predict
- Displays detection results

### Application — Frontend UI

The frontend allows users to upload an image and perform real-time object detection using the YOLOv8 model.

<img src="docs/predict-output.png" width="800"/>

🐳 Containerisation
- Multi-stage Docker builds
- Non-root user for security
- Lightweight base images
- Separate frontend/backend services

The backend API is fully containerised using Docker and runs inside an isolated environment with all dependencies installed.

The container exposes port `5000`, which is mapped to port `5002` on the host machine.

<img src="docs/docker-backend-running.png" width="800"/>

### 🔍 Verification

The container is verified using:

- `docker ps` to confirm it is running  
- `/health` endpoint to confirm API availability  


## 🌐 Full System — End-to-End Application

The complete application is running locally with:

- Frontend served via a lightweight HTTP server  
- Backend running inside a Docker container  
- YOLOv8 model performing real-time object detection  
- API communication over HTTP  

Users can upload an image and receive detection results including bounding boxes, labels, and confidence scores.

<img src="docs/full-system-working.png" width="800"/>


## 📦 Container Registry (ECR)

- Images are stored in Amazon ECR.

- docker tag yolov8-backend:latest <ecr-repo>:tag
- docker push <ecr-repo>:tag

The Docker image is pushed to Amazon Elastic Container Registry (ECR) for deployment.

<img src="docs/docker-push-ecr.png" width="800"/>


## ☁️ Deployment (AWS ECS - Fargate)
- Services Used
- ECS (Fargate)
- ECR
- Application Load Balancer
- Route53
- AWS Certificate Manager (ACM)
- IAM
- VPC


## 🏗️ Infrastructure as Code (Terraform)

All AWS infrastructure is provisioned using Terraform.


## 🔁 CI/CD Pipeline

Implemented using GitHub Actions.

- Pipeline Stages
- Build Docker images
- Push images to ECR
- Deploy infrastructure (Terraform)
- Update ECS service
- Run health checks


## 📸 Screenshots (To Add)
- Application
- UI with object detection results
- API response output
- Docker
- Running containers locally
- AWS
- ECS service
- ALB configuration
- HTTPS working
- CI/CD
- GitHub Actions pipeline

