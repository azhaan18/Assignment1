import json
from decimal import Decimal

# cleans yelp dataset and generate info we need

data = []
with open('yelp_academic_dataset_business.json', 'r') as f:
	for line in f:
		data.append(json.loads(line))

# business_id, name, address, coords, # of reviews, ratin, zip code
cuisines = {'Chinese': 0, 'Japanese': 0, 'American': 0, 'Italian': 0, 'Mexican': 0, 'Vietnamese': 0}

count = 0
n = len(data)
clean_data = []
for d in data:
	count += 1
	print("{}/{}".format(count, n), end='\r')
	in_target = False
	if not d['categories'] or 'Restaurants' not in d['categories']:
		continue
	for cuisine in cuisines.keys():
		if cuisine in d['categories']:
			in_target = True
			cuisines[cuisine] += 1
			c = cuisine
			break
	if not in_target:
		continue

	business_id = d['business_id']
	name = d['name']
	address = d['address']
	city = d['city']
	state = d['state']
	latitude = d['latitude']
	longitude = d['longitude']
	rating = d['stars']
	review_count = d['review_count']
	zip_code = d['postal_code']
	business = {'business_id': business_id, 'name': name, 'address': address, 'city': city, 'state': state, 'latitude': latitude, 'longitude': longitude, 'cuisine': c, 'rating': rating, 'review_count': review_count, 'zip_code': zip_code}
	clean_data.append(business)

print(cuisines)

with open('clean_data.json', 'w') as f:
	for d in clean_data:
		f.write(json.dumps(d) + '\n')
