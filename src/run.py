import os

import requests
import xlsxwriter
from bs4 import BeautifulSoup


def create_xlsx_file(headers, rows):
    ths = headers.findAll("th")
    header = [th.text for th in ths]

    row_list = []
    for row in rows:
        row_list.append([td.text for td in row.findAll("td")])

    wb = xlsxwriter.Workbook("data.xlsx")
    ws = wb.add_worksheet()
    ws.write_row(0, 0, header)
    for i, row in enumerate(row_list):
        ws.write_row(i + 1, 0, row)
    wb.close()


def update_num_txt(num):
    with open("num.txt", "w") as f:
        f.write(num + "\r\n")


def line_notify(num, event_date, agenda_list, docs):
    url = "https://notify-api.line.me/api/notify"
    access_token = os.getenv("ACCESS_TOKEN")
    assert access_token is not None
    headers = {"Authorization": f"Bearer {access_token}"}
    agenda = "\n".join(agenda_list)
    message = (
        f"\n\n回数:\n{num}\n\n"
        + f"開催日:\n{event_date}\n\n"
        + f"議題等:\n{agenda}\n\n"
        + f"資料等:\n{docs}"
    )
    data = {"message": message}
    resp = requests.post(url, headers=headers, data=data)
    assert resp.status_code == 200


def check_latest_num(num):
    url = "https://ssatocc.github.io/chuikyo-notify/"
    resp = requests.get(url)
    assert resp.status_code == 200
    saved_num = resp.text.split("\r\n")[0]
    return saved_num == num


def validate_headers(headers):
    ths = headers.findAll("th")
    th_set = {th.text for th in ths}
    expected_th_set = {
        "回数",
        "資料等",
        "開催案内",
        "議題等",
        "議事録／議事要旨",
        "開催日",
    }
    assert expected_th_set == th_set


def validate_title(title):
    expected_title = "中央社会保険医療協議会(中央社会保険医療協議会総会) ｜厚生労働省"
    assert expected_title == title


def main():
    url = "https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html"
    resp = requests.get(url)
    assert resp.status_code == 200
    soup = BeautifulSoup(resp.content, "html.parser")

    title = soup.find("title").text
    validate_title(title)

    table = soup.find("table", {"class": "m-tableFlex"})
    rows = table.findAll("tr")
    headers, latest = rows[0], rows[1]
    validate_headers(headers)

    tds = latest.findAll("td")
    td_num, td_event_date, td_agenda, _, td_docs, _ = tds

    num = td_num.text
    if not check_latest_num(num):
        event_date = td_event_date.text.split("（")[0]
        ol_agenda = td_agenda.find("ol")
        agenda_list = [li.text for li in ol_agenda.findAll("li")]
        docs = td_docs.find("a")["href"]
        line_notify(num, event_date, agenda_list, docs)
        update_num_txt(num)
        create_xlsx_file(headers, rows[1:])


if __name__ == "__main__":
    main()
