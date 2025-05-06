provider "aws" {
  region = var.aws_region
}

module "sqs_queue" {
  source = "./modules/sqs"
  queue_name = var.queue_name
}

module "s3_bucket" {
  source = "./modules/s3"
  bucket_name = var.bucket_name
}
