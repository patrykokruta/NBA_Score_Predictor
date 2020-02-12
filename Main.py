# This is Main script.

from datetime import date
from CountProbabilites import get_all_games_between_two_teams as games
from CountProbabilites import probability_a
from CountProbabilites import *
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.http import NBAStatsResponse
import pandas as pd
from pandas import DataFrame
from GetCurrentGames import get_current_games

today = date.today()
print("Desired date format: " + str(today))

print("Chose date")
dt = input()
current_games = get_current_games(dt)

print(current_games)
print("Choose game:")
chosen_game = input()
teamAA = current_games.iloc[int(chosen_game)].teamA
teamBB = current_games.iloc[int(chosen_game)].teamB
print("Choosen game:" + teamAA + " vs " + teamBB )

allgamesteamA = all_games_of_one_team(teamAA)
allgames = games(teamAA, teamBB)
teamA_all_games_won_with_teamB, p_a = probability_a(allgames)
teamA_games_won_twice_with_teamB, p_ab = probability_ab(allgames, teamA_all_games_won_with_teamB)
teamA_games_won_thrice_with_teamB, p_ac = probability_ac(allgames, teamA_games_won_twice_with_teamB)
wintotal, p_ad = probability_ad(allgamesteamA)
wintotaltwice, p_ae = probability_ae(allgamesteamA,wintotal)
wintotalthrice, p_af = probability_af(allgamesteamA,wintotaltwice)
p_ag = probability_ag(allgames)
p_ah = probability_ah(allgamesteamA)

Pwin = count_win_probability(p_a, p_ab, p_ac, p_ad, p_ae, p_af, p_ag, p_ah)
Plose = count_lose_probability(p_a, p_ab, p_ac, p_ad, p_ae, p_af, p_ag, p_ah)
compare = compare_probabilities(Pwin,Plose)
if compare == 1:
    print(teamAA + " is likely to win")
else:
    print(teamAA + " is likely to lose")



