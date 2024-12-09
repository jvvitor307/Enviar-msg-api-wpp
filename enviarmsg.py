import requests

headers = {
    "Authorization": "Bearer EAAY7NBJTZClMBO24lOweXAbputP09xuQ9tAtmMY2D17HiALELZCyvrQFBkYJe3SGn8M1DjF83nSe5gfq4e9kUwII6B8eFEhjH0VCGZByE5AsqqgBzA24UxYYNXToMWxUjxSZCdhvXlDnEiPyMqRypqNGFcvQzgOiiuVzTIMlKeZADzy2GVy8SDBLKs8BVPpnZAUrHYHQpG0Lj65XobmtJIDehQdxIZD",
    "Content-Type": "application/json"
}

json = {
    "messaging_product": "whatsapp",
    "to": "5586994353290",
    "type": "template",
    "template": {
        "name": "testeteste",
        "language": {"code": "en_US" },
        "components": [
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "teste do joao"},
                    {"type": "text", "text": "quero saber quanto vou gastar para enviar essas msg"},
                    {"type": "text", "text": "Parâmetro 3"},
                    {"type": "text", "text": "Parâmetro 4"}
                ]
            }
        ]
    }
}

response = requests.post(
    url="https://graph.facebook.com/v21.0/518650314662304/messages",
    headers=headers,
    json=json  # Use 'json' instead of 'data' for sending JSON data
)

print(response.status_code)
print(response.text)
