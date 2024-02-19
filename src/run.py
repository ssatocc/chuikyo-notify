import requests
from bs4 import BeautifulSoup


def main():
    url = "https://example.com"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.find("title").text
    print(title)


if __name__ == "__main__":
    main()
