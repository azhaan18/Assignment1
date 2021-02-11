from decimal import Decimal
import boto3
import json

# puts data into DynamoDB

client = boto3.resource('dynamodb')
table = client.Table('yelp-restaurants')

data = []
with open('clean_data.json', 'r') as f:
	for line in f:
		data.append(json.loads(line, parse_float=Decimal))
	
count = 0
with table.batch_writer() as batch:
	for r in data:
		batch.put_item(Item=r)
		count += 1
		print(count, end='\r')