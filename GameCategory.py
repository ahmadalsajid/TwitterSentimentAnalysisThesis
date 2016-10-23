# game list and its hashtags
games = {
    # MMO
    'WorldOfWarcraft': ['#Warcraft',],
    'StarWars': ['#StarWars', '#RogueOne'],
    'TERA': ['#TERA',],
    'PlanetArkadia': ['#planetarkadia',],
    'WorldOfTanks': ['#worldoftanks',],
    'EchoOfSoul':['#EchoOfSoul',],
    'rift': ['#riftgame', '#rift'],
    'Skyforge':['#Skyforge',],
    '4story': ['#4story',],
    'counterstrike':['#CounterStrike','#CounterStrikeGlobalOffensive','#CSGO','#CSGlobalOffensive','#CounterStrikeGo '],
    # simulation
    'JurassicWorldTheGame': ['#JurassicWorldGame',],
    'SimCity':['#SimCity',],
    'GoatSimulator': ['#GoatSimulator',],
    'InfiniteFlightSimulator': ['#InfiniteFlightSimulator','#infiniteflight'],
    'AssettoCorsa': ['#AssettoCorsa',],
    'eurotrucksimulator':['#eurotrucksimulator', '#eurotrucksimulator2', '#ETS2'],
    'SilentHunter4': ['#SilentHunter4',],
    'FlightSimulatorX':['#flightsimulatorx',],
    'MotorsportManager': ['#MotorsportManager',],
    'FootballManager2015': ['#FootballManager2015',],
    # Adventure
    '#DeadEffect2': ['#DeadEffect2',],
    '#GrandTheftAuto': ['#GrandTheftAuto','#GTA','#GTAOnline','#GTAV'],
    '#LaraCroftGo': ['#LaraCroftGo',],
    '#Samorost3': ['#Samorost3',],
    '#KingsQuest': ['#KingsQuest',],
    '#GeminiRue': ['#GeminiRue',],
    '#Panmorphia': ['#Panmorphia',],
    # Real-Time Strategy (RTS)
    'ClashofClans': ['#clashclans','#ClashOn','#ClashOfClans'],
    'TotalWarBattlesKingdom': ['#totalwar','#TotalWarBattlesKingdom'],
    'AutumnDynasty': ['#AutumnDynasty',],
    'CallofChampions': ['#CallofChampions',],
    'chessfree': ['#chessfree',],
    'Machines at War 3': ['#MachinesatWar3',],
    'ClashRoyale': ['#ClashRoyale',],
    # Puzzle
    'HitmanGO': ['#HitmanGO',],
    'MonumentValley': ['#MonumentValleyGame',],
    'TheRoom2': ['#TheRoom2',],
    'cuttherope': ['#cuttherope',],
    'Colorfy': ['#Colorfy',],
    'Q.U.B.E.': ['#QuBeGame',],
    'BrainAge': ['#BrainAge',],
    'Peggle': ['#Peggle','#Peggle2'],
    # Action
    'Titanfall2': ['#Titanfall','#Titanfall2'],
    'NeedForSpeed': ['#NeedForSpeedMostWanted','#NFSMostWanted','#NFSMW','#NeedforSpeed','#nfs'],
    'Battlefield': ['#BATTLEFIELD1', '#BATTLEFIELD2', '#BATTLEFIELD3', '#BATTLEFIELD4', '#BATTLEFIELDHARDLINE', '#BF1',
                    '#BF2', '#BF3', '#BF4',],
    'dragonage': ['#dragonage','#dragonage2'],
    'DeadSpace': ['#DeadSpace', '#DeadSpace1', '#DeadSpace2', '#DeadSpace3',],
    'XCOM2': ['#XCOM', '#XCOM2',],
    'Badland': ['#Badland','#Badland2'],
    'HalfLife': ['#HalfLife2', '#HalfLife', '#HalfLife3',],
    'IntotheDead': ['#IntotheDead',],
    'MirrorsEdge': ['#MirrorsEdge',],
    # Browser games
    'ROBLOX': ['#ROBLOX', '#ROBLOXDev',],
    'AnimalJam': ['#AnimalJam',],
    'EightBallPool': ['#EightBallPool','#8ballPool'],
    'MafiaReturns': ['#MafiaReturns',],
    'TownofSalem': ['#TownofSalem',],
    'slitherio': ['#slitherio',],
    'MightandMagic': ['#MightandMagic',],
    'candyCrushsodasaga': ['#candyCrushsodasaga', '#candyCrushsoda','#candyCrush'],
    # Sports
    'FIFA': ['#FIFA10','#FIFA11','#FIFA12','#FIFA13','#FIFA14,''#FIFA15','#FIFA16','#FIFA17'],
    'ProEvolutionSoccer': ['#PES14', '#PES15', '#PES16', '#PES17'],
    # Shooter
    'Doom': ['#Doom',],
    'CriticalOps': ['#CriticalOps', '#CriticalOpsGame', '#CriticalOpsFireteams'],
    'DeadEffect2': ['#DeadEffect2','#DeadEffect'],
    'deadtrigger': ['#deadtrigger', '#deadtrigger2'],
    'hitman': ['#hitman', '#hitmansniper'],
    'moderncombat': ['#moderncombat', '#moderncombat5', '#mc5',],
    'BlitzBrigade': ['#BlitzBrigade'],
    # Role-Playing (RPG)
    'Pokemongo': ['#Pokemongo',],
    'BaldursGate': ['#BaldursGate','#BaldursGate2'],
    'TheBardsTale': ['#TheBardsTale','#TheBardsTaleiv'],
    'MobiusFinalFantasy': ['#FFXV','#finalfantasy','#FinalFantasyX','#MobiusFF','#MobiusFinalFantasy'],
    'ChaosRings3': ['#ChaosRingsiii','#ChaosRings3'],
    'TheWitcher': ['#TheWitcher2','#TheWitcher','#TheWitcher3W','#TheWitcher3'],
    'Fallout': ['#FalloutNewVegas','#FalloutNV','#foNewVegas','#Fallout4','#Fallout3','#Fallout2'],
    'PlanescapeTorment': ['#PlanescapeTorment',],
}

hashtag_list = []
for name in games:
    for hasht in games[name]:
        hashtag_list.append(hasht)
# print(sorted(hashtag_list))
# print(len(hashtag_list))
all_hashtags = ['#4story', '#8ballPool', '#AnimalJam', '#AssettoCorsa', '#AutumnDynasty', '#BATTLEFIELD1 #BATTLEFIELD2',
                '#BATTLEFIELD3', '#BATTLEFIELD4', '#BATTLEFIELDHARDLINE', '#BF1', '#BF2', '#BF3', '#BF4', '#Badland',
                '#Badland2', '#BaldursGate', '#BaldursGate2', '#BlitzBrigade', '#BrainAge', '#CSGO',
                '#CSGlobalOffensive', '#CallofChampions', '#ChaosRings3', '#ChaosRingsiii', '#ClashOfClans', '#ClashOn',
                '#ClashRoyale', '#Colorfy', '#CounterStrike', '#CounterStrikeGlobalOffensive', '#CounterStrikeGo ',
                '#CriticalOps', '#CriticalOpsFireteams', '#CriticalOpsGame', '#DeadEffect', '#DeadEffect2',
                '#DeadEffect2', '#DeadSpace', '#DeadSpace1', '#DeadSpace2', '#DeadSpace3', '#Doom', '#ETS2',
                '#EchoOfSoul', '#EightBallPool', '#FFXV', '#FIFA10', '#FIFA11', '#FIFA12', '#FIFA13', '#FIFA14,#FIFA15',
                '#FIFA16', '#FIFA17', '#Fallout2', '#Fallout3', '#Fallout4', '#FalloutNV', '#FalloutNewVegas',
                '#FinalFantasyX', '#FootballManager2015', '#GTA', '#GTAOnline', '#GTAV', '#GeminiRue', '#GoatSimulator',
                '#GrandTheftAuto', '#HalfLife', '#HalfLife2', '#HalfLife3', '#HitmanGO', '#InfiniteFlightSimulator',
                '#IntotheDead', '#JurassicWorldGame', '#KingsQuest', '#LaraCroftGo', '#MachinesatWar3', '#MafiaReturns',
                '#MightandMagic', '#MirrorsEdge', '#MobiusFF', '#MobiusFinalFantasy', '#MonumentValleyGame',
                '#MotorsportManager', '#NFSMW', '#NFSMostWanted', '#NeedForSpeedMostWanted', '#NeedforSpeed',
                '#PES14', '#PES15', '#PES16', '#PES17', '#Panmorphia', '#Peggle', '#Peggle2', '#PlanescapeTorment',
                '#Pokemongo', '#QuBeGame', '#ROBLOX', '#ROBLOXDev', '#RogueOne', '#Samorost3 ', '#SilentHunter4',
                '#SimCity', '#Skyforge', '#StarWars', '#TERA', '#TheBardsTale', '#TheBardsTaleiv', '#TheRoom2',
                '#TheWitcher', '#TheWitcher2', '#TheWitcher3', '#TheWitcher3W', '#Titanfall', '#Titanfall2',
                '#TotalWarBattlesKingdom', '#TownofSalem', '#Warcraft', '#XCOM', '#XCOM2', '#candyCrush',
                '#candyCrushsoda', '#candyCrushsodasaga', '#chessfree', '#clashclans', '#cuttherope', '#deadtrigger',
                '#deadtrigger2', '#dragonage', '#dragonage2', '#eurotrucksimulator', '#eurotrucksimulator2',
                '#finalfantasy', '#flightsimulatorx', '#foNewVegas', '#hitman', '#hitmansniper', '#infiniteflight',
                '#mc5', '#moderncombat', '#moderncombat5', '#nfs', '#planetarkadia', '#rift', '#riftgame', '#slitherio',
                '#totalwar', '#worldoftanks']
# print(len(all_hashtags))
#
# game_name = [str(name) for name in games.keys()]
# print(len(game_name))
