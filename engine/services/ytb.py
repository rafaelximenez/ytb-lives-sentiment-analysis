import requests
import config
import json

def _get_live_data(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data["items"]

def get_live_comments():
    url = f'{config.BASE_URL}/commentThreads?part=snippet%2Creplies&videoId={config.VIDEO_ID}&key={config.API_KEY}&maxResults={config.MAX_RESULTS}'
    return _get_live_data(url)

def get_live_details():
    url = f'{config.BASE_URL}/videos?part=statistics,snippet&id={config.VIDEO_ID}&key={config.API_KEY}&maxResults={config.MAX_RESULTS}'
    return _get_live_data(url)