# This script is counting diffrent probabilities of certain events
# A:team A  lost on condition that lost last game
# B: team A  lost on condition that lost 3 of 5 last games
# C: team A  lost on condition that played two games in row
# D: team A  lost on condition that
# E: team A  lost on condition that
from CountProbabilites import get_all_games_between_two_teams as games
from CountProbabilites import probability_a
from CountProbabilites import *

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

allgamesteamA = all_games_of_one_team(teamAA)
allgames = games(teamAA, teamBB)
a, b =probability_a(allgames)
print(a, b)
c, d=probability_ab(allgames, a)
print(c, d)
e, f = probability_ac(allgames, c)
print(e, f)

wintotal, probability = probability_ad(allgamesteamA)
wintotaltwice, probabilitytwice = probability_ae(allgamesteamA,wintotal)
wintotalthrice, probabilitythrice = probability_af(allgamesteamA,wintotaltwice)
print(wintotal,probability)
print(probabilitytwice,wintotaltwice)
print(wintotalthrice,probabilitythrice)

homewins = probability_ag(allgames)
print(homewins)

overtimewins = probability_ah(allgamesteamA)
print(overtimewins)
#SAVING DATA TO EXCEL
#df = DataFrame(tryme)
#export = df.to_excel("output.xlsx", index = None, header=True)
#exp=tryme.to_excel("output2.xlsx")

