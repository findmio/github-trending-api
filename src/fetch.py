import enum
import aiohttp


class DateRange(enum.Enum):
    day = "daily"
    week = "weekly"
    month = "monthly"


async def get_trending_html(
    session: aiohttp.ClientSession, language="", date_range=DateRange.day
):
    async with session.get(
        f"https://github.com/trending/{language}?since={date_range.value}"
    ) as response:
        html = await response.text()
        return html
