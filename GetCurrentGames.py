from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import DayOffset, GameDate, LeagueID
from nba_api.stats.endpoints import ScoreboardV2

nba_teams = teams.get_teams()
#league_id_nullable="00",
gamefinder = leaguegamefinder.LeagueGameFinder(league_id_nullable="00")
games = gamefinder.get_data_frames()[0]
games.head()
Currentgames = games[games.GAME_DATE.str[:] == '2020-01-16']

a = ScoreboardV2(game_date="2019-12-3",).last_meeting.data
print(Currentgames)
