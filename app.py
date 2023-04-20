from datetime import date
from typing import List

from fastapi import FastAPI
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

app = FastAPI()

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://demo.netbox.dev/graphql/")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    {
    device_list {
        id,
        name,
        device_type {
            id,
            created,
            model,
            slug,
            part_number,
            manufacturer {
                id,
                name
            }
        },
        tenant {
            id,
            name
        },
        image_attachments {
            id,
            name
        },
        primary_ip4 {
            id,
            address
        }
    }
}
"""
)


@app.get("/netbox")
def netbox() -> List[dict]:
    result = client.execute(query)
    devices = result.get('device_list')
    results = []
    for device in devices:
        device_info = {
            "id": device["id"],
            "name": device["name"],
            "manufacturer": device["device_type"]["manufacturer"]["name"],
        }

        ipv4 = (
            device["primary_ip4"]["address"]
            if device["primary_ip4"]
            else "0.0.0.0"
        )
        device_info["ipv4"] = ipv4
        results.append(device_info)
    return results


@app.get("/payload")
async def payload() -> str:
    payload = (
        f"Nombre: Joel Guerrero Fecha ({date.today().strftime('%Y-%m-%d')})"
    )

    with open("payload.txt", "w") as file:
        file.write(payload)

    return payload
