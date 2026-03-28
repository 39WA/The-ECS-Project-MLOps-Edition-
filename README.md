# 🚀 YOLOv8 MLOps Project — Production Deployment on AWS ECS

![AWS](https://img.shields.io/badge/AWS-ECS%20%7C%20Fargate-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-623CE4)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-black)
![Model](https://img.shields.io/badge/Model-YOLOv8-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> Production-grade MLOps system deploying an object detection model using Docker, Terraform, AWS ECS (Fargate), and CI/CD with full HTTPS support.

---

## 📌 Overview

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

    📁 Project Structure

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


🖥️ Application
Backend (Flask API)
/health → Service health check
/predict → Object detection endpoint
Loads YOLOv8 model (yolov8n.pt)
Returns:
Bounding boxes
Labels
Confidence scores


Frontend
Image upload interface
Sends requests to /predict
Displays detection results

🐳 Containerisation
Multi-stage Docker builds
Non-root user for security
Lightweight base images
Separate frontend/backend services


📦 Container Registry (ECR)

Images are stored in Amazon ECR.

docker tag yolov8-backend:latest <ecr-repo>:tag
docker push <ecr-repo>:tag

☁️ Deployment (AWS ECS - Fargate)
Services Used
ECS (Fargate)
ECR
Application Load Balancer
Route53
AWS Certificate Manager (ACM)
IAM
VPC


🏗️ Infrastructure as Code (Terraform)

All AWS infrastructure is provisioned using Terraform.


🔁 CI/CD Pipeline

Implemented using GitHub Actions.

Pipeline Stages
Build Docker images
Push images to ECR
Deploy infrastructure (Terraform)
Update ECS service
Run health checks


📸 Screenshots (To Add)
Application
UI with object detection results
API response output
Docker
Running containers locally
AWS
ECS service
ALB configuration
HTTPS working
CI/CD
GitHub Actions pipeline

