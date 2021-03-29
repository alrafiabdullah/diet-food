import os
import json
import base64
from imagekitio import ImageKit

if os.path.exists('secrets.json'):
    with open('secrets.json') as secret:
        data = json.load(secret)
    secret.close()


imagekit = ImageKit(
    private_key=data["IMGKT_PRIVATE_KEY"],
    public_key=data["IMGKT_PUBLIC_KEY"],
    url_endpoint=data["IMGKT_URL_ENDPOINT"]
)


def get_image_url(path):
    imagekit_url = imagekit.url({
        "path": path,
        "url_endpoint": data["IMGKT_URL_ENDPOINT"],
        "transformation": [{"height": "300", "width": "400"}],
    })

    return imagekit_url


def upload_image(file_system, name):
    upload = imagekit.upload(
        file=file_system,
        file_name=name,
        options={
            "folder": "/Diet"
        }
    )

    return upload["response"]


def delete_image(file_id):
    imagekit.delete_file(file_id)
    return True
