import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup


def main1():
    html_data = requests.get('https://portal.morningstarjp.com/StockInfo/pts/ranking?kind=0&page=0')
    soup = BeautifulSoup(html_data.content, "html.parser")
    table = soup.findAll("table", {"class": "sr-tbl"})[0]
    thead = table.find("thead").findAll("tr")
    tbody = table.find("tbody").findAll("tr")

    file = open('./data/pts.csv', 'w', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    # ヘッダー
    for index, row in enumerate(thead):
        cell = row.findAll(['th'])
        writer.writerow([cell[0].get_text(),
                         cell[1].get_text(),
                         cell[2].get_text(),
                         cell[3].get_text(),
                         "時刻",
                         cell[4].get_text(),
                         cell[5].get_text(),
                         cell[5].get_text()+"(%)",
                         cell[6].get_text(),
                         cell[7].get_text()])
    for index, row in enumerate(tbody):
        cell = row.findAll(['td'])
        writer.writerow([cell[0].get_text(),
                         cell[1].get_text(),
                         cell[2].get_text(),
                         cell[3].get_text(),
                         cell[4].get_text(),
                         cell[5].get_text(),
                         cell[6].get_text(),
                         cell[7].get_text(),
                         cell[8].get_text(),
                         cell[9].get_text()])
    file.close()

def main2():
    html_data = requests.get('https://portal.morningstarjp.com/StockInfo/pts/ranking?kind=0&page=1')
    soup = BeautifulSoup(html_data.content, "html.parser")
    table = soup.findAll("table", {"class": "sr-tbl"})[0]
    thead = table.find("thead").findAll("tr")
    tbody = table.find("tbody").findAll("tr")

    file = open('./data/pts.csv', 'a', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    for index, row in enumerate(tbody):
        cell = row.findAll(['td'])
        writer.writerow([cell[0].get_text(),
                         cell[1].get_text(),
                         cell[2].get_text(),
                         cell[3].get_text(),
                         cell[4].get_text(),
                         cell[5].get_text(),
                         cell[6].get_text(),
                         cell[7].get_text(),
                         cell[8].get_text(),
                         cell[9].get_text()])
    file.close()

if __name__ == '__main__':
    main1()
    main2()
