from __future__ import annotations

import os
import bs4
import requests


class ImageDownloader:
    _youtube_url = ''
    _video_id = ''
    _title = ''

    def __init__(self, youtube_url):
        self._youtube_url = youtube_url

    def get_youtube_video_id(self) -> ImageDownloader:
        watch_string = self._youtube_url.split('/')[:1:-2][0]
        video_id_string = watch_string.split('=')[1]
        self._video_id = video_id_string
        return self

    def get_youtube_title(self) -> ImageDownloader:
        response = requests.get(self._youtube_url)
        html = bs4.BeautifulSoup(response.text, features="lxml")
        title = html.title.text
        clean_title = '-'.join(title.split('-')[:-1]).strip()
        self._title = clean_title
        return self

    def save_thumbnail_by_name(self) -> None:
        response = requests.get(f"https://img.youtube.com/vi/{self._video_id}/maxresdefault.jpg")
        if not os.path.exists(os.getenv('OUTPUT_PATH')):
            os.mkdir(os.getenv('OUTPUT_PATH'))

        with open(f"{os.getenv('OUTPUT_PATH')}/{self._title}.jpg", 'wb') as f:
            f.write(response.content)
            f.close()
