<h1 align="center">github-trending-api</h1>

<p align="center">使用 github actions 定时爬取 <a href="https://github.com/trending/">github trending</a> 生成备份文件。提供可调用的地址</p>

<details>
<summary>

### 数据类型

</summary>

```json
[
    {
        "author": "emilwallner",
        "name": "Screenshot-to-code",
        "avatar": "https://github.com/emilwallner.png",
        "sponsor": "https://github.com/sponsors/emilwallner",
        "url": "https://github.com/emilwallner/Screenshot-to-code",
        "description": "A neural network that transforms a design mock-up into a static website.",
        "language": "HTML",
        "languageColor": "#e34c26",
        "stars": 15508,
        "fork": 1494,
        "currentPeriodStars": 326,
        "builtBy": [
            {
                "href": "https://github.com/emilwallner",
                "avatar": "https://avatars.githubusercontent.com/u/12543699?s=40&v=4",
                "username": "emilwallner"
            }
        ]
    }
]
```

</details>

<details open>
<summary>

### 获取最新的数据

</summary>

**总榜单**

本日数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/day.json

本周数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/week.json

本月数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/month.json


```python
import requests

requests.get('https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/day.json')
```

**Python 榜单**

本日数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/Python.day.json


本周数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/Python.week.json


本月数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/Python.month.json

示例

```python
import requests

requests.get('https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/Python.day.json')
```

支持的语言，请查看 [languages.json](https://github.com/findmio/github-trending-api/blob/main/languages.json)

</details>

<details open>
<summary>

### 获取归档的数据

</summary>

**总榜单**

获取 2023-11-25 日的数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/archives/2023-11-25/day.json


获取 2023-11-25 所在周的数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/archives/2023-11-25/week.json


获取 2023-11-25 所在月的数据

https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/archives/2023-11-25/month.json


```python
import requests

requests.get('https://raw.githubusercontent.com/findmio/github-trending-api/main/raw/day.json')
```

支持的语言，请查看 [languages.json](https://github.com/findmio/github-trending-api/blob/main/languages.json)

</details>
