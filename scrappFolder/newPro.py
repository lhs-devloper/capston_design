from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from collections import deque
import time
import csv

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--incognito")
chrome_option.add_argument("--headless")
chrome_option.add_argument("--no-sandbox")
chrome_option.add_argument("--disable-setuid-sandbox")
chrome_option.add_argument("--disable-dev-shm-usage")
chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_option)
driver.implicitly_wait(5)

player_list = list()

# Defintion
def find_a_tag(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    link = soup.find_all("a")
    for i in link:
        if '<a href="player.php?' in str(i):
            i = i.attrs["href"]
            i = i.replace("player.php?", "player.php?opt=1&")
            player_list.append(i)


def get_stats(link):
    # gdp, sh sf
    driver.get(f"http://www.statiz.co.kr/{link}")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    name = soup.select_one(
        "body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(1) > div > div.col-xs-12.col-sm-4.col-md-4.col-lg-4 > div > div.btn-group > button > font"
    ).get_text()
    print(name)
    check = soup.select_one(
        "body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr > td"
    )
    if None == check:
        driver.quit()
        return
    check = check.get_text().rstrip()
    if "없습니다" in check:
        driver.quit()
        return
    f = open(f"../data/{name}.csv", "w", encoding="utf-8", newline="")
    csvWriter = csv.writer(f)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    stats_list = [
        "year",
        "team",
        "age",
        "G",
        "PA",
        "AB",
        "R",
        "HIT",
        "HIT_2",
        "HIT_3",
        "HOME_RUN",
        "BASE",
        "RBI",
        "SB",
        "CS",
        "HBP",
        "IBB",
        "SO",
        "GDP",
        "SH",
        "SF",
        "AVG",
        "OBP",
        "SLG",
        "OPS",
        "wOBA",
        "wRC",
        "WAR",
    ]
    csvWriter.writerow(stats_list)
    for i in range(3, 100):
        year = soup.select_one(
            f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td.colhead_stz"
        )
        if year is None:
            print("Searching 종료")
            break
        team = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(2)"
            )
            .get_text()
            .rstrip()
        )
        age = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(3)"
            )
            .get_text()
            .rstrip()
        )
        # app 경기 수(Game)
        g = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(5)"
            )
            .get_text()
            .rstrip()
        )
        # 타석
        pa = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(6)"
            )
            .get_text()
            .rstrip()
        )
        # 타수
        ab = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(7)"
            )
            .get_text()
            .rstrip()
        )
        # 득점
        r = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(8)"
            )
            .get_text()
            .rstrip()
        )
        # 안타
        hit = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(9)"
            )
            .get_text()
            .rstrip()
        )
        # 2타
        hit_2 = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(10)"
            )
            .get_text()
            .rstrip()
        )
        # 3타
        hit_3 = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(11)"
            )
            .get_text()
            .rstrip()
        )
        # 홈런
        home_run = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(12)"
            )
            .get_text()
            .rstrip()
        )
        # 루타 (1타+2*2타+{i}*3타+4*홈런)+도루+고의사구-볼넷
        base = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(13)"
            )
            .get_text()
            .rstrip()
        )
        # 타점
        rbi = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(14)"
            )
            .get_text()
            .rstrip()
        )
        # 도루
        sb = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(15)"
            )
            .get_text()
            .rstrip()
        )
        # 도루실패
        cs = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(16)"
            )
            .get_text()
            .rstrip()
        )
        # 사구
        hbp = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(18)"
            )
            .get_text()
            .rstrip()
        )
        # 고의사구
        ibb = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(19)"
            )
            .get_text()
            .rstrip()
        )
        # 삼진
        so = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(20)"
            )
            .get_text()
            .rstrip()
        )
        # 병살
        gdp = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(21)"
            )
            .get_text()
            .rstrip()
        )
        # 희생타
        sh = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(22)"
            )
            .get_text()
            .rstrip()
        )
        # 희생플라이
        sf = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(23)"
            )
            .get_text()
            .rstrip()
        )
        # 타율
        avg = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(24)"
            )
            .get_text()
            .rstrip()
        )
        # 출루
        obp = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(25)"
            )
            .get_text()
            .rstrip()
        )
        # 장타
        slg = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(26)"
            )
            .get_text()
            .rstrip()
        )
        # OPS
        ops = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(27)"
            )
            .get_text()
            .rstrip()
        )
        # wOBA
        woba = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(28)"
            )
            .get_text()
            .rstrip()
        )
        # wRC
        wrc = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(29)"
            )
            .get_text()
            .rstrip()
        )
        # War
        war = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(30)"
            )
            .get_text()
            .rstrip()
        )
        year = year.get_text().rstrip()
        if "," in team:
            team = team.replace(",", "|")
        basestat_List = f"{year}, {team}, {age}, {g}, {pa}, {ab}, {r}, {hit}, {hit_2}, {hit_3}, {home_run}, {base}, {rbi}, {sb}, {cs}, {hbp}, {ibb}, {so}, {gdp}, {sh}, {sf}, {avg}, {obp}, {slg}, {ops}, {woba}, {wrc}, {war}\n"
        f.write(basestat_List)
    f.close()
    driver.quit()


for i in range(3):
    driver.get(f"http://www.statiz.co.kr/draft.php?opt=0&sopt={2020-i}&te=")
    find_a_tag(driver.page_source)
set_player_list = set(player_list)
player_list = deque(set_player_list)
print(len(player_list))
while player_list:
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(5)
    link = player_list.popleft()
    time.sleep(3)
    print(link)
    get_stats(link)
