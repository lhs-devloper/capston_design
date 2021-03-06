from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from collections import deque
import time
import csv


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


def next_click(driver, i):
    if i == 0:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[5]/div/div/div[4]/table/tbody/tr/td[2]/a[2]",
        ).send_keys(Keys.ENTER)
        find_a_tag(driver.page_source)
    else:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[5]/div/div/div[4]/table/tbody/tr/td[2]/a[3]",
        ).send_keys(Keys.ENTER)
        find_a_tag(driver.page_source)


def get_stats(link):
    # gdp, sh sf
    driver.get(f"http://www.statiz.co.kr/{link}")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    name = soup.select_one(
        "body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(1) > div > div.col-xs-12.col-sm-4.col-md-4.col-lg-4 > div > div.btn-group > button > font"
    ).get_text()
    print(name)
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
            print("Searching ??????")
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
        # app ?????? ???(Game)
        g = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(5)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        pa = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(6)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        ab = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(7)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        r = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(8)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        hit = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(9)"
            )
            .get_text()
            .rstrip()
        )
        # 2???
        hit_2 = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(10)"
            )
            .get_text()
            .rstrip()
        )
        # 3???
        hit_3 = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(11)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        home_run = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(12)"
            )
            .get_text()
            .rstrip()
        )
        # ?????? (1???+2*2???+{i}*3???+4*??????)+??????+????????????-??????
        base = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(13)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        rbi = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(14)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        sb = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(15)"
            )
            .get_text()
            .rstrip()
        )
        # ????????????
        cs = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(16)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        hbp = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(18)"
            )
            .get_text()
            .rstrip()
        )
        # ????????????
        ibb = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(19)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        so = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(20)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        gdp = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(21)"
            )
            .get_text()
            .rstrip()
        )
        # ?????????
        sh = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(22)"
            )
            .get_text()
            .rstrip()
        )
        # ???????????????
        sf = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(23)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        avg = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(24)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
        obp = (
            soup.select_one(
                f"body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(25)"
            )
            .get_text()
            .rstrip()
        )
        # ??????
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
    # body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child(4) > td.colhead_stz > span


chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--incognito")
chrome_option.add_argument("--headless")
chrome_option.add_argument("--no-sandbox")
chrome_option.add_argument("--disable-setuid-sandbox")
chrome_option.add_argument("--disable-dev-shm-usage")
chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_option)
driver.implicitly_wait(5)

# ?????? http://www.statiz.co.kr/stat_at.php?re=0&lr=
# ?????? http://www.statiz.co.kr/stat_at.php?re=1&lr=
# ?????? http://www.statiz.co.kr/stat_at.php?re=2&lr=
driver.get("http://www.statiz.co.kr/stat_at.php?re=0&lr=")

# ???????????? ?????????
find_a_tag(driver.page_source)
# 1??? 30???
for i in range(4):
    next_click(driver, i)
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
# driver.get(
#     "http://www.statiz.co.kr/player.php?opt=1&sopt=0&name=%EA%B0%80%EB%82%B4%EC%98%81"
# )
# soup = BeautifulSoup(driver.page_source, "html.parser")
# team = soup.select_one(
#     "body > div.wrapper > div.content-wrapper > div > section.content > div > div:nth-child(2) > div > div:nth-child(4) > div > div > table > tbody > tr:nth-child(10) > td:nth-child(2) > span"
# ).get_text()
# print(type(team), team)
# driver.quit()
