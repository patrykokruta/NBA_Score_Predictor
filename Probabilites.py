# This script is counting diffrent probabilities of certain events
# A:team A  lost on condition that lost last game
# B: team A  lost on condition that lost 3 of 5 last games
# C: team A  lost on condition that played two games in row
# D: team A  lost on condition that
# E: team A  lost on condition that
from Sezon2TeamsCount import get_all_games_between_two_teams as games
from Sezon2TeamsCount import probability_a as pra
from Sezon2TeamsCount import probability_ab as prab
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.http import NBAStatsResponse
import pandas as pd
from pandas import DataFrame
# NBAStatsHTTP.clean_contents()
# NBAStatsResponse.get_response()
# conditional probability
# P(A|B) = P(A)*P(B) /P(B)

# 1 function for getting all games
# 2 choose team
# 3 choose opponnent
# 3 check how many games where lost after losing a game !
# 4 count probablity
print("Pass to team names: ")
teamAA = input()
teamBB = input()

tryme = games(teamAA, teamBB)
df = DataFrame(tryme)

export = df.to_excel("output.xlsx", index = None, header=True)
#exp=tryme.to_excel("output2.xlsx")
print("halo")
#pra(tryme)

# prab(tryme)