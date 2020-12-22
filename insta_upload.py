from instabot import Bot
import os
import sys


def upload(bot):
    if os.path.exists("upload.jpg.REMOVE_ME"):
        os.remove("upload.jpg.REMOVE_ME")
    bot.upload_photo("upload.jpg",  
               caption = "")

