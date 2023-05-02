import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")
NAME = os.getenv("NAME")
FILENAME = os.getenv("FILENAME")

QUERY = """
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
