import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Explicitly specify the path to your .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path)
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGO_DB")

print(f"[DEBUG] MONGO_URI being used: '{mongo_uri}'")  # Debug print

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db.ticket_summaries

def insert_ticket_summaries(csv_path):
    df = pd.read_csv(csv_path)

    records = df.to_dict(orient="records")
    collection.delete_many({})  # Clear old data
    result = collection.insert_many(records)
    
    print(f"✅ Inserted {len(result.inserted_ids)} ticket summaries into MongoDB")

def show_sample(limit=5):
    for doc in collection.find().limit(limit):
        print(doc)

def upsert_cluster_label(cluster_id, label):
    labels_col = db.cluster_labels
    labels_col.update_one({"cluster": cluster_id}, {"$set": {"label": label}}, upsert=True)

def get_all_labels():
    labels_col = db.cluster_labels
    return {doc["cluster"]: doc["label"] for doc in labels_col.find()}


# Example usage
if __name__ == "__main__":
    insert_ticket_summaries("data/summarized_tickets.csv")
    show_sample()
