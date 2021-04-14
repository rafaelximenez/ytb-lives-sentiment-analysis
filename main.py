from engine.services.sentiment_analysis import *
from engine.services.ytb                import *
import pandas as pd
import re

scores = []
magnitudes = []
comments = []
video_ids = []

for x in get_live_comments():
    comment = x["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    video_id = x["snippet"]["videoId"]
    cleanr = re.compile('<.*?>')
    clean_comment = re.sub(cleanr, '', comment)
    score, magnitude = sentiment_analysis(clean_comment)
    
    scores.append(score)
    magnitudes.append(magnitude)
    comments.append(clean_comment)
    video_ids.append(video_id)

live_details_complete_data = get_live_details()
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

'''df_live_details.to_csv('live_details.csv', sep=";")
df_comments.to_csv('comments.csv', sep=";")
print(df_comments)
print(df_live_details)'''