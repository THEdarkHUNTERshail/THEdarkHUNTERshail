#La la la la la
import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Devil's Son"

@borg.on(admin_cmd(pattern="hell$"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "**βHell!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"**β Lucifer**\nβ π{ms}πΏ\nβ My Peru Master:-{DEFAULTUSER}"
    )


CMD_HELP.update(
    {
        "hell": "__**PLUGIN NAME :** hell__\
    \n\nπ** CMD β** `.hell`\
    \n**USAGE   β  **Shows you the ping speed of server"
    }
)
