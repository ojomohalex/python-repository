"""
Create a DynamoDB table for something of your choosing 

add 10 or more items to the table

Use boto3 and Python to scan the DynamoDB table.

"""
import boto3

table = boto3.client("dynamodb", region_name='us-east-1')

Game = table.create_table(TableName='Game',
        KeySchema=[
            {'AttributeName': 'Title','KeyType': 'HASH'},  # Partition Key
            
            {'AttributeName': 'Genre','KeyType': 'RANGE'}],  # Sort Key
        
            AttributeDefinitions=[
                {'AttributeName': 'Title','AttributeType': 'N'},
                
                {'AttributeName': 'Genre','AttributeType': 'S'}
            ],
            
            ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10}
            )
print(Game)





