from helpers import request, make_the_soup, get_players
import pprint as pp

def main():
    boston_page = request('https://www.mlb.com/redsox/roster')
    boston_roster = make_the_soup(boston_page)
    boston_players = get_players(boston_roster)
    pp.pprint(boston_players)

if __name__ == '__main__':
    main()