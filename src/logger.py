import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
log_file_path = os.path.join(logs_path, LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

# Configuración base del logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

# 🔁 También loguear a consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
logging.getLogger().addHandler(console_handler)

if __name__ == "__main__":
    logging.info("Logging has started")
