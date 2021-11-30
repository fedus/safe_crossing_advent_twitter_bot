import logging

from datetime import datetime

from sc_advent_bot.bot import get_todays_message
from sc_advent_bot.config import config

logging.basicConfig(encoding='utf-8')
logger = logging.getLogger(f"sc_advent_bot")
logger.setLevel(config.get("LOG_LEVEL", "INFO"))

def run() -> None:
    logger.info(f"Safe Crossing Advent Calendar bot started at {datetime.now()}")
    get_todays_message()
    logger.info(f"Run finished at {datetime.now()}")

if __name__ == "__main__":
    run()
