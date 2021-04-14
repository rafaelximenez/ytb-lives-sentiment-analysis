from engine.services.sentiment_analysis import GNaturalLanguage
from engine.services.ytb                import Youtube
import pandas as pd
import re

scores = []
magnitudes = []
comments = []
video_ids = []

class Lives:
    def __init__(self):
        self.gnlp = GNaturalLanguage()
        self.ytb = Youtube()

    def handle_live_data(self):
        for x in self.ytb.get_live_comments():
            comment = x["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            video_id = x["snippet"]["videoId"]
            cleanr = re.compile('<.*?>')
            clean_comment = re.sub(cleanr, '', comment)
            score, magnitude = self.gnlp.sentiment_analysis(clean_comment)
            
            scores.append(score)
            magnitudes.append(magnitude)
            comments.append(clean_comment)
            video_ids.append(video_id)

        live_details_complete_data = self.ytb.get_live_details()
        live_details_data = live_details_complete_data[0]["snippet"]

        live_video_id = live_details_complete_data[0]["id"]
        live_title = [live_details_data["title"]]
        live_description = [live_details_data["description"]]
        live_channel_id = [live_details_data["channelId"]]
        live_img = [live_details_data["thumbnails"]["medium"]["url"]]

        df_live_details = pd.DataFrame({
            "video_id": live_video_id,
            "title": live_title,
            "description": live_description,
            "channel_id": live_channel_id,
            "url_image": live_img,
        })

        df_comments = pd.DataFrame({
            "video_id": video_ids,
            "comments": comments,
            "scores": scores,
            "magnitudes": magnitudes,
        })
        print(df_live_details)
        print(df_comments)