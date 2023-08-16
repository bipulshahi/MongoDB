import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# Create a database and collection
mydb = client['ArtSupplies']
inventory = mydb.inventory

# Insert multiple documents
inventory_items = [
    {"item": "paintbrushes",
     "qty": 150,
     "size": {"h": 15, "w": 1.5, "uom": "cm"},
     "status": "A"},
    {"item": "canvas",
     "qty": 75,
     "size": {"h": 50, "w": 70, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 100,
     "size": {"h": 21, "w": 29.7, "uom": "cm"},
     "status": "A"},
    {"item": "erasers",
     "qty": 50,
     "size": {"h": 3, "w": 2, "uom": "cm"},
     "status": "P"},
    # ... additional items ...
]
inventory.insert_many(inventory_items)

# Update a document - sketch pad
inventory.update_one(
    {"item": "sketchbook"},
    {"$set": {"size.uom": "m", "status": "P"},
     "$currentDate": {"lastModified": True}}
)

# Update multiple documents - items with quantity less than 50
inventory.update_many(
    {"qty": {"$lt": 50}},
    {"$set": {"size.uom": "in", "status": "P"},
     "$currentDate": {"lastModified": True}}
)

# Replace a document - paper with warehouses
inventory.replace_one(
    {"item": "paper"},
    {"item": "paper",
     "instock": [
         {"warehouse": "C", "qty": 70},
         {"warehouse": "D", "qty": 55}]}
)
