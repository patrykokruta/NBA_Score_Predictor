from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import tenorflow
teamA = input()
teamB = input()

nba_teams = teams.get_teams()
#print(nba_teams)
#Select the dictionary for the Celtics, which contains their team ID
MteamA = [team for team in nba_teams if team['abbreviation'] == teamA][0]
teamA_Id = teamA['id']

# Query for games where the Celtics were playing
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=teamA_Id)
# The first DataFrame of those returned is what we want.
games = gamefinder.get_data_frames()[0]
games.head()

#games_1718 = games[games.SEASON_ID.str[-4:] == '2018' ]
games_1718 = games
games_1718.head()

teamB_games_1718 = games_1718[games_1718.MATCHUP.str.contains(teamB)]
teamB_games_1718.head()

winCounter=0
loseCounter=0

#gameCount = teamB_games_1718.filter(like='W', axis=0).count
teamA_games_WON =teamB_games_1718[teamB_games_1718.WL =='W'].WL.count()
teamA_games_LOST = teamB_games_1718[teamB_games_1718.WL =='L'].WL.count()
#licznik = teamA_games_WON.WL.count()
print(teamA_games_WON/teamB_games_1718.WL.count())
print(teamA_games_LOST/teamB_games_1718.WL.count())
print(teamB_games_1718.WL.count())
#winCounter = teamB_games_1718[teamB_games_1718.WL=='W'].count

#loseCounter = count(teamB_games_1718.WL['W'])
#print(loseCounter)