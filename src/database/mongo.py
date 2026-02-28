import os
from pymongo import MongoClient


# Read Mongo URI dynamically
MONGO_URI = os.environ.get(
    "MONGO_URI",
    "mongodb://localhost:27017/"
)

print("Using Mongo URI:", MONGO_URI)


# Create client
client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)


# Database
mongo_db = client.inventory


# Connection test
try:
    client.admin.command("ping")
    print("✅ MongoDB connected successfully")

except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")