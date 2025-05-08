output "rurax_bucket_name" {
    value = aws_s3_bucket.rurax_bucket.bucket  
}

output "rurax_queue_url" {
    value = aws_sqs_queue.rurax_queue.id  
}

output "rurax_queue_arn" {
    value = aws_sqs_queue.rurax_queue.arn    
}