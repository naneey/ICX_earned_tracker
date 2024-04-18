from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider

connections = {
    "mainnet": {"iconservice": "https://ctz.solidwallet.io", "nid": 1},
    "lisbon": {"iconservice": "https://lisbon.net.solidwallet.io", "nid": 2}
}

NETWORK = 'mainnet'
env = connections[NETWORK]

icon_service = IconService(HTTPProvider(env["iconservice"], 3))
NID = env["nid"]

contracts={
    'system':'cx0000000000000000000000000000000000000000'
}

EXA = 1e18
ICX_MULTIPLIER = 1000