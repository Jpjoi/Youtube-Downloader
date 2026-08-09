import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

DOWNLOAD_FOLDER = Path("downloads")

if not YOUTUBE_API_KEY:
    raise RuntimeError(
        "YOUTUBE_API_KEY is missing. "
        "Put it in your .env file."
    )

DOWNLOAD_FOLDER.mkdir(exist_ok=True)