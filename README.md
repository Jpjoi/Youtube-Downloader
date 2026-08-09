1. How do I get it working on my laptop?

When you get your MacBook, you clone the GitHub repository.

You'll need three things installed on the Mac:

Python
Git
FFmpeg

Then:

git clone https://github.com/Jpjoi/Youtube-Downloader.git

That creates a local copy of the project.

Then:

cd Youtube-Downloader

Install the Python dependencies:

pip install -r requirements.txt

And recreate your .env:

YOUTUBE_API_KEY=your_api_key_here

Remember, .env isn't on GitHub because we deliberately excluded it. That's good.

Then you should be able to run:

python main.py
After that, the workflow is beautiful

On your PC:

change code
↓
git add .
git commit -m "..."
git push

On your Mac:

git pull
↓
latest version

If you make changes on your Mac:

git add .
git commit -m "..."
git push

Then on your PC:

git pull

So the computers don't really "transfer files" to each other. They both synchronize through GitHub.
