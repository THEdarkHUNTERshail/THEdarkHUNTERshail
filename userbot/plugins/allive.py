import os
import requests
import time
from PIL import Image
from io import BytesIO
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from datetime import datetime

ALIVE_PHOTTO = os.environ.get("ALIVE_PHHOTO" , None)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "This user"

@borg.on(admin_cmd(outgoing=True, pattern="allive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "**LUCIFER πΈπ πΎοΈπ½π»πΈπ½π΄**\n"
        pm_caption += f"**ππͺ πΉπ π€π€**            : {DEFAULTUSER}\n"
        pm_caption += "ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½        : 15.0\n"
        pm_caption += "πΏπππ·πΎπ½ ππ΄πππΈπΎπ½          : 3.8.5\n"
        pm_caption += "πππΏπΏπΎππ π²π·π°π½π½π΄π»         : [α΄α΄ΙͺΙ΄](https://t.me/lucifer_userbot)\n"
        pm_caption += "πππΏπΏπΎππ πΆππΎππΏ           : [α΄α΄ΙͺΙ΄](https://t.me/lucifer_support)\n"
        pm_caption += "πΎππππππππ π½π            : [ @broken_identitiess ](https://t.me/broken_identitiess)\n"
        pm_caption += "ββββββββββββββ\n ββββββββββββββ\nββββββββββββββ\nββββββββββββββ\nβββββββββ«ββββββ\nβββββββββββββββ"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PIC,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/d7cbffcb6bae55874b1c2.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"**LUCIFER πΈπ πΎοΈπ½π»πΈπ½π΄**\n"
                      f"**ππͺ πΉπ π€π€**            : {DEFAULTUSER}\n"
                      "ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½        : 15.0\n"
                      "πΏπππ·πΎπ½ ππ΄πππΈπΎπ½          : 3.8.5\n"
                      "πππΏπΏπΎππ π²π·π°π½π½π΄π»         : [α΄α΄ΙͺΙ΄](https://t.me/lucifer_userbot)\n"
                      "πππΏπΏπΎππ πΆππΎππΏ           : [α΄α΄ΙͺΙ΄](https://t.me/lucifer_userbot)\n"
                      "πΎππππππππ π½π           : [ @broken_identitiess ](https://t.me/broken_identitiess)\n"
                                "ββββββββββββββ\n ββββββββββββββ\n ββββββββββββββ\n βββββββββββββββ \n βββββββββ«ββββββ \n βββββββββββββββ" , link_preview = False) 
        await alive.delete()
