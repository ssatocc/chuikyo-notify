import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    title = soup.find("title").text
    print(title)

    table = soup.find("table", {"class": "m-tableFlex"})
    rows = table.findAll("tr")
    headers, recent = rows[0], rows[1]
    print(headers)
    print(recent)


if __name__ == "__main__":
    main()
