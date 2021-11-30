import logging

from yaml import safe_load, YAMLError
from string import Template

from sc_advent_bot.config import config

logger = logging.getLogger(f"sc_advent_bot.{__name__}")

def get_message_for(index: int) -> str:
    with open(config.get("MESSAGES_FILE"), "r") as stream:
        try:
            return Template(safe_load(stream)[index]).substitute(day=index)
        except IndexError as ex:
            raise NoMessageForIndexException

class NoMessageForIndexException(Exception):
    pass