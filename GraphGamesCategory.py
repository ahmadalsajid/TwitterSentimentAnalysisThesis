# from time import clock
# start_time = clock()
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb
# total tweets
total = db.TSAtweets.find().count()
# irrelevant twit that does not contain any hashtag
irrelevent_tweet = db.TSAtweets.find({'entities.hashtags': [ ]}).count()
#actual tweets
total_tweet = total - irrelevent_tweet
# games categorized according to strategy
massive_multiplayer_online_game = db.TSAtweets.find(
    { "$or":
          [
              {'entities.hashtags.text': {'$regex': 'Warcraft', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'StarWars', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'RogueOne', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'TERA', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'planetarkadia', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'worldoftanks', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'EchoOfSoul', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'riftgame', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'rift', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'Skyforge', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': '4story', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'CounterStrike', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'CounterStrikeGlobalOffensive', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'CSGO', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'CSGlobalOffensive', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'CounterStrikeGo', '$options':'i'}},

          ]
    }).count()

simulation_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'JurassicWorldGame', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'SimCity', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'GoatSimulator', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'InfiniteFlightSimulator', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'infiniteflight', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'AssettoCorsa', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'eurotrucksimulator', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'eurotrucksimulator2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'ETS2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'SilentHunter4', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'flightsimulatorx', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MotorsportManager', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FootballManager2015', '$options':'i'}},
         ]
    }).count()

adventure_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'DeadEffect2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'GrandTheftAuto', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'GTA', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'GTAOnline', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'GTAV', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'LaraCroftGo', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Samorost3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'KingsQuest', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'GeminiRue', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Panmorphia', '$options':'i'}},
         ]
    }).count()

real_time_strategy_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'clashclans', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'ClashOn', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'ClashOfClans', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'totalwar', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TotalWarBattlesKingdom', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'AutumnDynasty', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'CallofChampions', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'chessfree', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MachinesatWar3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'ClashRoyale', '$options':'i'}},
         ]
    }).count()

puzzle_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'HitmanGO', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MonumentValleyGame', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TheRoom2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'cuttherope', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Colorfy', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'QuBeGame', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BrainAge', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Peggle', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Peggle2', '$options':'i'}},
         ]
    }).count()

action_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'Titanfall', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Titanfall2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'NeedForSpeedMostWanted', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'NFSMostWanted', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'NFSMW', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'NeedforSpeed', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'nfs', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BATTLEFIELD1', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BATTLEFIELD2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BATTLEFIELD3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BATTLEFIELD4', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BATTLEFIELDHARDLINE', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BF1', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BF2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BF3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BF4', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'dragonage', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'dragonage2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'DeadSpace', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'DeadSpace1', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'DeadSpace2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'DeadSpace3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'XCOM', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'XCOM2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Badland', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Badland2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'HalfLife2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'HalfLife', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'HalfLife3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'IntotheDead', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MirrorsEdge', '$options':'i'}},
         ]
    }).count()

browser_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'ROBLOX', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'ROBLOXDev', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'AnimalJam', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'EightBallPool', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': '8ballPool', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MafiaReturns', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TownofSalem', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'slitherio', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MightandMagic', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'candyCrushsodasaga', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'candyCrushsoda', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'candyCrush', '$options':'i'}},
         ]
    }).count()

sports_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'FIFA10', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FIFA11', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FIFA12', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FIFA13', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FIFA14', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FIFA15', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FIFA16', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FIFA17', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'PES14', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'PES15', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'PES16', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'PES17', '$options':'i'}},
         ]
    }).count()

shooter_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'Doom', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'CriticalOps', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'CriticalOpsGame', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'CriticalOpsFireteams', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'DeadEffect2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'DeadEffect', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'deadtrigger', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'deadtrigger2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'hitman', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'hitmansniper', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'moderncombat', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'moderncombat5', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'mc5', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BlitzBrigade', '$options':'i'}},
         ]
    }).count()

roll_playing_game = db.TSAtweets.find(
    { "$or":
         [
             {'entities.hashtags.text': {'$regex': 'Pokemongo', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BaldursGate', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'BaldursGate2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TheBardsTale', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TheBardsTaleiv', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FFXV', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'finalfantasy', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FinalFantasyX', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MobiusFF', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'MobiusFinalFantasy', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'ChaosRingsiii', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'ChaosRings3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TheWitcher2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TheWitcher', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TheWitcher3W', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'TheWitcher3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FalloutNewVegas', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'FalloutNV', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'foNewVegas', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Fallout4', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Fallout3', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'Fallout2', '$options':'i'}},
             {'entities.hashtags.text': {'$regex': 'PlanescapeTorment', '$options':'i'}},
         ]
    }).count()
# print(massive_multiplayer_online_game)
# print(simulation_game)
# print(adventure_game)
# print(real_time_strategy_game)
# print(puzzle_game)
# print(action_game)
# print(browser_game)
# print(sports_game)
# print(shooter_game)
# print(roll_playing_game)

# plot graph about categorized games
import matplotlib.pyplot as plt

df = {'type':['Massive Multiplayer Online', 'Simulation', 'Adventure_game', 'RealTime Strategy', 'Puzzle', 'Action',
              'Browser', 'Sports', 'Shooter', 'Roll Playing'] ,
            'count': [massive_multiplayer_online_game, simulation_game, adventure_game, real_time_strategy_game,
                      puzzle_game,action_game, browser_game, sports_game, shooter_game, roll_playing_game],
        }
# Create a figure with a single subplot
f, ax = plt.subplots(1, figsize=(10,5))
# Set bar width at 1
bar_width = 1
# positions of the left bar-boundaries
bar_l = [i for i in range(len(df['count']))]
# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width/2) for i in bar_l]
# Create the percentage of the total score the percentage value for each participant was
percentage = [(i / total_tweet) * 100 for i in df['count']]
# add percentage with names
for i in range(len(percentage)):
    tmp = df['type'][i]
    tmp = tmp+'  '+"%.2f" % percentage[i]+'%'
    df['type'][i] = tmp

# Create a bar chart in position bar_1
ax.bar(bar_l,
       # using percentage data
       percentage,
       # labeled
       label='Pre Score',
       # with alpha
       alpha=0.9,
       # with color
       color='#019600',
       # with bar width
       width=bar_width,
       # with border color
       edgecolor='white'
       )
# Set the ticks to be first names
plt.xticks(tick_pos, df['type'])
ax.set_ylabel("Percentage")
ax.set_xlabel("Category")
plt.title('Strategy based Category Percentage')
# Let the borders of the graphic
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.ylim(0, 45)
# rotate axis labels
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
# shot plot
plt.show()

# print("total time :",round(clock()-start_time,2),"seconds")