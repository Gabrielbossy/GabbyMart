import requests
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth
import requests
from requests.auth import HTTPBasicAuth

consumer_key = "oU9zdq18A1sKxGivrGGkl0cPkcGbOa50WqPK2AuFI5Atb8LK"
consumer_secret = "TtXszowiBqOouxHJANTTTGg4yt7tLi62eihUdtiuZ6MpFtctYQa8Hus3lFdKt8ne"


def get_access_token():

    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(
            consumer_key,
            consumer_secret
        )
    )

    return response.json()['access_token']