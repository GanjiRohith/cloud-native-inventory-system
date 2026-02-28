import os
from pymongo import MongoClient

# MongoDB connection - use environment variable without defaults in production
mongo_uri = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017"  # Development default only
)

client = MongoClient(mongo_uri)

mongo_db = client.inventory