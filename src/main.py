import asyncio
from os import path
from typing import List, TypedDict

import aiohttp

from parse import parse_html
from fetch import DateRange, get_trending_html
from utils import get_current_day, get_current_hour, read_json, write_json

src_path = path.dirname(__file__)
project_path = path.dirname(src_path)

raw_path = path.join(project_path, "./raw")
archives_path = path.join(raw_path, "./archives")


class Language(TypedDict):
    urlParam: str
    name: str


async def get_language_data(
    session: aiohttp.ClientSession,
    language: Language,
    date_range=DateRange.day,
):
    html = await get_trending_html(
        session=session, language=language["urlParam"], date_range=date_range
    )

    repositories = parse_html(language["name"], html)

    if language["name"]:
        filename = f"{language['name']}.{date_range.name}.json"
    else:
        filename = f"{date_range.name}.json"

    # back up today's data at midnight every day
    if get_current_hour() == 0:
        filepath = f"{archives_path}/{get_current_day()}/{filename}.json"
        await write_json(filepath, repositories)

    filepath = f"{raw_path}/{filename}.json"
    await write_json(filepath, repositories)


async def main():
    languages_path = path.join(project_path, "./languages.json")
    languages: List[Language] = await read_json(languages_path)

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[
                get_language_data(session, language, date_range)
                for date_range in DateRange
                for language in languages
            ]
        )


if __name__ == "__main__":
    asyncio.run(main())
