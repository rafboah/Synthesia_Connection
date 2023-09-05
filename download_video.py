import requests, tempfile
from fastapi.responses import FileResponse

def download_vh_video(download_url:str,video_title:str):
    response = requests.get(url=download_url)
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(suffix=".mp4",delete=False) as tmp_file:
            tmp_file.write(response.content)
            #tmp_file.close()
            file_path = tmp_file.name
        return FileResponse(file_path, filename=video_title+".mp4")
    else:
        return None