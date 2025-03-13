import enum
import aiohttp
from tenacity import retry, stop_after_attempt, wait_fixed


class DateRange(enum.Enum):
    day = "daily"
    week = "weekly"
    month = "monthly"

@retry(stop=stop_after_attempt(6), wait=wait_fixed(4))
async def get_trending_html(
    session: aiohttp.ClientSession, language="", date_range=DateRange.day
):
    async with session.get(
        f"https://github.com/trending/{language}?since={date_range.value}"
    ) as response:
        html = await response.text()
        return html
