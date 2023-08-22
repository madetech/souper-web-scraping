provider "aws" {
  region = "eu-west-2"  # Change this to your desired region
}

# Create a VPC
resource "aws_vpc" "main" {
  cidr_block = "172.32.0.0/16"

  tags = {
    Name = "souper-vpc"
  }
}

/* Public subnet */
resource "aws_subnet" "souper_subnet_public" {
  vpc_id                  = aws_vpc.main.id
  count                   = 1
  cidr_block              = "172.32.0.0/24"
  availability_zone       = "eu-west-2c"
  map_public_ip_on_launch = true
  tags = {
    Name = "souper-subnet-public-1"
  }
}

resource "aws_subnet" "souper_subnet_private_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "172.32.2.0/24"  # Change this to your desired subnet CIDR block
  availability_zone      = "eu-west-2a"    # Change this to your desired availability zone within the region

  tags = {
    Name = "souper-subnet-private-1"
  }
}

resource "aws_subnet" "souper_subnet_private_2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "172.32.4.0/24"  # Change this to your desired subnet CIDR block
  availability_zone      = "eu-west-2b"    # Change this to your desired availability zone within the region

  tags = {
    Name = "souper-subnet-private-2"
  }
}

# Create a security group for the database
resource "aws_security_group" "database_sg" {
  name = "database"
  vpc_id = aws_vpc.main.id
}

resource "aws_security_group" "backend_sg" {
  vpc_id = aws_vpc.main.id
  name = "backend"
}

resource "aws_security_group" "frontend_sg" {
  name = "frontend"
  vpc_id = aws_vpc.main.id
}

# Create security group rule
resource "aws_security_group_rule" "private_backend_to_database" {
  type              = "ingress"
  from_port         = 5432
  to_port           = 5432
  protocol          = "tcp"
  security_group_id = "${aws_security_group.database_sg.id}"
  source_security_group_id = "${aws_security_group.backend_sg.id}"
}

# Create security group rule
resource "aws_security_group_rule" "private_database_to_backend" {
  type              = "egress"
  from_port         = 5432
  to_port           = 5432
  protocol          = "tcp"
  security_group_id = "${aws_security_group.backend_sg.id}"
  source_security_group_id = "${aws_security_group.database_sg.id}"
}

# Create security group rule
resource "aws_security_group_rule" "private_frontend_to_backend" {
  type              = "egress"
  from_port         = 8000
  to_port           = 8000
  protocol          = "tcp"
  security_group_id = "${aws_security_group.backend_sg.id}"
  source_security_group_id = "${aws_security_group.frontend_sg.id}"
}

# # Create security group rule
# resource "aws_security_group_rule" "frontend_to_world" {
#   type              = "egress"
#   from_port         = 8000
#   to_port           = 8000
#   protocol          = "tcp"
#   security_group_id = "${aws_security_group.backend_sg.id}"
#   source_security_group_id = "${aws_security_group.frontend_sg.id}"
# }

# # Create a security group for the backend service
# resource "aws_security_group" "backend_sg" {
#   vpc_id = aws_vpc.main.id

#   // Allow outgoing traffic to the database security group
#   egress {
#     from_port   = 0
#     to_port     = 65535  # Allow all ports for communication
#     protocol    = "tcp"
#     security_groups = [aws_security_group.database_sg.id]
#   }

#   // Allow incoming traffic from the frontend security group
#   ingress {
#     from_port   = 8000  # Example port for your backend service
#     to_port     = 8000
#     protocol    = "tcp"
#     security_groups = [aws_security_group.frontend_sg.id]
#   }

#   // Deny all other incoming traffic
#   ingress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   // Deny all other outgoing traffic
#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

# # Create a security group for the frontend service
# resource "aws_security_group" "frontend_sg" {
#   vpc_id = aws_vpc.main.id

#   // Allow incoming traffic from the Internet on HTTP port (frontend)
#   ingress {
#     from_port   = 80  # HTTP port
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   // Allow incoming traffic from the backend security group
#   ingress {
#     from_port   = 8000  # Example port for your backend service
#     to_port     = 8000
#     protocol    = "tcp"
#     security_groups = [aws_security_group.backend_sg.id]
#   }

#   // Deny all other incoming traffic
#   ingress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

# # Create an RDS PostgreSQL database
# resource "aws_db_instance" "database" {
#   // ...

#   // Configure the database to use the database security group
#   vpc_security_group_ids = [aws_security_group.database_sg.id]
# }

# Create a FastAPI backend
# resource "aws_ecs_task_definition" "backend_task" {
#   family                   = "backend-task"  # A unique name for the task definition
#   network_mode             = "awsvpc"        # Network mode for the task
#   requires_compatibilities = ["FARGATE"]     # Launch type

#   // Define the container(s) for the backend
#   container_definitions = jsonencode([
#     {
#       name  = "backend-container"
#       image = "your-backend-image-url"
#       memory = 256  # Specify memory allocation for the container (in MiB)
#       cpu    = 128  # Specify CPU units for the container
#     }
#   ])
# }

# resource "aws_ecs_task_definition" "frontend_task" {
#   family                   = "frontend-task"  # A unique name for the task definition
#   network_mode             = "awsvpc"        # Network mode for the task
#   requires_compatibilities = ["FARGATE"]     # Launch type

#   container_definitions = jsonencode([
#     {
#       name  = "frontend-container"
#       image = "your-frontend-image-url"
#       memory = 256  # Specify memory allocation for the container (in MiB)
#       cpu    = 128  # Specify CPU units for the container
#       // Add other container settings such as environment variables, ports, etc.
#     }
#   ])
# }
