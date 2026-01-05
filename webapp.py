import requests

def get_title(url: str) -> str:
    resp = requests.get(url, timeout=1)
    resp.raise_for_status()
    return resp.json()["title"]