import json
import requests
from typing import Optional, Tuple

# logger = logging.getLogger("general")
session = requests.Session()
ResponseType = Tuple[Optional[dict], int]

def get_json(url: str, **kwargs) -> ResponseType:
    """Send a GET request to `url` and parse response as json"""
    # logger.debug(f">>>>>> GET {url}")
    # kwargs.setdefault("timeout", settings.REQUEST_TIMEOUT)
    try:
        with session:
            response = session.get(url, **kwargs)
    except (requests.ConnectionError, requests.Timeout) as e:
        # logger.error(f"GET request failed for {url}: {e!r}")
        return None, 500

    try:
        return json.loads(response.text), response.status_code
    except json.JSONDecodeError as e:
        # logger.error(f"GET request for {url} response parsing failed: {e!r}")
        return None, 500

def post_json(url: str, payload: Optional[dict] = None, **kwargs) -> ResponseType:
    """
    Send a POST request to `url` with `payload` as json and parse response as json
    """
    # logger.debug(f">>>>>> POST {url}")
    # kwargs.setdefault("timeout", settings.REQUEST_TIMEOUT)
    try:
        with session:
            response = session.post(url, json=payload, **kwargs)
    except (requests.ConnectionError, requests.Timeout) as e:
        # logger.error(f"POST request failed for {url}: {e!r}")
        return None, 500

    try:
        return json.loads(response.text), response.status_code
    except json.JSONDecodeError as e:
        # logger.error(f"POST request for {url} response parsing failed: {e!r}")
        return None, 500