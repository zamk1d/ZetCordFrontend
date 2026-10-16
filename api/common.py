import httpx

from .token_manager import TokenManager
#
URL = "https://28dc-138-124-92-226.ngrok-free.app/"
timeout = httpx.Timeout(30.0, read=20.0)
#

token_manager = TokenManager()