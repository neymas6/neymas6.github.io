## Data Analysis on NCAA basketball tournament dataset

import pandas as pd
import numpy as np

# read in data as df
bball = pd.read_csv('ncaa.csv',header=0,names=['Year','Round','RegionNumber',
                                               'RegionName','Team1Seed','Team1Score',
                                               'Team1','Team2','Team2Score',
                                               'Team2Seed'],engine='python') 




# find only winners
one = bball[bball['RegionName'] == 'Championship'] # get only games from the championship
team1winners = one[one['Team1Score'] - one['Team2Score'] > 0] # find the Team 1 winners
team2winners = one[one['Team1Score'] - one['Team2Score'] < 0] # find the Team 2 winners
pd.concat([team1winners['Team1'],team2winners['Team2']]).value_counts() 
    # combine the winners and find championships per school






# find top schools with most tournament appearances

round1 = bball[bball['Round'] == 1] # get only games from the first round
two_a = pd.DataFrame(round1['Team1'].copy()) # make a copy of the df from # 1
two_b = pd.DataFrame(round1['Team2'].copy()) # make a copy of the df from # 1
two_a.rename(columns={'Team1':'Team'}, inplace=True) # change the name of the col
two_b.rename(columns={'Team2':'Team'}, inplace=True) # change the name of the col
two = pd.concat([two_a,two_b]) # combine the two 
two['Team'].groupby(two['Team']).count().sort_values(ascending=False).iloc[0:11]






## average margin of victory per round

bball['MOV'] = np.abs(bball['Team1Score'] - bball['Team2Score']) # calculate the margin of victory
bball['MOV'].groupby(bball['Round']).mean() # find the average MOV per round






## average margin of victory for each champion

bball['Team1Year'] = bball['Team1'].map(str) + '-' + bball['Year'].map(str) # get Team-Year combination
bball['Team2Year'] = bball['Team2'].map(str) + '-' + bball['Year'].map(str) # get Team-Year combination

eight_a = pd.DataFrame(team1winners[['Team1','Year']].copy()) # make a copy of the df of champions
eight_b = pd.DataFrame(team2winners[['Team2','Year']].copy()) # make a copy of the df of champions
eight_a.rename(columns={'Team1':'Team'}, inplace=True) # rename the col
eight_b.rename(columns={'Team2':'Team'}, inplace=True) # rename the col
eight = pd.concat([eight_a,eight_b]) # combine the two dfs
eight['TeamYear'] = eight['Team'].map(str) + '-' + eight['Year'].map(str) # get Team-Year combination for champions

eight_merged1 = pd.merge(eight,bball,left_on='TeamYear',right_on='Team1Year',how='left') # left merge Team-Year of champions with all games
eight_merged2 = pd.merge(eight,bball,left_on='TeamYear',right_on='Team2Year',how='left') # left merge Team-Year of champions with all hames
eight_final = pd.concat([eight_merged1,eight_merged2]) # combine the two merged dfs
eight_final.dropna()['MOV'].groupby(eight_final['TeamYear']).mean().sort_values(ascending=False).iloc[0:10]
    # calculate the average Margin of Victory for each champion
