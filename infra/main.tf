provider "aws" {
  profile = var.aws_profile
  region = var.aws_region
}

resource "aws_s3_bucket" "rurax_bucket" {
    bucket = var.bucket_name
    force_destroy = true
}

resource "aws_sqs_queue" "rurax_queue" {
    name = var.sqs_queue
}

resource "aws_security_group" "rds_sg" {
  name        = "rds_sg_temp_test"
  description = "Allow all to Postgres temporarily"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # aberto para o mundo, cuidado
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

data "aws_vpc" "default" {
  default = true
}

resource "aws_db_instance" "rurax_postgres" {
  identifier              = "rurax-test-temp"
  engine                  = "postgres"
  instance_class          = "db.t3.micro"
  allocated_storage       = 20
  db_name                 = var.db_name
  username                = var.db_user
  password                = var.db_password
  port                    = 5432
  publicly_accessible     = true
  skip_final_snapshot     = true

  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
}

resource "null_resource" "init_db_schema" {
  depends_on = [aws_db_instance.rurax_postgres]

  provisioner "local-exec" {
    command = <<EOT
PGPASSWORD="${var.db_password}" psql \
  --host=${aws_db_instance.rurax_postgres.address} \
  --port=5432 \
  --username=${var.db_user} \
  --dbname=${var.db_name} \
  --file=../init.sql
EOT
  }
}
