import requests
from synthesia.create_video import base_url, API_KEY

def check_vh_video_status(video_id:str):
    url = base_url + "/" + video_id
    headers = {"Authorization": API_KEY}
    response = requests.get(url, headers=headers)
    video_data = response.json()
    return video_data