from pathlib import Path

import yt_dlp

from config import DOWNLOAD_FOLDER


def download_mp3(url):
    """
    Download the audio from a YouTube URL and convert it to MP3.

    Returns:
        Path to the resulting MP3 file.
    """

    output_template = str(
        DOWNLOAD_FOLDER / "%(title)s.%(ext)s"
    )

    options = {
        "format": "bestaudio/best",

        "outtmpl": output_template,

        "noplaylist": True,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],

        "quiet": False,

        "no_warnings": False,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)

    original_path = Path(
        ydl.prepare_filename(info)
    )

    mp3_path = original_path.with_suffix(".mp3")

    return mp3_path