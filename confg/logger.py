# confg/logger.py
import logging
import logging.config
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LOGGER_ROOT_NAME = os.getenv("LOGGER_ROOT_NAME", "upms_add_money")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()

# Reduce verbosity in production
if ENVIRONMENT == "production":
    LOG_LEVEL = "WARNING"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[{asctime} | {levelname} | {pathname}:{lineno}] {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "level": LOG_LEVEL,
        },
    },
    "loggers": {
        "general": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": True,
        },
        LOGGER_ROOT_NAME: {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": True,
        },
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING)
