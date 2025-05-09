provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "rurax_bucket" {
    bucket = var.bucket_name
    force_destroy = true
}

resource "aws_sqs_queue" "rurax_queue_input" {
    name = var.sqs_queue_input
}

resource "aws_sqs_queue" "rurax_queue_output" {
    name = var.sqs_queue_output
}