from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Portfolio database
db = client["portfolio_db"]

# Collections
profile = db["profile"]
skills = db["skills"]
projects = db["projects"]
education = db["education"]
contacts = db["contacts"]