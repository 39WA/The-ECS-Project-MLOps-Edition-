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

Optimised ML container images and learned about dependency size management.

<img src="docs/docker-push-ecr.png" width="800"/>


### 💰 Cost Considerations

- ECR storage: ~$0.50/month  
- ECS + ALB: ~$1.50/day when running  
- Resources are destroyed after testing to minimize cost


## ☁️ Deployment (AWS ECS - Fargate)
- Services Used
- ECS (Fargate)
- ECR
- Application Load Balancer
- Route53
- AWS Certificate Manager (ACM)
- IAM
- VPC


# ☁️ AWS ECS Fargate Deployment

The containerised YOLOv8 Flask backend was successfully deployed to AWS ECS using Fargate behind an Application Load Balancer (ALB).

This section documents the full deployment workflow, debugging process, infrastructure setup, and final production deployment.

---

# AWS Services Used

- Amazon ECS (Fargate)
- Amazon Elastic Container Registry (ECR)
- Application Load Balancer (ALB)
- IAM Roles
- VPC Networking
- Security Groups
- CloudWatch Logs
- ECS Task Definitions
- ECS Services

---

# Deployment Features Implemented

- Docker container deployment to ECS
- Container image hosting in Amazon ECR
- ECS cluster provisioning
- ECS service configuration
- Application Load Balancer integration
- Public endpoint exposure
- Health check configuration
- CloudWatch logging
- ECS deployment troubleshooting
- ARM64 vs x86_64 architecture debugging
- ECS task recovery workflows

---

# 🚀 Deployment Workflow

---

# 1️⃣ Create Amazon ECR Repository

An Amazon Elastic Container Registry (ECR) repository was created to host the backend Docker images.

<img src="docs/ecr-repository.png" width="1000"/>

---

# 2️⃣ Build and Tag Docker Image

The YOLOv8 backend Docker image was built locally and tagged for ECR deployment.

```bash
docker build -t yolov8-backend .
docker tag yolov8-backend:latest \
739340816202.dkr.ecr.eu-west-2.amazonaws.com/yolov8-backend:latest
```

---

# 3️⃣ Authenticate Docker with Amazon ECR

Docker authentication was configured using AWS CLI credentials.

```bash
aws ecr get-login-password --region eu-west-2 \
| docker login --username AWS --password-stdin \
739340816202.dkr.ecr.eu-west-2.amazonaws.com
```

---

# 4️⃣ Push Docker Image to ECR

The Docker image was successfully pushed to the ECR repository.

## Docker Push In Progress

<img src="docs/ecr-push-in-progress.png" width="1000"/>

---

## Docker Push Progress

<img src="docs/ecr-push-complete.png" width="1000"/>

---

## Docker Push Completed Successfully

<img src="docs/ecr-push-success.png" width="1000"/>

---

# 5️⃣ Verify Uploaded Docker Image in ECR

The uploaded container image was verified inside Amazon ECR.

<img src="docs/ecr-image.png" width="1000"/>

---

# 6️⃣ Create ECS Cluster

An ECS cluster was created successfully for AWS Fargate deployment.

<img src="docs/ecs-cluster-created.png" width="1000"/>

---

# ⚠️ ECS Deployment Troubleshooting

Several deployment issues occurred during production rollout and were debugged using ECS task monitoring and CloudWatch logs.

---

# 7️⃣ Initial ECS Service Deployment Failure

The ECS service deployment initially failed and rolled back automatically.

<img src="docs/ecs-deployment-failed.png" width="1000"/>

---

# 8️⃣ ECS Rollback Triggered

The ECS deployment circuit breaker triggered a rollback because tasks failed health checks.

<img src="docs/ecs-rollback.png" width="1000"/>

---

# 9️⃣ ECS Tasks Stuck in Pending State

During troubleshooting, ECS tasks remained in a pending state while debugging container startup issues.

<img src="docs/ecs-task-pending.png" width="1000"/>

---

# 🔟 CloudWatch Runtime Error Investigation

CloudWatch logs revealed the following runtime error:

```text
exec /usr/local/bin/python: exec format error
```

This occurred because the Docker image was built for ARM64 architecture instead of x86_64, which ECS Fargate expected.

<img src="docs/ecs-exec-format-error.png" width="1000"/>

---

# 🛠️ Resolving the Architecture Issue

The Docker image was rebuilt for the correct Linux AMD64 platform.

```bash
docker buildx build \
--platform linux/amd64 \
-t yolov8-backend:latest .
```

The rebuilt image was then re-tagged and pushed to Amazon ECR.

---

# ✅ Successful ECS Deployment

After rebuilding and redeploying the container image, the ECS tasks started successfully and the API became publicly accessible.

---

# 1️⃣1️⃣ Direct ECS Task Health Check

The Flask API successfully responded from the ECS task public IP address.

<img src="docs/ecs-direct-health-check.png" width="1000"/>

---

# 1️⃣2️⃣ ALB Health Check Endpoint Success

The Application Load Balancer successfully routed traffic to the ECS service health endpoint.

<img src="docs/ecs-yolov8-health-endpoint-success.png" width="1000"/>

---

# 1️⃣3️⃣ Final Production Endpoint Working

The final production endpoint successfully returned a valid response through the Application Load Balancer.

<img src="docs/ecs-yolov8-root-endpoint-success.png" width="1000"/>

---

# ✅ Deployment Successfully Verified

The following production deployment functionality was successfully verified:

- ECS Fargate deployment
- Docker container orchestration
- ECR image hosting
- ECS task scheduling
- ALB traffic routing
- Health check monitoring
- Public endpoint accessibility
- CloudWatch debugging workflows
- ECS rollback troubleshooting
- Architecture compatibility debugging
- Production Flask API deployment

---

# 📌 Final Result

The YOLOv8 Flask backend is now successfully containerised and deployed on AWS ECS Fargate behind an Application Load Balancer with working public endpoints and health monitoring.


## 🏗️ Infrastructure as Code (Terraform)

# Infrastructure as Code (Terraform)

## Objective

Provision the AWS infrastructure for the YOLOv8 MLOps deployment using Terraform.

This section automates:

- VPC networking
- Public subnets
- Security groups
- ECS Cluster
- ECS Task Definition
- ECS Fargate Service
- Application Load Balancer (ALB)
- Target Group
- CloudWatch logging
- IAM roles

---

# Architecture

```text
Internet
   ↓
Application Load Balancer (ALB)
   ↓
ECS Fargate Service
   ↓
YOLOv8 Flask Container
   ↓
Amazon ECR Image
```

---

# Project Structure

```text
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── provider.tf
├── ecs.tf
├── alb.tf
├── iam.tf
├── networking.tf
├── terraform.tfvars
```

---


# provider.tf

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
```

---

# variables.tf

```hcl
variable "aws_region" {
  default = "eu-west-2"
}

variable "project_name" {
  default = "yolov8"
}

variable "container_image" {
  default = "739340816202.dkr.ecr.eu-west-2.amazonaws.com/yolov8-backend:latest"
}
```

---

# networking.tf

```hcl
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "yolov8-vpc"
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "yolov8-igw"
  }
}

resource "aws_subnet" "public_a" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "eu-west-2a"
  map_public_ip_on_launch = true

  tags = {
    Name = "yolov8-public-a"
  }
}

resource "aws_subnet" "public_b" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "eu-west-2b"
  map_public_ip_on_launch = true

  tags = {
    Name = "yolov8-public-b"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.public_a.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.public_b.id
  route_table_id = aws_route_table.public.id
}

resource "aws_security_group" "ecs_sg" {
  name        = "yolov8-sg"
  description = "Allow HTTP traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

# iam.tf

```hcl
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole-yolov8"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
```

---

# alb.tf

```hcl
resource "aws_lb" "main" {
  name               = "yolov8-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.ecs_sg.id]

  subnets = [
    aws_subnet.public_a.id,
    aws_subnet.public_b.id
  ]
}

resource "aws_lb_target_group" "app" {
  name        = "yolov8-target-group"
  port        = 5000
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = aws_vpc.main.id

  health_check {
    path                = "/health"
    protocol            = "HTTP"
    matcher             = "200"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.main.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.app.arn
  }
}
```

---

# ecs.tf

```hcl
resource "aws_ecs_cluster" "main" {
  name = "yolov8-cluster"
}

resource "aws_cloudwatch_log_group" "ecs_logs" {
  name = "/ecs/yolov8"
}

resource "aws_ecs_task_definition" "app" {
  family                   = "yolov8-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "1024"
  memory                   = "3072"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name      = "yolov8-backend"
      image     = var.container_image
      essential = true

      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = aws_cloudwatch_log_group.ecs_logs.name
          awslogs-region        = var.aws_region
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}

resource "aws_ecs_service" "app" {
  name            = "yolov8-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets = [
      aws_subnet.public_a.id,
      aws_subnet.public_b.id
    ]

    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = "yolov8-backend"
    container_port   = 5000
  }

  depends_on = [aws_lb_listener.http]
}
```

---

# outputs.tf

```hcl
output "alb_dns_name" {
  value = aws_lb.main.dns_name
}
```

---

# terraform.tfvars

```hcl
aws_region = "eu-west-2"
```

---

# Step 3 — Initialise Terraform

```bash
terraform init
```

Expected:

```text
Terraform has been successfully initialized!
```

Screenshot:

```text
<p align="left">
<img src="docs/terraform-init-success.png"/>
<p>

```

---

# Step 4 — Validate Configuration

```bash
terraform validate
```

Expected:

```text
Success! The configuration is valid.
```

Screenshot:

```text
terraform-validate-success.png
```

---

# Step 5 — Review Infrastructure Plan

```bash
terraform plan
```

Screenshot:

```text
terraform-plan.png
```

---

# Step 6 — Deploy Infrastructure

```bash
terraform apply
```

Type:

```text
yes
```

Screenshot:

```text
terraform-apply-success.png
```

---

# Step 7 — Retrieve ALB URL

```bash
terraform output
```

Expected:

```text
alb_dns_name = "yolov8-alb-xxxxxxxx.eu-west-2.elb.amazonaws.com"
```

Screenshot:

```text
terraform-output-alb.png
```

---

# Step 8 — Test Health Endpoint

Open:

```text
http://ALB-DNS/health
```

Expected:

```json
{"status":"ok"}
```

Screenshot:

```text
terraform-health-success.png
```

---

# Step 9 — Test Predict Endpoint

```bash
curl -X POST -F "image=@test.jpg" http://ALB-DNS/predict
```

Expected:

```json
[
  {
    "bbox": [...],
    "confidence": 0.89,
    "label": 2
  }
]
```

Screenshot:

```text
terraform-predict-success.png
```

---

# Terraform Resources Used

| Resource | Purpose |
|---|---|
| aws_vpc | Networking |
| aws_subnet | Public subnets |
| aws_security_group | Firewall rules |
| aws_lb | Application Load Balancer |
| aws_lb_target_group | ECS routing |
| aws_ecs_cluster | Container orchestration |
| aws_ecs_task_definition | Container specification |
| aws_ecs_service | Running service |
| aws_cloudwatch_log_group | Logging |
| aws_iam_role | ECS permissions |

---

# Skills Demonstrated

- Infrastructure as Code (IaC)
- Terraform automation
- AWS ECS/Fargate deployment
- ALB configuration
- Container orchestration
- Cloud networking
- IAM configuration
- Cloud-native MLOps deployment
- Production-ready infrastructure provisioning

---

# Cleanup

Destroy all infrastructure to avoid AWS charges:

```bash
terraform destroy
```

Type:

```text
yes
```

---

# Portfolio Outcome

This section demonstrates production-grade Infrastructure as Code deployment for a machine learning inference service using Terraform and AWS ECS/Fargate.


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

