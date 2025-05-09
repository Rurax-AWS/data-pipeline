output "rurax_bucket_name" {
    value = aws_s3_bucket.rurax_bucket.bucket  
}

output "rurax_queue_input_url" {
    value = aws_sqs_queue.rurax_queue_input.id  
}

output "rurax_queue_input_arn" {
    value = aws_sqs_queue.rurax_queue_input.arn    
}

output "rurax_queue_output_url" {
    value = aws_sqs_queue.rurax_queue_output.id  
}

output "rurax_queue_output_arn" {
    value = aws_sqs_queue.rurax_queue_output.arn    
}