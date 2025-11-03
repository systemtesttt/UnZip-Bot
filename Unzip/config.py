import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8566938243:AAHI0OvVU1opM_b1eNQN7kOQ-8m07OO1xDw")
    API_ID = int(os.environ.get("API_ID", "14029127"))
    API_HASH = os.environ.get("API_HASH", "72cac79d6c73536769b2f5ed08cebe4f")
    MAX_FILE_SIZE = 2194304000
    
    
