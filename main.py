from typing import Optional
import logging
from fastapi import FastAPI, Depends
from models import UserInBucket, UserOutBucket
import pymongo
from mongodb_utils import startup_event,shutdown_event
from mongodb import AsyncIOMotorClient, get_database

app = FastAPI(title="OneClick DB API")
#Adding a controll to start and stop mongodb connection
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

database_name = "oneclick-db"
collection_name = "user_data"

@app.post("/")
async def storeUserPayload(payload: UserInBucket, db: AsyncIOMotorClient = Depends(get_database)):
    print(payload.dict())
    if type(payload.dict()["payload"]) == dict:
        ext_resp = await db[database_name][collection_name].find_one_and_update({'token': payload.dict()["token"]}, { '$set': payload.dict()})
        if ext_resp == None:
            new_resp = await db[database_name][collection_name].insert_one(payload.dict())
            if new_resp != None:
                status = "201"
                message = "Saved Successfuly"

            else:
                status = "504"
                message = "Internal Server Error"
        else:
            status = "201"
            message = "Saved Successfully"
    return {'status':status, 'message': message}

@app.get("/{token}")
async def giveUserPayload(token: str, keys:str = None, db: AsyncIOMotorClient = Depends(get_database)):
    if keys == None:
        response = await db[database_name][collection_name].find_one({'token': token})
        status = "200"
        message = response["payload"]
    else:
        response = await db[database_name][collection_name].find_one({'token': token})
        print(response)
        print(type(response))
        try:
            key_val = response["payload"][keys]
            status = "200"
            message = {keys: key_val}
        except KeyError as e:
            status = "404"
            message = "Key not not"
    return {'status': status, 'response': message}