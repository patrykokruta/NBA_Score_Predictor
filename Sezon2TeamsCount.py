from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder


#teamA = input()
#teamB = input()

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
        # teamA_games_WON = all_games[all_games.WL == 'W'].WL.count()
        teamA_games_LOST = all_games[all_games.WL == 'L'].WL.count()
        # licznik = teamA_games_WON.WL.count()
        # print(teamA_games_WON / all_games.WL.count())
        print(teamA_games_LOST / all_games.WL.count())
        print(all_games.WL.count())


def probability_ab(all_games): # condition that team A lost to team B when lost the previous match against them
        print("probAB")
        #  teamA_games_lost_when_lost_pr_match = all_games[all_games.WL == 'L'].WL.count()
        lostgames = 0
        for n in  all_games.WL:
            k=0
            if all_games.iloc[k].WL == 'L' and all_games.iloc[k+1].WL == 'L':
                lostgames = lostgames + 1
            k = k+1

        print(lostgames)
         # print(all_games[all_games.GAME_ID == '0029201048'])
         #print(all_games[all_games == '2539'])
         #print(all_games.iloc[1])
         #print(all_games.iloc[0])
         #print(all_games.iloc[22])