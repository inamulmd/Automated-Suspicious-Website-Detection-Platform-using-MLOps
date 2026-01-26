from pymongo.mongo_client import MongoClient

uri ="mongodb+srv://inamulmd:Inamul123@cluster0.4b1dldv.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("✅ Connected to MongoDB Atlas successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
