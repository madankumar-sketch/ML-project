import os
import logging

from from_root import from_root


from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S_')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(logspath, exist_ok=True)

logging.basicConfig(

    filename=logs_path,
    # levelname like notificatins , info , debug
    format="[%(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
