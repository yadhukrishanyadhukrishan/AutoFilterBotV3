import re
import base64
import logging
from struct import pack
from pyrogram.errors import UserNotParticipant
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
import os
import PTN
import requests
import json
from Config import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME, USE_CAPTION_FILTER, AUTH_CHANNEL, API_KEY
DATABASE_URI_2=os.environ.get('DATABASE_URI_2', DATABASE_URI)
DATABASE_NAME_2=os.environ.get('DATABASE_NAME_2', DATABASE_NAME)
COLLECTION_NAME_2="Posters"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance.from_db(db)

IClient = AsyncIOMotorClient(DATABASE_URI_2)
imdbdb=client[DATABASE_NAME_2]
imdb=Instance.from_db(imdbdb)

@instance.register
class Media(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField(allow_none=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)

class Meta:
        collection_name = COLLECTION_NAME


