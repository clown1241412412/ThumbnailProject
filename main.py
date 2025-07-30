import requests
from datetime import datetime
#
video_url = input("링크를 붙여넣어주세요.(Ctrl + Shift + V)\n")
video_id = video_url.split("v=")[-1]
thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"
response = requests.get(thumbnail_url)

now = datetime.now().strftime("%Y%m%d_%H%M%S")  # 예: 20250730_152345
with open(f"thumbnail{now}.jpg", "wb") as f:
   f.write(response.content)
print(" 썸네일 다운로드 완료!")