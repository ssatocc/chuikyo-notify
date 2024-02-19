import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    title = soup.find("title").text
    expected_title = "中央社会保険医療協議会(中央社会保険医療協議会総会) ｜厚生労働省"
    assert expected_title == title

    table = soup.find("table", {"class": "m-tableFlex"})
    rows = table.findAll("tr")
    headers, recent = rows[0], rows[1]

    ths = headers.findAll("th")
    th_set = {th.text for th in ths}
    expected_th_set = {"回数", "資料等", "開催案内", "議題等", "議事録／議事要旨", "開催日"}
    assert expected_th_set == th_set

    print(recent)


if __name__ == "__main__":
    main()
