from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

def all_games_of_one_team(teamA):
    nba_teams = teams.get_teams()
    teamA = [team for team in nba_teams if team['abbreviation'] == teamA][0]
    teamA_Id = teamA['id']
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=teamA_Id)
    games = gamefinder.get_data_frames()[0]
    return games


def get_all_games_between_two_teams(teamA, teamB):
    nba_teams = teams.get_teams()
    teamA = [team for team in nba_teams if team['abbreviation'] == teamA][0]
    teamA_Id = teamA['id']
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=teamA_Id)
    games = gamefinder.get_data_frames()[0]
    games.head()
    games_1718 = games
    teamB_games_1718 = games_1718[games_1718.MATCHUP.str.contains(teamB)]
    return teamB_games_1718


def probability_a(all_games):
    teamA_games_win = all_games[all_games.WL == 'W'].WL.count()
    teamA_games_win_probability = teamA_games_win / all_games.WL.count()
    return teamA_games_win, teamA_games_win_probability


def probability_ab(all_games, games_won_once):
    game_count = all_games.WL.count()
    won_games_twice = 0
    k = 0
    for n in range(game_count - 1):

        if all_games.iloc[k].WL == 'W' and all_games.iloc[k + 1].WL == 'W':
            won_games_twice = won_games_twice + 1
        k = k + 1

    probability_game_won_twice = won_games_twice / games_won_once
    return won_games_twice, probability_game_won_twice


def probability_ac(all_games, games_won_twice):  # condition that team A lost to team B when lost the previous match against them

    game_count = all_games.WL.count()
    games_won_thrice = 0
    k = 0
    for n in range(game_count - 2):

        if all_games.iloc[k].WL == 'W' and all_games.iloc[k + 1].WL == 'W' and all_games.iloc[k + 2].WL == "W":
            games_won_thrice = games_won_thrice + 1
        k = k + 1

    probability_games_won_thrice = games_won_thrice / games_won_twice

    return games_won_thrice, probability_games_won_thrice


def probability_ad(teamA_games):
    games_won_total = 0
    k = 0
    game_count = teamA_games.WL.count()
    for n in range(game_count):
        if teamA_games.iloc[k].WL == 'W':
            games_won_total = games_won_total + 1
        k = k+1

    probability_won_games_total = games_won_total/game_count
    return games_won_total, probability_won_games_total


def probability_ae(teamA_games, games_won_total):
    games_won_total_twice = 0
    k = 0
    game_count = teamA_games.WL.count()
    for n in range(game_count - 1):
        if teamA_games.iloc[k].WL == 'W' and teamA_games.iloc[k+1].WL == 'W':
            games_won_total_twice = games_won_total_twice + 1
        k = k+1

    probability_won_games_total_twice = games_won_total_twice/games_won_total
    return games_won_total_twice, probability_won_games_total_twice


def probability_af(teamA_games, games_won_total_twice):
    games_won_total_thrice = 0
    k = 0
    game_count = teamA_games.WL.count()
    for n in range(game_count - 2):
        if teamA_games.iloc[k].WL == 'W' and teamA_games.iloc[k+1].WL == 'W' and teamA_games.iloc[k+2].WL == 'W':
            games_won_total_thrice = games_won_total_thrice + 1
        k = k+1

    probability_won_games_total_thrice = games_won_total_thrice/games_won_total_twice
    return games_won_total_thrice, probability_won_games_total_thrice


def probability_ag(all_games):
    home_games_won = 0
    k = 0
    home_games = all_games[all_games.MATCHUP.str.contains('vs')]
    game_count = home_games.WL.count()
    for n in range(game_count):
        if all_games.iloc[k].WL == 'W':
            home_games_won = home_games_won + 1
        k = k + 1

    probability_home_games_won = home_games_won/game_count
    return probability_home_games_won


def probability_ah(teamA_games):
    #teamA_games_won = teamA_games[teamA_games.WL.str.contains('W')]
    after_overtime_games_won = 0
    overtime_games = 0
    k = 0
    game_count =  teamA_games.WL.count()

    for n in range(game_count - 1):
        if teamA_games.iloc[k].MIN > 245:
            overtime_games = overtime_games + 1
        if teamA_games.iloc[k].WL == 'W' and teamA_games.iloc[k].MIN > 245:
            after_overtime_games_won = after_overtime_games_won + 1
        k = k + 1

    probability_after_overtime_games_won = after_overtime_games_won/overtime_games
    print(overtime_games,after_overtime_games_won)
    return probability_after_overtime_games_won

