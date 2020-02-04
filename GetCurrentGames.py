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
Currentgames = games[games.GAME_DATE.str[:] == '2020-02-04']

#a = ScoreboardV2(game_date="2020-2-5",).last_meeting.data
b = ScoreboardV2(game_date="2020-2-4",).last_meeting.data
print(Currentgames)

print(b)