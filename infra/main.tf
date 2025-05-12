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