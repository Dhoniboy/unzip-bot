# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL"))
    MONGODB_URL = os.environ.get("MONGODB_URL")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 5 # 5 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
