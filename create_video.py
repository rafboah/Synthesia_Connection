import requests, json

base_url = "https://api.synthesia.io/v2/videos" 
API_KEY = "YOUR API_KEY"

def create_vh_video(
        video_mode:str, title:str, description:str, 
        script:str, avatar:str, background:str
    ):
    if video_mode=="test":
        test = True
        visibility = "private"
    elif video_mode=="production":
        test = False
        visibility = "public"
    else:
        test = True
        visibility = "public"
            
    headers = {"Authorization":API_KEY, "Content-Type":"application/json"}
    data = {
        "test": test, "title":title, "description":description, "visibility":visibility,
        "input": [{ "scriptText":script, "avatar":avatar, "background":background}]
    } 
    response = requests.post(url=base_url,headers=headers,data=json.dumps(data))
    if response.status_code==200 or response.status_code==201:
        video_data = response.json()
        return video_data
    elif response.status_code==400:
        return {"detail":"Failed To Create Video!"}
    else:
        return {"detail":"Error!"}