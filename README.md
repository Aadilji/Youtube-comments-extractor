# Youtube-comments-extractor

1. The code imports necessary libraries such as googleapiclient.discovery, csv, datetime, urlparse, parse_qs, textblob and re.
2. It sets the API key for the YouTube Data API v3, which is required to access the YouTube API.
3. It creates a YouTube service object, which is used to make requests to the API.
4. It reads links from a file called links.txt and split each link by newline.
5. It creates a CSV file called comments.csv and writes the headers to it.
6. It loops through the links, and for each link, it extracts the video id using the re library.
7. It makes a request to the YouTube API to get the comments of the video using the extracted video id.
8. It loops through the comments and gets the sentiment of each comment using the textblob library, classifying it as "positive", "negative" or "neutral"
9. It gets the title of the video using the extracted video id from the video response from the YouTube API.
10. It writes the comments, month, link, sentiment and video title to the CSV file for each comment.
