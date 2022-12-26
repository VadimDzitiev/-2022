import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from lxml import html
from lxml import etree



url = 'https://www.championat.com/basketball/_nba/tournament/5163/calendar/'
headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
         }
bot = telebot.TeleBot('5844095331:AAGFbUel39e_avY2zMEGa0PsXP5CK9gJP_8')


response = requests.get(url, headers=headers)
tree = html.fromstring(response.text)
time = []
games = []
teams = []
score = []
play = []

for elem in tree.xpath('//td[@class="stat-results__date-time _hidden-td"]'):
    time.append(elem.text.replace(' ', ''))
for elem in tree.xpath('//span[@class="table-item__name"]'):
    teams.append(elem.text)
for elem in tree.xpath('//span[@class="stat-results__count-main"]'):
    score.append(elem.text.replace(' ', ''))

a = len(teams)/2
b = 0
c = 0

while b < a:
    if score[c][1:] == "–:–": play.append(0)
    else: play.append(1)
    games.append({"game number": c+1,"team1": teams[b], "team2": teams[b+1], "time": time[c].replace("\n", ""), "score": score[c][1:],"play": play[c]})
    b += 2
    c += 1

print(games[500].get("team1"))
print(games[500].get("team2"))
print(games[500].get("time"))
print(games[500].get("score"))
print(games[500].get("play"))



@bot.message_handler(commands=['start'])
def start(message):
    user_id =message.from_user.id
    user_name = message.from_user.first_name
    user_full_name= message.from_user.full_name
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f'Привет, {user_full_name}')
    bot.send_message(message.chat.id, "Выберите команду:")
    t = ""

    team = set(teams)
    for i in team:
        t += f'{i}\n'
    bot.send_message(message.chat.id, t)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    stat = types.KeyboardButton('Stat of last 10 games')
    team = types.KeyboardButton('Выберите команду')

    markup.add(stat, team)


@bot.message_handler()
def lol(message):

    team = set(teams)
    if message.text in team:
        bot.send_message(message.chat.id, "Посмотрим игры "+message.text)
        a=0
        res = ''
        s="  "
        while games[a].get("play")==1:
            if message.text == games[a].get("team1") or message.text == games[a].get("team2"):
                b = f'{games[a].get("team1")} : {games[a].get("team2")}    {games[a].get("time")}     {games[a].get("score")}'
                res += f'{b}\n'
            a+=1
        bot.send_message(message.chat.id, res)

@bot.message_handler()
def lol(message): pass

bot.polling(none_stop=True)
"""'\n19.10.2022\xa002:30'"""