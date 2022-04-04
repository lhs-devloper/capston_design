from cgi import MiniFieldStorage
from selenium import webdriver
from bs4 import BeautifulSoup
import time


class Crawling:
    def __init__(self, url):
        self.url = url

    def run(self):
        # Crawling Run
        driver = webdriver.Chrome("chromedriver.exe")
        time.sleep(3)
        driver.get(self.url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        inf = soup.find("a")
        if inf.get_text() == "WhoScored.com":
            driver.close()
        else:
            apps = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.ap"
            )
            mins = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.minsPlayed"
            )
            goal = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.goal"
            )
            assists = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.assistTotal"
            )
            yels = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.yellowCard"
            )
            reds = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.redCard"
            )
            shot_per_game = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.shotsPerGame"
            )
            ps = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.passSuccess"
            )
            awon = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.aerialWonPerGame"
            )
            motm = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.manOfTheMatch"
            )
            apps = apps.get_text()
            mins = mins.get_text()
            goal = goal.get_text()
            assists = assists.get_text()
            yels = yels.get_text()
            reds = reds.get_text()
            shot_per_game = shot_per_game.get_text()
            ps = ps.get_text()
            awon = awon.get_text()
            motm = motm.get_text()
            # print("html_parser: ", apps)
            # print("html_parser: ", mins)
            # print("html_parser: ", goal)
            # print("html_parser: ", assists)
            # print("html_parser: ", yels)
            # print("html_parser: ", reds)
            # print("html_parser: ", shot_per_game)
            # print("html_parser: ", ps)
            # print("html_parser: ", awon)
            # print("html_parser: ", motm)

            # -------------------------------------------------------------------------------------------------
            # > tr:nth-child(1) > td.minsPlayed
            """
            for i in range(100):
                mins_value = soup.select(
                    f"#player-table-statistics-body > tr:nth-child({i})"
                )
                if len(mins_value)==0:
                    break
            """

            # mins_value = mins_value.find_all("tr")

            driver.close()
