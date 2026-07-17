from dotenv import load_dotenv
import os
import logging
from app.log_config import configurarLogs
load_dotenv()
configurarLogs()
logger = logging.getLogger(__name__)
tokemBotTelegram = os.getenv("TOKEM_TELEGRAM")
idChatTelegram = os.getenv("ID_CHAT_TELEGRAM")
DBPath=os.getenv("DB_PATH")
logPath=os.getenv("LOG_PATH")