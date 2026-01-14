
# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://rahuldutta_db_user:Admin123@cluster0.qtmmo6m.mongodb.net/?appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)



from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://ghangadhar6_db_user:Admin123@cluster0.n3meooi.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
