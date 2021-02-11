import json

# gets business_id and cuisine for elasticsearch

data = []
with open('clean_data.json', 'r') as f:
	for line in f:
		data.append(json.loads(line))

indexes = []
clean_data = []
for d in data:
	business_id = d['business_id']
	cuisine = d['cuisine']
	clean_data.append({'business_id': business_id, 'cuisine': cuisine})

with open('es_data.json', 'w') as f:
	for d in clean_data:
		f.write(json.dumps({'index': {'_index': 'restaurants', '_id': d['business_id']}}) + '\n')
		f.write(json.dumps({'cuisine': d['cuisine']}) + '\n')