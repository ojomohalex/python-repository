import boto3
client = boto3.resource('dynamodb') 
table = client.Table('Cars')#

from boto3.dynamodb.conditions import Key #query items based on year
response = table.query(
    TableName= 'Cars',
    KeyConditionExpression= Key('year').eq('2016')
)


print(response)

 