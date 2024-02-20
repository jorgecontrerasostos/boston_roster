
import requests
from bs4 import BeautifulSoup

def request(url: str):
    response = requests.get(url)
    return response.text


def make_the_soup(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_players(soup: BeautifulSoup):
    player_names = []
    players_list = soup.find_all('td', class_='info')
    for player in players_list:
        player = player.find('a').text
        player_names.append(player)
    return player_names