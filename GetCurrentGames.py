from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import DayOffset, GameDate, LeagueID
from nba_api.stats.endpoints import ScoreboardV2
from datetime import date
import pandas as pd
import numpy as np

from pandas import DataFrame

today = date.today()
print(today)

def get_current_games():

    print("Chose date")
    datka = input()

    jutro = "2020-02-12"
    d = {'teamA' : [], 'teamB' :[]}
    #ff = DataFrame(columns=['teamA', 'teamB'])
    b = ScoreboardV2(game_date=datka,).last_meeting.data
    ran=b['data'].__len__()
    dff = DataFrame(index=np.arange(0,ran),columns=['teamA', 'teamB'])

    for n in range(ran):
        x = b['data'][n][6]
        y = b['data'][n][11]
        dff.iloc[n].teamA = y
        dff.iloc[n].teamB = x


    return dff