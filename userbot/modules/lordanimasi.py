# created by @liualvinas
# lorduserbot

from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`█۞███████]▄▄▄▄▄▄▄▄▄▄▃`"
                     "`▂▄▅█████████▅▄▃▂…`"
                     "`[███████████████████]`"
                     "`◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤`")
    sleep(5)
    await typew.edit("`Bensin Habis..0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`")


@register(outgoing=True, pattern='^.fk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`┌П┐(◣_◢)┌П┐`")


@register(outgoing=True, pattern='^.fu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`┌П┐(►˛◄'!) Fuck You`")


CMD_HELP.update({
    "animasi":
    "`.tank`\
    \nUsage: coba aja.\
    \n\n`.fk` atau `.fu`\
    \nUsage: fuck you.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya."
})
