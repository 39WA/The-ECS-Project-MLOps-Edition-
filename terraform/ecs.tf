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
  subnets = data.aws_subnets.existing.ids

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