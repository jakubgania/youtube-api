from googleapiclient.discovery import build
from dotenv import load_dotenv
import json
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_channel_statistics(username = None, channel_id = None):
    if username:
        reuqest = youtube.channels().list(
            part='statistics',
            forUsername=username
        )

        response = reuqest.execute()

        if response['pageInfo']['totalResults'] == 0:
            return f"No channel found for username '{username}'."
        
        return response
    elif channel_id:
        request = youtube.channels().list(
            part='statistics',
            id=channel_id
        )

        response = request.execute()

        if response['pageInfo']['totalResults'] == 0:
            return f"No channel found for channel ID '{channel_id}.'"
        
        return response
    else:
        return "Provide a username or channel ID."
    
# request for channel name github
username = "github"
response = get_channel_statistics(username=username)
print(json.dumps(response, sort_keys=True, indent=4))

# request for github channel id
channel_id="UC7c3Kb6jYCRj4JOHHZTxKsQ"
response = get_channel_statistics(channel_id=channel_id)
print(json.dumps(response, sort_keys=True, indent=4))