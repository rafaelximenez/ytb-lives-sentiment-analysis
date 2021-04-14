import requests
import config
import json

class Youtube:
    def __init__(self):
        self.video_id = config.VIDEO_ID
        self.api_key = config.API_KEY
        self.max_results = config.MAX_RESULTS

    def _get_live_data(self, url):
        r = requests.get(url)
        data = json.loads(r.text)
        return data["items"]

    def get_live_comments(self):
        url = f'{config.BASE_URL}/commentThreads?part=snippet%2Creplies&videoId={self.video_id}&key={self.api_key}&maxResults={self.max_results}'
        return self._get_live_data(url)

    def get_live_details(self):
        url = f'{config.BASE_URL}/videos?part=statistics,snippet&id={self.video_id}&key={self.api_key}&maxResults={self.max_results}'
        return self._get_live_data(url)