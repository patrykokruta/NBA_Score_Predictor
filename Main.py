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
from GetCurrentGames import get_current_games

# 1 function for getting all games
# 2 choose team
# 3 choose opponnent
# 3 check how many games where lost after losing a game !
# 4 count probablity
#(p_a, p_ab, p_ac, p_ad, p_ae, p_af, p_ag, p_ah) = 0

current_games = get_current_games()
print(current_games)
print("Choose game:")
chosen_game = input()
teamAA = current_games.iloc[int(chosen_game)].teamA
teamBB = current_games.iloc[int(chosen_game)].teamB
print("Choosen game:" + teamAA + " vs " + teamBB )
allgamesteamA = all_games_of_one_team(teamAA)
allgames = games(teamAA, teamBB)
teamA_all_games_won_with_teamB, p_a = probability_a(allgames)
#print(a, b)
teamA_games_won_twice_with_teamB, p_ab = probability_ab(allgames, teamA_all_games_won_with_teamB)
#print(c, d)
teamA_games_won_thrice_with_teamB, p_ac = probability_ac(allgames, teamA_games_won_twice_with_teamB)
#print(e, f)

wintotal, p_ad = probability_ad(allgamesteamA)
wintotaltwice, p_ae = probability_ae(allgamesteamA,wintotal)
wintotalthrice, p_af = probability_af(allgamesteamA,wintotaltwice)


p_ag = probability_ag(allgames)
#print(homewins)

p_ah = probability_ah(allgamesteamA)

Pwin = p_a*p_ab*p_ac*p_ad*p_ae*p_af*p_ag*p_ah
Plose = (1-p_a)*(1-p_ab)*(1-p_ac)*(1-p_ad)*(1-p_ae)*(1-p_af)*(1-p_ag)*(1-p_ah)
print(Pwin, Plose)
if Pwin > Plose:
    print(teamAA+" wins")
else:
    print(teamBB + " wins")
#print(overtimewins)
#SAVING DATA TO EXCEL
#df = DataFrame(tryme)
#export = df.to_excel("output.xlsx", index = None, header=True)
#exp=tryme.to_excel("output2.xlsx")

