import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

title = ["POINTS", "REBOUNDS", "ASSISTS", "BLOCKS", "STEALS", "TURNOVER", "THREE POINTERS MADE",
         "FREE THROWS MADE", "FANTASY POINTS"]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
REQUEST_LINE = "GET / HTTP/1.1"
ACCEPT_ENCODING = "gzip, deflate, br"
ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
#     playableTile__descriptionContainer

NBA_LINK = "https://www.nba.com/stats"
req = requests.get(NBA_LINK, headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGUAGE,
                                "Accept-Encoding": ACCEPT_ENCODING, "Accept": ACCEPT, "Request-Line": REQUEST_LINE})
NBA_TEXT = req.text
nba_details = BeautifulSoup(NBA_TEXT, features="lxml")
# print(nba_details)

nba_player_name = nba_details.find_all(name="tbody")
# print(nba_player_name[0])
nba_player = nba_details.find_all(name="a", class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
# print(nba_player)
# print(nba_player[0].text)

player_points = []
player_name = []

for player in nba_player:
    if player.get("href").split("/")[1] == "game":
        player_points.append(player.text)
    else:
        player_name.append(player.text)

print(player_name[44])
print(player_points[44])

player_names = player_name[:45]
player_points = player_points[:45]

player_names = [[x] for x in player_names]
for i in range(len(player_names)):
    player_names[i].append(player_points[i])

# data = [["Player Name", "Points"]]
# data.extend(player_names)
# csv_file_path = "NBA_PLAYERS_POINTS.csv"
#
# with open(csv_file_path, mode="w", newline="") as file:
#     csv_file = csv.writer(file)
#
#     csv_file.writerows(data)

# FOR SEPERATE DIVISION FOR NBA PLAYERS
start = 0
end = 5
new_list = []
for i in range(9):
    data = [["Player Name", "Points"]]
    new_list = player_names[start:end]
    start += 5
    end += 5
    data.extend(new_list)
    print(data)
    csv_file_path = f"{title[i]}.csv"

    with open(csv_file_path, mode="w", newline="") as file:
        csv_file = csv.writer(file)

        csv_file.writerows(data)



