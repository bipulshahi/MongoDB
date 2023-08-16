from pymongo import MongoClient
import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client['School']

# Access collection of the database
collection = mydatabase['studentscores']

# Insert sample data
data = [
    {"user": "Alice", "subject": "Math", "score": 80},
    {"user": "Bob", "subject": "Science", "score": 90},
    {"user": "Alice", "subject": "Science", "score": 85},
    {"user": "Bob", "subject": "Math", "score": 75},
    {"user": "Alice", "subject": "History", "score": 60},
    {"user": "Bob", "subject": "History", "score": 95}
]
collection.insert_many(data)

# Group and count subjects for each user
agg_result = collection.aggregate([
    {
        "$group":
            {
                "_id": "$user",
                "Total Subjects": {"$sum": 1}
            }
    }
])
for i in agg_result:
    print(i)

# Group and calculate total marks for each user
agg_result = collection.aggregate([
    {
        "$group":
            {
                "_id": "$user",
                "Total Marks": {"$sum": "$score"}
            }
    }
])
for i in agg_result:
    print(i)

# Group and calculate average score for each user
agg_result = collection.aggregate([
    {
        "$group":
            {
                "_id": "$user",
                "Average Score": {"$avg": "$score"}
            }
    }
])
for i in agg_result:
    print(i)

# Create a new collection
data = [
    {"item": "pen", "price": 10, "quantity": 5, "date": datetime.datetime.utcnow()},
    {"item": "pencil", "price": 5, "quantity": 10, "date": datetime.datetime.utcnow()},
    {"item": "notebook", "price": 20, "quantity": 3, "date": datetime.datetime.utcnow()}
]
collection = mydatabase['sales']
collection.insert_many(data)

# Group and calculate average price and quantity for each item
agg_result = collection.aggregate([
    {
        "$group":
            {
                "_id": "$item",
                "Avg Price": {"$avg": "$price"},
                "Avg Quantity": {"$avg": "$quantity"}
            }
    }
])
for i in agg_result:
    print(i)

# Create a new collection for books
data = [
    {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "copies": 5},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "copies": 10},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 3}
]
collection = mydatabase['books']
collection.insert_many(data)

# Project only title and author fields
for row in collection.aggregate([{"$project": {"title": 1, "author": 1}}]):
    print(row)
