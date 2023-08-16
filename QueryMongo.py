import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# Create a database and collection
mydb = client['Store']
products = mydb.products

# Insert a single document
product_record = {
    'name': 'Smartphone',
    'category': 'Electronics',
    'price': 599.99,
    'stock': 50
}
products.insert_one(product_record)

# Insert multiple documents
product_records = [
    {
        'name': 'Laptop',
        'category': 'Electronics',
        'price': 1299.99,
        'stock': 25
    },
    {
        'name': 'Book',
        'category': 'Stationery',
        'price': 14.99,
        'stock': 100
    },
    {
        'name': 'Headphones',
        'category': 'Electronics',
        'price': 79.99,
        'stock': 30
    }
]
products.insert_many(product_records)

# Simple way of querying - Find a single document
print(products.find_one())

# Select * from products - Find all documents
for product in products.find({}):
    print(product)

# Query documents based on equality conditions - Find products with category 'Electronics'
for product in products.find({'category': 'Electronics'}):
    print(product)

# Query documents using query operators - Find products with price less than $100
for product in products.find({'price': {'$lt': 100}}):
    print(product)

# AND and Query operators - Find electronics products with price less than $100
for product in products.find({'category': 'Electronics', 'price': {'$lt': 100}}):
    print(product)

# OR operators - Find products with category 'Electronics' or price less than $100
for product in products.find({'$or': [{'category': 'Electronics'}, {'price': {'$lt': 100}}]}):
    print(product)

# Inventory collection
inventory = mydb.inventory

# Insert inventory documents
inventory_records = [
    {
        'item': 'pen',
        'qty': 200,
        'size': {'h': 10, 'w': 1, 'uom': 'cm'},
        'status': 'A'
    },
    {
        'item': 'notebook',
        'qty': 100,
        'size': {'h': 20, 'w': 15, 'uom': 'cm'},
        'status': 'A'
    },
    {
        'item': 'pencil',
        'qty': 150,
        'size': {'h': 10, 'w': 0.5, 'uom': 'cm'},
        'status': 'D'
    }
]
inventory.insert_many(inventory_records)

# Find inventory items with size: {'h': 10, 'w': 1, 'uom': 'cm'}
for item in inventory.find({'size': {'h': 10, 'w': 1, 'uom': 'cm'}}):
    print(item)
