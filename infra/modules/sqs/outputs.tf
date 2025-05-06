output "rurax_queue_url" {
  value = aws_sqs_queue.rurax_queue.name  
}

output "rurax_queue_arn" {
  value = aws_sqs_queue.rurax_queue.arn
}