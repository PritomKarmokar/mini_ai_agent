import logging
import os
from dotenv import load_dotenv
from confg.logger import setup_logging

def load_env(env_path: str = None):
    """
    Load environment variables from .env file.
    If env_path is None, defaults to the .env in the project root.
    """
    setup_logging()
    logger = logging.getLogger(__name__)

    if env_path is None:
        base_dir = os.path.abspath(os.path.dirname(__file__))
        env_path = os.path.join(base_dir, "..", ".env")

    if load_dotenv(dotenv_path=env_path):
        logger.info(f"ENV loaded from {env_path}")
    else:
        logger.warning(f"ENV NOT LOADED from {env_path}")

    return {
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
        "WEATHER_INFO_URL": os.getenv("WEATHER_INFO_URL"),
        "GEOCODE_FETCH_URL": os.getenv("GEOCODE_FETCH_URL"),
    }

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WEATHER_INFO_URL = os.getenv("WEATHER_INFO_URL")
GEOCODE_FETCH_URL = os.getenv("GEOCODE_FETCH_URL")
