from pymongo import MongoClient

# Connect to MongoDB running in Docker container
client = MongoClient('mongodb://admin:yourpassword@localhost:27017/')

# List all databases
print(client.list_database_names())