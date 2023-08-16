from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client['School']

# Access collection of the database
collection = mydatabase['studentscores']

# Delete a single document
result = collection.delete_one({"user": "Alice", "subject": "Math"})
print("Deleted count:", result.deleted_count)

# Delete multiple documents
result = collection.delete_many({"user": "Bob"})
print("Deleted count:", result.deleted_count)

# Print remaining documents in the collection
for document in collection.find():
    print(document)
