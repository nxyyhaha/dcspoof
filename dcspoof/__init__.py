from discord.gateway import DiscordWebSocket

from .identify import make_identify

_current = "ios"
DiscordWebSocket.identify = make_identify(_current)


def mode(name: str = "ios"):
    global _current
    _current = name
    DiscordWebSocket.identify = make_identify(name)
