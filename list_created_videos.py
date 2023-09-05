import requests, json
from .create_video import API_KEY

base_url = "https://api.synthesia.io/v2/videos"
api_key = API_KEY

def list_videos(offset_value:int):
    url = base_url + f"?limit=5&offset={offset_value}" 
    headers = {"Authorization": api_key, "accept":"application/json"}
    response = requests.get(url, headers=headers)
    response_json = response.text
    response_data = json.loads(response_json)
    videos_data = response_data["videos"]
    return videos_data  
