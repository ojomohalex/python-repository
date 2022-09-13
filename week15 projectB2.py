"""
add 10 or more items to the table

Use boto3 and Python to scan the DynamoDB table.
"""


import boto3

client = boto3.resource('dynamodb') 
table = client.Table('Cars')# set client to variable

# adding 10 items to table
input1 = {'year': '2010', 
	'title': 'Toyota',
	'Color': 'White',}

response = table.put_item(Item=input1)


input2 = {'year': '2011',
	'title': 'Ford',
	'Color': 'red',}

response = table.put_item(Item=input2)

input3 = {'year': '2016',
	'title': 'Honda',
	'Color': 'Blue',}

response = table.put_item(Item=input3)


input4 = {'year': '2022',
	'title': 'Tesla',
	'Color': 'White',}

response = table.put_item(Item=input4)


input5 = {'year': '2021',
	'title': 'Sentra',
	'Color': 'green',}

response = table.put_item(Item=input5)

input6 = {'year': '2020',
	'title': 'Honda',
	'Color': 'black',}

response = table.put_item(Item=input6)


input7 = {'year': '2008',
	'title': 'Ford',
	'Color': 'White',}

response = table.put_item(Item=input7)


input8 = {'year': '2018',
	'title': 'Toyota',
	'Color': 'red',}

response = table.put_item(Item=input8)

input9 = {'year': '2016',
	'title': 'Chrysler',
	'Color': 'Blue',}

response = table.put_item(Item=input9)

input10 = {'year': '2019',
	'title': 'Jeep',
	'Color': 'red',}
	
response = table.put_item(Item=input10)
	

print(response)


