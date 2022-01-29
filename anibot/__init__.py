import os
from pyrogram import Client

TRIGGERS = os.environ.get("TRIGGERS", "/ !").split()
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME")
DB_URL = os.environ.get("DATABASE_URL")
ANILIST_CLIENT = os.environ.get("ANILIST_CLIENT")
ANILIST_SECRET = os.environ.get("ANILIST_SECRET")
ANILIST_REDIRECT_URL = os.environ.get("ANILIST_REDIRECT_URL", "https://anilist.co/api/v2/oauth/pin")
API_ID = int(os.environ.get("API_ID"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID"))
OWNER = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID", "1005170481 972029825").split())))  ## sudos can be included

DOWN_PATH = "anibot/downloads/"
plugins = dict(root="anibot/plugins")
anibot = Client("anibot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)

HELP_DICT = {
    'Misc': '\x1fGroup based commands:\x1f\x1f/settings - Toggle stuff like whether to allow 18+ stuff in group or whether to notify about aired animes\x1f\x1f/disable - Disable use of a cmd in the group (Disable multiple cmds by adding space between them)\x1f`/disable anime anilist me user`\x1f\x1f/enable - Enable use of a cmd in the group (Enable multiple cmds by adding space between them)\x1f`/enable anime anilist me user`\x1f\x1f/disabled - List out disabled cmds\x1f',
    'Additional': 'Use /reverse cmd to get reverse search via tracemoepy API\x1f__Note: This works best on uncropped anime pic,\x1fwhen used on cropped media, you may get result but it might not be too reliable__\x1f\x1fUse /schedule cmd to get scheduled animes based on weekdays\x1f\x1fUse /watch cmd to get watch order of searched anime\x1f\x1fUse /fillers cmd to get a list of fillers for an anime\x1f',
    'Anilist': "\x1fBelow is the list of basic anilist cmds for info on anime, character, manga, etc.\x1f\x1f/anime - Use this cmd to get info on specific anime using keywords (anime name) or Anilist ID\x1f(Can lookup info on sequels and prequels)\x1f\x1f/anilist - Use this cmd to choose between multiple animes with similar names related to searched query\x1f(Doesn't includes buttons for prequel and sequel)\x1f\x1f/character - Use this cmd to get info on character\x1f\x1f/manga - Use this cmd to get info on manga\x1f\x1f/airing - Use this cmd to get info on airing status of anime\x1f\x1f/top - Use this cmd to lookup top animes of a genre/tag or from all animes\x1f(To get a list of available tags or genres send /gettags or /getgenres)\x1f\x1f/user - Use this cmd to get info on an anilist user\x1f",
    'Oauth': '\x1fThis includes advanced anilist features\x1f\x1fUse /auth or !auth cmd to get details on how to authorize your Anilist account with bot\x1fAuthorising yourself unlocks advanced features of bot like:\x1f- adding anime/character/manga to favourites\x1f- viewing your anilist data related to anime/manga in your searches which includes score, status, and favourites\x1f- unlock /flex, /me, /activity and /favourites commands\x1f- adding/updating anilist entry like completed or plan to watch/read\x1f- deleting anilist entry\x1f\x1fUse /flex or !flex cmd to get your anilist stats\x1f\x1fUse /logout or !logout cmd to disconnect your Anilist account\x1f\x1fUse /me or !me cmd to get your anilist recent activity\x1fCan also use /activity or !activity\x1f\x1fUse /favourites or !favourites cmd to get your anilist favourites\x1fHELP_DICT["Oauth"] = ',
}