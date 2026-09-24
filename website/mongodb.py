import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load .env file
load_dotenv()

# Read values from .env
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("MONGODB_DATABASE")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)

db = client[DATABASE_NAME]

# Collections
profile = db["profile"]
skills = db["skills"]
projects = db["projects"]
education = db["education"]
contacts = db["contacts"]