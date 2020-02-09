from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder



def get_all_games_between_two_teams(teamA, teamB):


    nba_teams = teams.get_teams()
    #print(nba_teams)
    #Select the dictionary for the Celtics, which contains their team ID
    teamA = [team for team in nba_teams if team['abbreviation'] == teamA][0]
    teamA_Id = teamA['id']

    # Query for games where the Celtics were playing
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=teamA_Id)
    # The first DataFrame of those returned is what we want.
    games = gamefinder.get_data_frames()[0]
    games.head()


    games_1718 = games
   # games_1718.head()

    teamB_games_1718 = games_1718[games_1718.MATCHUP.str.contains(teamB)]
    # teamB_games_1718.head()
    return teamB_games_1718
    win_counter = 0
    lose_counter = 0

    # gameCount = teamB_games_1718.filter(like='W', axis=0).count
    # teamA_games_WON =teamB_games_1718[teamB_games_1718.WL =='W'].WL.count()
    # teamA_games_LOST = teamB_games_1718[teamB_games_1718.WL =='L'].WL.count()
    # licznik = teamA_games_WON.WL.count()
    # print(teamA_games_WON/teamB_games_1718.WL.count())
    # print(teamA_games_LOST/teamB_games_1718.WL.count())
    # print(teamB_games_1718.WL.count())
# winCounter = teamB_games_1718[teamB_games_1718.WL=='W'].count

# loseCounter = count(teamB_games_1718.WL['W'])
# print(loseCounter)

def probability_a(all_games):
        teamA_games_WON = all_games[all_games.WL == 'W'].WL.count()
        teamA_games_LOST = all_games[all_games.WL == 'L'].WL.count()
        # licznik = teamA_games_WON.WL.count()
        teamA_games_WON_Probability = teamA_games_WON / all_games.WL.count()
        #print(teamA_games_WON / all_games.WL.count())
        #print(teamA_games_LOST / all_games.WL.count())
        #print(all_games.WL.count())
        #print(teamA_games_WON)
        return teamA_games_WON, teamA_games_WON_Probability

def probability_ab(all_games,teamA_games_WON): # condition that team A lost to team B when lost the previous match against them
        print("probAB")
        #  teamA_games_lost_when_lost_pr_match = all_games[all_games.WL == 'L'].WL.count()
        incr = all_games.WL.count()
        wongames = 0
        k = 0
        for n in range(incr-1):

            if all_games.iloc[k].WL == 'W' and all_games.iloc[k+1].WL == 'W':
                wongames = wongames + 1
            k=k+1

        probability_game_wontwice =  wongames/teamA_games_WON
        return wongames, probability_game_wontwice

def probability_ac(all_games, teamAwon):  # condition that team A lost to team B when lost the previous match against them
    print("probAc")
    #  teamA_games_lost_when_lost_pr_match = all_games[all_games.WL == 'L'].WL.count()
    incr = all_games.WL.count()
    lostgames = 0
    k = 0
    for n in range(incr - 2):

        if all_games.iloc[k].WL == 'W' and all_games.iloc[k + 1].WL == 'W' and all_games.iloc[k+2].WL == "W":
            lostgames = lostgames + 1
        k = k + 1

    prob=lostgames/teamAwon

    return lostgames, prob