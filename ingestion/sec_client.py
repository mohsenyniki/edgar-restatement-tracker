import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


class SECError(Exception):
    """SEC couldn't give us the data (network problem or an error response)."""

# normalize the CIK to 10 digits, and validate it
def normalize_cik(raw):
    """Validate a CIK and zero-pad it to 10 digits."""
    if not raw.isdigit():
        raise ValueError(f"The input {raw} is not a valid CIK. CIK must be a number.")
    if len(raw) > 10:
        raise ValueError(f"The input {raw} is too long. CIK must be at most 10 digits long.")

    # pad it to 10 digits starting with 0s
    return raw.zfill(10)


def get_user_agent():
    """Read SEC_USER_AGENT from the environment (.env locally)."""
    load_dotenv()
    user_agent = os.getenv("SEC_USER_AGENT")
    if not user_agent:
        raise ValueError("SEC_USER_AGENT is not set in the .env file. Please set it to your name and email.")
    return user_agent


def fetch_json(url, user_agent):
    """GET a JSON document from SEC and return it as a dict."""
    headers = {"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"}

    # network failures (no internet, timeout) raise an exception instead of returning a status code
    try:
        response = requests.get(url, headers=headers, timeout=30)
    except requests.exceptions.RequestException as e:
        raise SECError(f"Network error while contacting SEC: {e}. Try again.") from e

    # SEC answered, but maybe not with the data
    if response.status_code == 403:
        raise SECError("SEC refused the request (403). Check SEC_USER_AGENT in .env.")
    if response.status_code == 404:
        raise SECError(f"Nothing found at {url} (404). Check the CIK.")
    if response.status_code != 200:
        raise SECError(f"Unexpected response from SEC: {response.status_code}.")

    return response.json()


def save_json(data, out_path):
    """Save a dict as JSON to a file."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(data, f)
    
    return out_path