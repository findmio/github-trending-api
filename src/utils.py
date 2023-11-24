import os
import json
from datetime import datetime

import aiofiles
import aiofiles.os


def get_current_hour():
    now = datetime.now()
    hour = now.strftime("%H")
    return int(hour)


def get_current_day():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    return current_date


def parse_int(text: str):
    if isinstance(text, str):
        return int("".join([word for word in text if word.isdigit()]))
    return None


async def read_json(filepath):
    async with aiofiles.open(filepath, mode="r") as f:
        content = await f.read()
    return json.loads(content)


async def write_json(filepath: str, data: dict):
    dir_name = os.path.dirname(filepath)
    path_exists = await aiofiles.os.path.exists(dir_name)

    if not path_exists:
        await aiofiles.os.makedirs(dir_name)

    async with aiofiles.open(filepath, "w") as f:
        await f.write(json.dumps(data, ensure_ascii=False, indent=4))
