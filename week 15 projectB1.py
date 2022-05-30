"""
Create a DynamoDB table for something of your choosing 

"""
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #set client to a variable 


#invoke pthon to create a a table 
table = dynamodb.create_table(
    TableName='Cars',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10, #adding how many items the table will read
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)



