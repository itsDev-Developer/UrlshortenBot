# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23267035"))
API_HASH = os.environ.get("API_HASH", "a516af48bca80b9f339980650126149c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6332894117:AAEitpZdPorLOBONhgF-kdnrKX3HLww3jlk")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "5729587090").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://animebot:animesdkbot@cluster0.cybneuo.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5729587090")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "App4Earn") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"
