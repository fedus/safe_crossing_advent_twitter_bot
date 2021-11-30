import logging
from pytz import timezone

from datetime import datetime
from string import Template

from sc_advent_bot.config import config
from sc_advent_bot.message_service import get_message_for, NoMessageForIndexException
from sc_advent_bot.tweet_service import tweet_service

logger = logging.getLogger(f"sc_advent_bot.{__name__}")

def get_todays_message():
    now_lux = timezone("Europe/Luxembourg").localize(datetime.utcnow())
    current_day = now_lux.day
    current_day_index = current_day - 1

    logger.debug(f"Current day: {current_day}, current day index: {current_day_index}")

    try:
        message = f"{build_url_for_day(current_day)} {get_message_for(current_day_index)}"
        logger.debug(f"Final message: {message}")
    except NoMessageForIndexException:
        logger.warn(f"No message found for day {current_day}, aborting.")
        return
    except Exception as e:
        logger.error(f"Failed while loading messages, aborting.", exc_info=True)
        return

    try:
        logger.debug("Attempting to tweet")
        tweet_service.tweet_thread(message)
    except Exception as e:
        logger.error(f"Error while tweeting!", exc_info=True)

def build_url_for_day(day: int) -> str:
    return Template(config.get("CALENDAR_URL_TEMPLATE")).substitute(day=day)