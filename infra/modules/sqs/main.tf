resource "aws_sqs_queue" "rurax_queue" {
    name = var.queue_name  
}