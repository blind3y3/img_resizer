import sys
from dotenv import load_dotenv
from src.image_downloader import ImageDownloader

load_dotenv()

try:
    downloader = ImageDownloader(sys.argv[1])
    downloader.get_youtube_video_id().get_youtube_title().save_thumbnail_by_name()
except IndexError:
    print('Please insert correct youtube url')
    exit(1)
