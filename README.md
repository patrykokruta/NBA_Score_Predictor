# NBA_Score_Predictor

## Configuration
In order to use this project it is necessary to have the following libraries:\
pandas\
numpy\
nba-api https://pypi.org/project/nba-api/ (newest version)

## About project
This program uses nba-api to get historical data about NBA games from website https://www.nba.com/scores#/.
In order to predict the probability of one team winning with the other you have to run Main script insert the date of the  match and choose the teams. The output is which team is more likly to win. It is based on Naive-Bayes algorithm. 

## Useful information  
P(A) - probability that team A wins a match with team B  
P(A|B) - probability that team A wins a match on condition that won last match with team B  
P(A|C) - probability that team A wins a match on condition that won two matches in row with team B  
P(A|D) - probability that team A wins their match (total)\
P(A|E) - probabilty that team A wins their match on conditon that won their last match\
P(A|F) - probabilty that team A wins their match on conditon that won their last two matches\
P(A|G) - probability that team A wins their match with team B on condition that it is home game\
P(A|H) probability that team A wins match on conditon that they played overtime last game\

