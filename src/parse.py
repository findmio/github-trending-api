from typing import List, Union

from bs4 import BeautifulSoup, Tag

from utils import parse_int


github_url = "https://github.com"


def get_html_text(view_html: Union[Tag, None]):
    if view_html:
        return view_html.get_text(strip=True)
    return None


def parse_language_color(view_html: Union[Tag, None]):
    if view_html:
        language_color_style = view_html.attrs.get("style")
        language_color = [
            part.strip() for part in language_color_style.split(":") if part
        ][-1]
        return language_color
    return None


def parse_builds(views_html: List[Union[Tag, None]]):
    def parse_build_html(view_html: Union[Tag, None]):
        user = view_html.get("href")
        avatar = view_html.find(class_="avatar").get("src")
        return {
            "href": f"{github_url}{user}",
            "avatar": avatar,
            "username": user[1:],
        }

    return [parse_build_html(view) for view in views_html]


def parse_repository(repository_html: Tag):
    link = repository_html.find("a", attrs={"class": "Link"}).get("href")

    (author, name) = [part for part in link.split("/") if part]

    description_html = repository_html.find("p")

    language_html = repository_html.find(
        "span", attrs={"itemprop": "programmingLanguage"}
    )

    language_color_html = repository_html.find("span", class_="repo-language-color")

    stars_html = repository_html.find(
        "a", attrs={"href": f"/{author}/{name}/stargazers"}
    )

    fork_html = repository_html.find("a", attrs={"href": f"/{author}/{name}/forks"})

    builds_html = repository_html.select("a[class='d-inline-block']")

    sponsor_html = repository_html.find("a", class_="Button--secondary")

    new_stars_html = repository_html.find(class_="d-inline-block float-sm-right")

    data = {
        "author": author,
        "name": name,
        "avatar": f"{github_url}/{author}.png",
        "sponsor": f"{github_url}{sponsor_html.get('href')}" if sponsor_html else None,
        "url": f"{github_url}{link}",
        "description": get_html_text(description_html),
        "language": get_html_text(language_html),
        "languageColor": parse_language_color(language_color_html),
        "stars": parse_int(get_html_text(stars_html)),
        "fork": parse_int(get_html_text(fork_html)),
        "currentPeriodStars": parse_int(get_html_text(new_stars_html)),
        "builtBy": parse_builds(builds_html),
    }

    return data


def parse_html(name, html: str):
    soup = BeautifulSoup(html, "lxml")

    projects: List[Tag] = soup.find_all("article", class_="Box-row")

    repositories = [parse_repository(project) for project in projects]

    return repositories
