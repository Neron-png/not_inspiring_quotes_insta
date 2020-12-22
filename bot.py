# -*- coding: utf-8 -*-
import argparse
import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402


from edit_image import compose

clock = 360 # Bot refresh interval in seconds (int)

try:
    input = raw_input
except NameError:
    pass

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
args = parser.parse_args()


bot = Bot()
bot.login(username=args.u, password=args.p, proxy=args.proxy)

if __name__ == '__main__': # Protect against creating an infinite loop if this file gets imported for whatever reason.
    # Loop #                 
    while True:

        if bot.api.get_inbox_v2():
            data = bot.last_json["inbox"]["threads"]
            for item in data:
                user_id = str(item["inviter"]["pk"])
                if user_id == "8431380614":
                    #bot.console_print(item["inviter"]["username"], "lightgreen")
                    
                    last_item = item["last_permanent_item"]
                    item_type = last_item["item_type"]
                    if item_type == "text":
                        content = last_item["text"]
                        if content != "copy!":
                            print(content)
                            bot.send_message("copy!", user_id, thread_id=item["thread_id"])
                            compose(content,bot)
        time.sleep(clock)                    