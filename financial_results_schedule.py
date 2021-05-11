import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup


def main():
    file = open('./data/financial_results_schedule.csv', 'w', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    html_data = requests.get('https://www.traders.co.jp/domestic_stocks/domestic_market/kessan_s/kessan_s.asp')
    soup = BeautifulSoup(html_data.content, "html.parser")
    table = soup.findAll("table", {"bordercolor": "#AAB5BB"})[0]

    tr = table.findAll("tr")
    for index, row in enumerate(tr):
        cell = row.findAll(['td'])
        writer.writerow([cell[0].get_text().strip(),
                         cell[1].get_text().strip(),
                         cell[2].get_text().strip(),
                         cell[3].get_text().strip(),
                         cell[4].get_text().strip(),
                         cell[5].get_text().strip(),
                         cell[6].get_text().strip(),
                         cell[7].get_text().strip(),
                         cell[8].get_text().strip()])
    file.close()


if __name__ == '__main__':
    main()
