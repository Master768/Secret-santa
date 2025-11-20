import os
from motor.motor_asyncio import AsyncIOMotorClient

# Default to localhost if not specified
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = "secret_santa_db"

class Database:
    client: AsyncIOMotorClient = None
    db = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.db = self.client[DB_NAME]
        print(f"Connected to MongoDB at {MONGO_URL}")

    def close(self):
        if self.client:
            self.client.close()
            print("Disconnected from MongoDB")

db = Database()
