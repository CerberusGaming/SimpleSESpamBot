import os
import time
from VRageAPI import VRageAPI

api_key = str(os.getenv("API_KEY"))
api_url = str(os.getenv("API_URL"))

delay = int(os.getenv("MESSAGE_DELAY", "300"))
message = str(os.getenv("MESSAGE"))

while True:
    try:
        server = VRageAPI(api_url, api_key)
        server.do_call("/v1/session/chat", "post", data=str(message))
        time.sleep(delay)
    except Exception as E:
        print(E)
        quit(1)
