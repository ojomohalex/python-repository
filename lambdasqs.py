import boto3

sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='Lambda_SQS')
print(queue.url)