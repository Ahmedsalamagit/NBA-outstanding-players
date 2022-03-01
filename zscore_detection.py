import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df_players = pd.read_csv("data/player_regular_season.txt")
df_players.head()

pts = df_players["pts"]
reb = df_players["reb"]
asts = df_players["asts"]
stl = df_players["stl"]
blk = df_players["blk"]
fga = df_players["fga"]
fgm = df_players["fgm"]
fta = df_players["fta"]
ftm = df_players["ftm"]
turnover = df_players["turnover"]
gp = df_players["gp"]

# Formula for player efficiency rating below
# Efficiency = ( ( points + rebounds + assists + steals + blocks ) - ( ( fieldgoal_atttempts – fieldgoals_made ) + ( freethrow_attempts – freethrows_made ) + turnover ) ) / games_played
efficiencies = ((pts + reb + asts + stl + blk) - ((fga - fgm) + (fta - ftm) + turnover)) / gp
efficiencies = efficiencies.to_frame()
efficiencies.columns = ["efficiency"]


player_eff = pd.concat([df_players[["firstname", "lastname"]], efficiencies], axis=1)

## detecting outliers through a z-score method
#zScores = np.abs(stats.zscore(player_eff["efficiency"]))
zScores = np.abs((player_eff["efficiency"] - player_eff["efficiency"].mean()) / player_eff["efficiency"].std(ddof=0))
print(zScores)
outlier = []
zthreshold = 3
index = 0
outstanding_Zscore = np.where(zScores > zthreshold)
outstanding_players_Zscore = pd.concat([ player_eff["firstname"][outstanding_Zscore[0]], player_eff["lastname"][outstanding_Zscore[0]] ], axis=1)

outstanding_players_Zscore = outstanding_players_Zscore.drop_duplicates()
print(outstanding_players_Zscore)