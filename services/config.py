import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_URL = os.getenv("BOT_URL")
OWNER_ID = os.getenv("OWNER_ID")
GROUP_ID = os.getenv("GROUP_ID")
NLP_KEY = os.getenv("NLP_KEY")
GROUP_URL = os.getenv("GROUP_URL")