import os
import time
import requests
import shutil

# creating a forever loop
os.system("TASKKILL /F /IM discord.exe")
url = 'https://github.com/paul2487/discordoldicon/blob/main/app.ico?raw=true'
r = requests.get(url, allow_redirects=True)
open('app.ico', 'wb').write(r.content)
username = os.getlogin()
appico = r"C:\Users\{}\AppData\Local\DiscordPBT\app.ico".format(username)
oldappico = r"app.ico"

try:
    os.remove(appico)
except OSError as e:
    print(e)
else:
    print("File is deleted successfully")
    shutil.copyfile(oldappico, appico)