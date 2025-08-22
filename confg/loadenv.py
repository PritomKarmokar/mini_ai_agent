import logging
import os
from dotenv import load_dotenv
from confg.logger import setup_logging

def load_env(env_path: str = None):
    """
    Load environment variables from .env file.
    If env_path is None, defaults to the .env in the project root.
    """
    setup_logging()  # Always setup logging first
    logger = logging.getLogger(__name__)

    # Determine .env path
    if env_path is None:
        base_dir = os.path.abspath(os.path.dirname(__file__))
        env_path = os.path.join(base_dir, "..", ".env")
        logger.info(f"ENV loaded from .env")

    if load_dotenv(dotenv_path=env_path):
        logger.info(f"ENV loaded from {env_path}")
    else:
        logger.warning(f"ENV NOT LOADED from {env_path}")
