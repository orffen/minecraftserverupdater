#!/usr/bin/env python3
# update.py -- Minecraft server updater

import bs4
import requests

def download(download_url):
    print("Downloading latest...")
    response = requests.get(download_url)
    with open("minecraft_server.jar", "wb") as file:
        file.write(response.content)
    with open("version.txt", "w") as file:
        file.write(download_url)


if __name__ == "__main__":
    response = requests.get("https://www.minecraft.net/en-us/download/server/")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    link = soup("a", attrs={
        "aria-label": "mincraft version"
    })
    download_url = link[0]["href"]
    try:
        with open("version.txt", "r") as file:
            last = file.read()
            if download_url != last:
                download(download_url)
            else:
                print("Already up-to-date.")
    except FileNotFoundError:
        download(download_url)
