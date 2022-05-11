from cgi import MiniFieldStorage
from email import header
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import deque
import time
import csv


driver = webdriver.Chrome("chromedriver.exe")
time.sleep(2)
# 타격
driver.get("http://www.statiz.co.kr/stat_at.php?re=0&lr=")
# 투구 http://www.statiz.co.kr/stat_at.php?re=1&lr=
# 수비 http://www.statiz.co.kr/stat_at.php?re=2&lr=
soup = BeautifulSoup(driver.page_source, "html.parser")
link = soup.find_all("a")
player_list = deque()
for i in link:
    if '<a href="player.php?' in str(i):
        player_list.append(i.attrs["href"])
link = player_list.popleft()
driver.get(f"http://www.statiz.co.kr/{link}")
# #Algorithm
# while player_list:
#     link =  player_list.popleft()
#     driver.get(f"http://www.statiz.co.kr/{link}")
driver.close()
