import googleapiclient.discovery
import csv
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from textblob import TextBlob   
import re 
# Set API_KEY to your API key
API_KEY = 'AIzaSyAiYZ5ozz_rwKHW0FL8UH89yRN-YRzGYMw'

# create a youtube service object
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)


# Add your list of video links here
with open("links.txt", "r") as file:
    links_list = file.read().split("\n")


# create the CSV file and write the headers
with open('comments.csv', mode='w', newline='', errors='replace') as csv_file:
    fieldnames = ['Comments', 'Month', 'Link', 'Sentiment', 'Video title']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for link in links_list:
        # extract the video id from the link
        # video_id = parse_qs(urlparse(link).query)['v'][0]
        video_id = re.search("(?<=v=)[^&#]+", link).group(0)
        # call the comments.list method to get the comments
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
        )
        response = request.execute()

        # print the comments, dates, and video title
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            date = datetime.strptime(item['snippet']['topLevelComment']['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            month = date.strftime("%y-%b")
            sentiment_score = TextBlob(comment).sentiment.polarity
            if sentiment_score > 0:
                sentiment = 'positive'
            elif sentiment_score == 0:
                sentiment = 'neutral'
            else:
                sentiment = 'negative'
            # get the video title
            video_request = youtube.videos().list(
                part='snippet',
                id=video_id
            )
            video_response = video_request.execute()

            video_title = video_response['items'][0]['snippet']['title']
            # write the data to the CSV file
            writer.writerow({'Comments': comment, 'Month': month, 'Link':link, 'Sentiment': sentiment, 'Video title': video_title})