from datetime import date
from typing import List

from fastapi import FastAPI
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from SETTINGS import FILENAME, NAME, TOKEN, URL, QUERY
from models import DeviceInfo

app = FastAPI()

transport = AIOHTTPTransport(
    url=URL,
    headers={"Authorization": f"Token {TOKEN}"},
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(QUERY)


########################################################################
#    /netbox is an endpoint that fetches the list of devices from the
#    GraphQL server and returns a list of DeviceInfo objects.
#######################################################################
@app.get("/netbox", response_model=List[DeviceInfo])
def netbox() -> List[DeviceInfo]:
    result = client.execute(query)
    devices = result.get("device_list", [])
    results = []

    for device in devices:
        ipv4 = device.get("primary_ip4", {}).get("address", "0.0.0.0")
        device_info = DeviceInfo(
            id=device.get("id"),
            name=device.get("name"),
            manufacturer=device.get("device_type", {})
            .get("manufacturer", {})
            .get("name"),
            ipv4=ipv4,
        )
        results.append(device_info)
    return results


########################################################################
#    /payload is an endpoint that writes a file with information about
#               the name and current date of the project
#######################################################################
@app.get("/payload")
async def payload() -> str:
    data = f"Name: {NAME} Date ({date.today().strftime('%Y-%m-%d')})"

    with open(FILENAME, "w") as file:
        file.write(data)

    return data
