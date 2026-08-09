from youtube_search import search_youtube
from downloader import download_mp3


def main():
    print()
    print("=" * 50)
    print("           YouTube → MP3 Downloader")
    print("=" * 50)
    print()

    query = input("What do you want to download? ").strip()

    if not query:
        print("You didn't enter anything.")
        return

    print()
    print(f'Searching YouTube for: "{query}"...')
    print()

    try:
        result = search_youtube(query)
    except Exception as e:
        print("YouTube search failed.")
        print(f"Error: {e}")
        return

    if result is None:
        print("No YouTube videos were found.")
        return

    print("Found:")
    print()
    print(f"  Title:   {result['title']}")
    print(f"  Channel: {result['channel']}")
    print(f"  URL:     {result['url']}")
    print()

    confirmation = input("Download this? [Y/n]: ").strip().lower()

    if confirmation not in ("", "y", "yes"):
        print("Cancelled.")
        return

    print()
    print("Downloading...")
    print()

    try:
        path = download_mp3(result["url"])
    except Exception as e:
        print()
        print("Download failed.")
        print(f"Error: {e}")
        return

    print()
    print("=" * 50)
    print("Download complete!")
    print("=" * 50)
    print()
    print(f"Saved to:")
    print(path.resolve())
    print()


if __name__ == "__main__":
    main()