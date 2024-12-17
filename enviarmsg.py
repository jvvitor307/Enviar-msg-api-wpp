import os

import requests
from dotenv import load_dotenv

load_dotenv()

bearer = os.getenv("BEARER")

headers = {
    "Authorization": f"Bearer {bearer}",
    "Content-Type": "application/json"
}

json = {
    "messaging_product": "whatsapp",
    "to": "5586994661837",
    "type": "template",
    "template": {
        "name": "statement_available_1",
        "language": {"code": "pt_BR" },
        "components": [
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "João Vitor Melo Fontenele"},
                    {"type": "text", "text": "4645165464"}
                ]
            }
        ]
    }
}

response = requests.post(
    url="https://graph.facebook.com/v21.0/541328609054736/messages",
    headers=headers,
    json=json  # Use 'json' instead of 'data' for sending JSON data

    )

print(response.status_code)
print(response.text)
