from cgi import MiniFieldStorage
from email import header
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


class Crawling:
    def __init__(self, url):
        self.url = url

    def setting(self):
        driver = webdriver.Chrome("chromedriver.exe")
        time.sleep(3)
        driver.get(self.url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        inf = soup.find("a")
        no_result = soup.select_one("#player-table-statistics-body > tr > td")
        if inf.get_text() == "WhoScored.com" or no_result is None:
            driver.close()
        elif no_result.get_text() == "There are no results to display":
            driver.close()
        else:
            name = soup.select_one(
                "#layout-wrapper > div.sticky-unit-wrapper > div.main-content-column > div.header > h1"
            )
            name = name.get_text()
            name = name.replace(" ", "_")
            name = name.lstrip()
            name = name.rstrip()
            print(name)
            f = open(f"data/{name}.csv", "w", encoding="utf-8", newline="")
            csvWriter = csv.writer(f)
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
            rating = soup.select_one(
                "#player-table-statistics-head > tr > th.global.sortable.rating"
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
            rating = rating.get_text()

            settingList = [
                apps,
                mins,
                goal,
                assists,
                yels,
                reds,
                shot_per_game,
                ps,
                awon,
                motm,
                rating,
            ]
            print(settingList)
            csvWriter.writerow(settingList)
            f.close()
            driver.close()

    def run(self):
        # Crawling Run
        driver = webdriver.Chrome("chromedriver.exe")
        time.sleep(3)
        driver.get(self.url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        inf = soup.find("a")
        no_result = soup.select_one("#player-table-statistics-body > tr > td")
        if inf.get_text() == "WhoScored.com" or no_result is None:
            driver.close()
        elif no_result.get_text() == "There are no results to display":
            driver.close()
        else:
            name = soup.select_one(
                "#layout-wrapper > div.sticky-unit-wrapper > div.main-content-column > div.header > h1"
            )
            name = name.get_text()
            name = name.replace(" ", "_")
            name = name.lstrip()
            name = name.rstrip()
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
            # player-table-statistics-body > tr:nth-child(1) > td:nth-child(6)
            f = open(f"data/{name}.csv", "a", encoding="utf-8", newline="")
            for i in range(1, 100):
                apps_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td:nth-child(6)"
                )
                mins_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.minsPlayed"
                )
                goals_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.goal"
                )
                assists_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.assistTotal"
                )
                yellows_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.yellowCard"
                )
                reds_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.redCard"
                )
                spg_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.shotsPerGame"
                )
                ps_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.passSuccess"
                )
                awpg_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.aerialWonPerGame"
                )
                mom_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.manOfTheMatch"
                )
                rattings_value = soup.select_one(
                    f"#player-table-statistics-body > tr:nth-child({i}) > td.rating"
                )
                if mins_value is None:
                    print("Searching 종료")
                    break
                apps = apps_value.get_text()
                mins = mins_value.get_text()
                goals = goals_value.get_text()
                assists = assists_value.get_text()
                yellows = yellows_value.get_text()
                reds = reds_value.get_text()
                spg = spg_value.get_text()
                ps = ps_value.get_text()
                awp = awpg_value.get_text()
                mom = mom_value.get_text()
                rating = rattings_value.get_text()

                apps = apps.rstrip()
                mins = mins.rstrip()
                goals = goals.rstrip()
                assists = assists.rstrip()
                yellows = yellows.rstrip()
                reds = reds.rstrip()
                spg = spg.rstrip()
                ps = ps.rstrip()
                awp = awp.rstrip()
                mom = mom.rstrip
                rating = rating.rstrip()

                searchingList = f"{apps}, {mins}, {goals}, {assists}, {yellows}, {reds}, {spg}, {ps}, {awp}, {mom}, {rating}\n"
                f.write(searchingList)
            # mins_value = mins_value.find_all("tr")
            f.close()
            driver.close()
