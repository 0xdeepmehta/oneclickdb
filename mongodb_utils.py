import logging

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from mongodb import db


async def startup_event():
    print("[INFO] Connnecting to MongoDB")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT,
                                   maxIdleTimeMS=5000)
    print("[INFO] MongoDB connected！")


async def shutdown_event():
    print("===========")
    print("[INFO] Disconnecting mongoDB connection...")
    db.client.close()
    print("[INFO] MongoDB Connection closed！")