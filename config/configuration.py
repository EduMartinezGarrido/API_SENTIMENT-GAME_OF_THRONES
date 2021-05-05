import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()


dburl = os.getenv("URL")

client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]

