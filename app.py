import os
import requests
import praw

from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def gerar_nome_padrao(extensao, prefixo="wallpaper"):
    arquivos = os.listdir("images")
    numeros = [
        int(f.split("-")[1].split(".")[0])
        for f in arquivos
        if f.startswith(prefixo) and f.endswith(extensao)
        and f.split("-")[1].split(".")[0].isdigit()
    ]
    proximo_num = max(numeros) + 1 if numeros else 1
    return f"{prefixo}-{proximo_num:03d}{extensao}"

subreddit = reddit.subreddit("wallpaper")

for post in subreddit.hot(limit=2):
    url = post.url

parsed_url = urlparse(url)
_, ext = os.path.splitext(parsed_url.path)

if ext.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
    print("URL does not appear to be a direct image.")

response = requests.get(url)

if response.status_code != 200:
    print("Error downloading image:", response.status_code)

file_name = gerar_nome_padrao(ext.lower())
path = os.path.join("images", file_name)

with open(path, "wb") as f:
    f.write(response.content)

print("Image saved as:", file_name)
