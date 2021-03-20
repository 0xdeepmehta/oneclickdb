from datetime import datetime, timezone
from pydantic import BaseConfig, BaseModel
from typing import Dict
# # Base Model
# class RWModel(BaseModel):
#     class Config(BaseConfig):
#         allow_population_by_alias = True
#         json_encoders = {
#             datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
#             .isoformat()
#             .replace("+00:00", "Z")
#         }

# UserBucket Model
class UserInBucket(BaseModel):
    token: str
    payload: dict

class UserOutBucket(BaseModel):
    token: str
    keys: list