from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

nba_teams = teams.get_teams()
#league_id_nullable="00",
gamefinder = leaguegamefinder.LeagueGameFinder(league_id_nullable="00")
games = gamefinder.get_data_frames()[0]
games.head()
Currentgames = games[games.GAME_DATE.str[:] == '2019-11-27']
print("a")