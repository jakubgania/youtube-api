from googleapiclient.discovery import build
from dotenv import load_dotenv
import json
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

request = youtube.channels().list(
    part='statistics',
    forUsername='github'
)

response = request.execute()

print(json.dumps(response, sort_keys=True, indent=4))