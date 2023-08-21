from pymongo import MongoClient

# Connect to MongoDB running in Docker container
client = MongoClient('mongodb://admin:yourpassword@localhost:27017/')

# Use a database named "testdb". If it doesn't exist, this will automagically create it for you. <3. 
db = client['testdb']

# Use a collection named "testcollection"
collection = db['testcollection']

# 1. Adding Data:
# Insert a single document
doc = {"name": "John", "age": 30, "city": "New York"}
inserted_id = collection.insert_one(doc).inserted_id
print(f"Inserted document with ID: {inserted_id}")

# Insert multiple documents
docs = [
    {"name": "Anna", "age": 25, "city": "London"},
    {"name": "Mike", "age": 32, "city": "Chicago"}
]
inserted_ids = collection.insert_many(docs).inserted_ids
print(f"Inserted documents with IDs: {inserted_ids}")

# 2. Fetching Data:
# Fetch a single document
john_data = collection.find_one({"name": "John"})
print(f"Fetched data for John: {john_data}")

# Fetch multiple documents
all_data = collection.find()
print("Fetched all data:")
for data in all_data:
    print(data)

# 3. Updating Data:
# Update a single document
update_criteria = {"name": "John"}
new_values = {"$set": {"city": "Los Angeles"}}
collection.update_one(update_criteria, new_values)
print("Updated John's city to Los Angeles")

# Update multiple documents
update_criteria_multi = {"age": {"$gt": 30}}
new_values_multi = {"$set": {"status": "senior"}}
collection.update_many(update_criteria_multi, new_values_multi)
print("Updated status to 'senior' for everyone older than 30")

# 4. Deleting Data:
# Delete a single document
delete_criteria = {"name": "Mike"}
collection.delete_one(delete_criteria)
print("Deleted Mike's record")

# Delete multiple documents
delete_criteria_multi = {"age": {"$lt": 30}}
collection.delete_many(delete_criteria_multi)
print("Deleted records of everyone younger than 30")

# Close the connection
client.close()
