import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

#print(player_eff)

boxplot = sns.boxplot(x=player_eff["efficiency"])
boxplot.set_xlabel("Player Efficiency")

plt.show()

#tweakable parameter for determining outstanding players (EFF rating threshold)
threshold = 30


outstanding = np.where(player_eff["efficiency"] > threshold)


outstanding_players = pd.concat([ player_eff["firstname"][outstanding[0]], player_eff["lastname"][outstanding[0]] ], axis=1)

outstanding_players = outstanding_players.drop_duplicates()

print(outstanding_players)