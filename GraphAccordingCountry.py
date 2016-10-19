import pymongo
from time import clock
import matplotlib.pyplot as plt
start_time = clock()
client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb

country = {
    # country : time zones
    'Armenia' : ['Yerevan',],
    'Azerbaijan': ['Baku',],
    'Afghanistan' : ['Kabul',],
    'Africa' : ['Africa',],
    'Argentina' : ['Cordoba', 'Buenos Aires'],
    'America' : ['America','El_Salvador','Central America'],
    'Austria' : ['Vienna'],
    'Australia' : ['Melbourne','Adelaide','Canberra','Perth','Brisbane','Sydney'],
    'Bangladesh' : ['Dhaka',],
    'Belgium' : ['Brussels',],
    'Belarus': ['Minsk',],
    'Bolivia' : ['La Paz',],
    'Bosnia And Herzegovina': ['Sarajevo',],
    'Brazil' : ['Campo_Grande','Sao_Paulo','Brasilia'],
    'British Columbia' : ['Vancouver',],
    'Bulgaria' : ['Sofia',],
    'Canada' : ['Atikokan','Resolute','Atlantic Time (Canada)','Detroit','Vancouver','Dawson','Toronto','Newfoundland','Guadalajara','Saskatchewan','Edmonton'],
    'Central Africa' : ['West Central Africa'],
    'China' : ['Beijing','Urumqi'],
    'Chile': ['Santiago',],
    'Congo': ['Brazzaville',],
    'Colombia' : ['Bogota',],
    'Croatia' : ['Zagreb',],
    'Czech Republic' : ['Prague',],
    'Denmark' : ['Copenhagen',],
    'Ecuador' : ['Quito','Guayaquil',],
    'Egypt' : ['Cairo',],
    'Estonia' : ['Tallinn',],
    'France' : ['Paris',],
    'Finland' : ['Helsinki',],
    'Germany': ['Berlin',],
    'Georgia': ['Tbilisi',],
    'Greece' : ['Athens',],
    'Greenland' : ['Greenland',],
    'Guam' : ['Guam',],
    'Guatemala': ['Guatemala',],
    'Guyana' : ['Georgetown',],
    'Honiara' : ['Solomon Island',],
    'Iran' : ['Tehran',],
    'Iraq' : ['Baghdad',],
    'Italy' : ['Rome',],
    'India' : ['Kolkata','Mumbai','New Delhi','Calcutta','Chennai'],
    'Ireland' : ['Dublin',],
    'Indonesia': ['Jakarta',],
    'Israel': ['Jerusalem',],
    'Japan' : ['Sapporo','Tokyo','Osaka'],
    'Hong Kong' : ['Hong Kong',],
    'Hungary': ['Budapest',],
    'Kazakhastan' : ['Almaty',],
    'Kenya' : ['Nairobi',],
    'Kuwait' : ['Kuwait',],
    'Latvia' : ['Riga',],
    'Lithuania' : ['Vilnius',],
    'Malaysia' : ['Kuala Lumpur',],
    'Macedonia' : ['Skopje',],
    'Mid-Atlantic' : ['Mid-Atlantic',],
    'Mexico' : ['Chihuahua','Mazatlan','Monterrey','Tijuana','Chihuahua','Mexico City'],
    'Morocco' : ['Casablanca',],
    'Myanmar' : ['Rangoon',],
    'Nepal' : ['Kathmandu',],
    'Netherland' : ['Amsterdam',],
    'New Caledonia' : ['New Caledonia',],
    'New Zealand' : ['Wellington','Auckland'],
    'Nigeria' : ['Lagos',],
    'Oman' : ['Muscat',],
    'Pakistan' : ['Islamabad','Karachi',],
    'Papua New Guinea': ['Port Moresby',],
    'Portugal': ['Azores','Lisbon'],
    'Peru' : ['Lima',],
    'Poland' : ['Warsaw',],
    'Romania' : ['Bucharest',],
    'Russia' : ['Moscow','Saint Petersburg','Irkutsk','Volgograd','Yakutsk','Vladivostok','Novosibirsk','Ekaterinburg','Krasnoyarsk'] ,
    'Samoa' : ['Samoa',],
    'Spain' : ['Madrid',],
    'Scotland' : ['Edinburgh',],
    'Serbia' : ['Belgrade',],
    'Singapore' : ['Singapore',],
    'Saudi Arabia' : ['Riyadh',],
    'South Korea' : ['Seoul',],
    'Slovakia' : ['Bratislava',],
    'Slovenia' : ['Ljubljana',],
    'Sri Lanka' : ['Sri Jayawardenepura',],
    'South Africa' : ['Pretoria',],
    'Sweden' : ['Stockholm',],
    'Switzerland' : ['Bern',],
    'Taiwan': ['Taipei',],
    'Thailand' : ['Bangkok',],
    'Tonga' : ["Nuku'alofa",],
    'Turkey' : ['Istanbul',],
    'Venezuela': ['Caracas',],
    'Vietnam' : ['Hanoi',],
    'Ukrain' : ['Kiev',],
    'Uzbekistan' : ['Tashkent',],
    'United Arab Emirates' : ['Abu Dhabi',],
    'United Kingdom' : ['London',],
    'United States': ['Hawaii','Indiana (East)','Midway Island','Arizona','Chicago','New_York','Honolulu','Mid-Atlantic','Alaska','Denver','Boise','Los_Angeles'],
    'Zimbabwe' : ['Harare',],
}

user_country = dict()

########################################################################################################################
# code snippet 1 : used to generate code snippet 2
# with open('temp.py',"w") as f:
#     for c in country:
#         if len(country[c]) >1:
#             query = 'user_country["'+c+'"]  = db.TSAtweets.find({ "$or": ['
#             for t_z in country[c]:
#                 query+="{'user.time_zone': {'$regex': '"+t_z+"', '$options':'i'}},"
#             query += "]}).count()\n"
#         else:
#             query = 'user_country["'+c+'"]  = db.TSAtweets.find('+"{'user.time_zone': {'$regex': '"+country[c][0]+"', '$options':'i'}}).count()\n"
#         f.write(query)
#         tmp_str = 'print("people from '+c+' counted")\n'
#         f.write(tmp_str)
########################################################################################################################
# code snippet 2: count user according to country
user_country["Iraq"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Baghdad', '$options':'i'}}).count()
print("people from Iraq counted")
user_country["New Caledonia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'New Caledonia', '$options':'i'}}).count()
print("people from New Caledonia counted")
user_country["Austria"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Vienna', '$options':'i'}}).count()
print("people from Austria counted")
user_country["South Korea"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Seoul', '$options':'i'}}).count()
print("people from South Korea counted")
user_country["Mid-Atlantic"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Mid-Atlantic', '$options':'i'}}).count()
print("people from Mid-Atlantic counted")
user_country["Honiara"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Solomon Island', '$options':'i'}}).count()
print("people from Honiara counted")
user_country["Lithuania"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Vilnius', '$options':'i'}}).count()
print("people from Lithuania counted")
user_country["Hong Kong"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Hong Kong', '$options':'i'}}).count()
print("people from Hong Kong counted")
user_country["Bosnia And Herzegovina"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Sarajevo', '$options':'i'}}).count()
print("people from Bosnia And Herzegovina counted")
user_country["Kenya"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Nairobi', '$options':'i'}}).count()
print("people from Kenya counted")
user_country["Oman"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Muscat', '$options':'i'}}).count()
print("people from Oman counted")
user_country["Guam"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Guam', '$options':'i'}}).count()
print("people from Guam counted")
user_country["Uzbekistan"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Tashkent', '$options':'i'}}).count()
print("people from Uzbekistan counted")
user_country["Poland"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Warsaw', '$options':'i'}}).count()
print("people from Poland counted")
user_country["Estonia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Tallinn', '$options':'i'}}).count()
print("people from Estonia counted")
user_country["Greenland"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Greenland', '$options':'i'}}).count()
print("people from Greenland counted")
user_country["Slovenia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Ljubljana', '$options':'i'}}).count()
print("people from Slovenia counted")
user_country["Latvia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Riga', '$options':'i'}}).count()
print("people from Latvia counted")
user_country["Azerbaijan"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Baku', '$options':'i'}}).count()
print("people from Azerbaijan counted")
user_country["South Africa"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Pretoria', '$options':'i'}}).count()
print("people from South Africa counted")
user_country["Macedonia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Skopje', '$options':'i'}}).count()
print("people from Macedonia counted")
user_country["Congo"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Brazzaville', '$options':'i'}}).count()
print("people from Congo counted")
user_country["Turkey"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Istanbul', '$options':'i'}}).count()
print("people from Turkey counted")
user_country["Samoa"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Samoa', '$options':'i'}}).count()
print("people from Samoa counted")
user_country["British Columbia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Vancouver', '$options':'i'}}).count()
print("people from British Columbia counted")
user_country["Italy"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Rome', '$options':'i'}}).count()
print("people from Italy counted")
user_country["China"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Beijing', '$options':'i'}},{'user.time_zone': {'$regex': 'Urumqi', '$options':'i'}},]}).count()
print("people from China counted")
user_country["Australia"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Melbourne', '$options':'i'}},{'user.time_zone': {'$regex': 'Adelaide', '$options':'i'}},{'user.time_zone': {'$regex': 'Canberra', '$options':'i'}},{'user.time_zone': {'$regex': 'Perth', '$options':'i'}},{'user.time_zone': {'$regex': 'Brisbane', '$options':'i'}},{'user.time_zone': {'$regex': 'Sydney', '$options':'i'}},]}).count()
print("people from Australia counted")
user_country["Kazakhastan"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Almaty', '$options':'i'}}).count()
print("people from Kazakhastan counted")
user_country["Ecuador"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Quito', '$options':'i'}},{'user.time_zone': {'$regex': 'Guayaquil', '$options':'i'}},]}).count()
print("people from Ecuador counted")
user_country["Thailand"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Bangkok', '$options':'i'}}).count()
print("people from Thailand counted")
user_country["France"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Paris', '$options':'i'}}).count()
print("people from France counted")
user_country["Kuwait"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Kuwait', '$options':'i'}}).count()
print("people from Kuwait counted")
user_country["Belarus"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Minsk', '$options':'i'}}).count()
print("people from Belarus counted")
user_country["Colombia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Bogota', '$options':'i'}}).count()
print("people from Colombia counted")
user_country["Israel"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Jerusalem', '$options':'i'}}).count()
print("people from Israel counted")
user_country["New Zealand"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Wellington', '$options':'i'}},{'user.time_zone': {'$regex': 'Auckland', '$options':'i'}},]}).count()
print("people from New Zealand counted")
user_country["Pakistan"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Islamabad', '$options':'i'}},{'user.time_zone': {'$regex': 'Karachi', '$options':'i'}},]}).count()
print("people from Pakistan counted")
user_country["Singapore"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Singapore', '$options':'i'}}).count()
print("people from Singapore counted")
user_country["Guyana"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Georgetown', '$options':'i'}}).count()
print("people from Guyana counted")
user_country["Slovakia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Bratislava', '$options':'i'}}).count()
print("people from Slovakia counted")
user_country["Guatemala"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Guatemala', '$options':'i'}}).count()
print("people from Guatemala counted")
user_country["Belgium"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Brussels', '$options':'i'}}).count()
print("people from Belgium counted")
user_country["Sri Lanka"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Sri Jayawardenepura', '$options':'i'}}).count()
print("people from Sri Lanka counted")
user_country["Egypt"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Cairo', '$options':'i'}}).count()
print("people from Egypt counted")
user_country["Switzerland"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Bern', '$options':'i'}}).count()
print("people from Switzerland counted")
user_country["Tonga"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Nuku\'alofa', '$options':'i'}}).count()
print("people from Tonga counted")
user_country["America"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'America', '$options':'i'}},{'user.time_zone': {'$regex': 'El_Salvador', '$options':'i'}},{'user.time_zone': {'$regex': 'Central America', '$options':'i'}},]}).count()
print("people from America counted")
user_country["India"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Kolkata', '$options':'i'}},{'user.time_zone': {'$regex': 'Mumbai', '$options':'i'}},{'user.time_zone': {'$regex': 'New Delhi', '$options':'i'}},{'user.time_zone': {'$regex': 'Calcutta', '$options':'i'}},{'user.time_zone': {'$regex': 'Chennai', '$options':'i'}},]}).count()
print("people from India counted")
user_country["Brazil"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Campo_Grande', '$options':'i'}},{'user.time_zone': {'$regex': 'Sao_Paulo', '$options':'i'}},{'user.time_zone': {'$regex': 'Brasilia', '$options':'i'}},]}).count()
print("people from Brazil counted")
user_country["Finland"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Helsinki', '$options':'i'}}).count()
print("people from Finland counted")
user_country["Netherland"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Amsterdam', '$options':'i'}}).count()
print("people from Netherland counted")
user_country["Vietnam"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Hanoi', '$options':'i'}}).count()
print("people from Vietnam counted")
user_country["Chile"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Santiago', '$options':'i'}}).count()
print("people from Chile counted")
user_country["Nigeria"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Lagos', '$options':'i'}}).count()
print("people from Nigeria counted")
user_country["Saudi Arabia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Riyadh', '$options':'i'}}).count()
print("people from Saudi Arabia counted")
user_country["Spain"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Madrid', '$options':'i'}}).count()
print("people from Spain counted")
user_country["Ireland"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Dublin', '$options':'i'}}).count()
print("people from Ireland counted")
user_country["United States"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Hawaii', '$options':'i'}},{'user.time_zone': {'$regex': 'Indiana (East)', '$options':'i'}},{'user.time_zone': {'$regex': 'Midway Island', '$options':'i'}},{'user.time_zone': {'$regex': 'Arizona', '$options':'i'}},{'user.time_zone': {'$regex': 'Chicago', '$options':'i'}},{'user.time_zone': {'$regex': 'New_York', '$options':'i'}},{'user.time_zone': {'$regex': 'Honolulu', '$options':'i'}},{'user.time_zone': {'$regex': 'Mid-Atlantic', '$options':'i'}},{'user.time_zone': {'$regex': 'Alaska', '$options':'i'}},{'user.time_zone': {'$regex': 'Denver', '$options':'i'}},{'user.time_zone': {'$regex': 'Boise', '$options':'i'}},{'user.time_zone': {'$regex': 'Los_Angeles', '$options':'i'}},]}).count()
print("people from United States counted")
user_country["Malaysia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Kuala Lumpur', '$options':'i'}}).count()
print("people from Malaysia counted")
user_country["Taiwan"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Taipei', '$options':'i'}}).count()
print("people from Taiwan counted")
user_country["Armenia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Yerevan', '$options':'i'}}).count()
print("people from Armenia counted")
user_country["Ukrain"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Kiev', '$options':'i'}}).count()
print("people from Ukrain counted")
user_country["United Kingdom"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'London', '$options':'i'}}).count()
print("people from United Kingdom counted")
user_country["Denmark"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Copenhagen', '$options':'i'}}).count()
print("people from Denmark counted")
user_country["Hungary"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Budapest', '$options':'i'}}).count()
print("people from Hungary counted")
user_country["Nepal"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Kathmandu', '$options':'i'}}).count()
print("people from Nepal counted")
user_country["Morocco"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Casablanca', '$options':'i'}}).count()
print("people from Morocco counted")
user_country["Scotland"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Edinburgh', '$options':'i'}}).count()
print("people from Scotland counted")
user_country["Papua New Guinea"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Port Moresby', '$options':'i'}}).count()
print("people from Papua New Guinea counted")
user_country["Argentina"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Cordoba', '$options':'i'}},{'user.time_zone': {'$regex': 'Buenos Aires', '$options':'i'}},]}).count()
print("people from Argentina counted")
user_country["Portugal"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Azores', '$options':'i'}},{'user.time_zone': {'$regex': 'Lisbon', '$options':'i'}},]}).count()
print("people from Portugal counted")
user_country["Canada"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Atikokan', '$options':'i'}},{'user.time_zone': {'$regex': 'Resolute', '$options':'i'}},{'user.time_zone': {'$regex': 'Atlantic Time (Canada)', '$options':'i'}},{'user.time_zone': {'$regex': 'Detroit', '$options':'i'}},{'user.time_zone': {'$regex': 'Vancouver', '$options':'i'}},{'user.time_zone': {'$regex': 'Dawson', '$options':'i'}},{'user.time_zone': {'$regex': 'Toronto', '$options':'i'}},{'user.time_zone': {'$regex': 'Newfoundland', '$options':'i'}},{'user.time_zone': {'$regex': 'Guadalajara', '$options':'i'}},{'user.time_zone': {'$regex': 'Saskatchewan', '$options':'i'}},{'user.time_zone': {'$regex': 'Edmonton', '$options':'i'}},]}).count()
print("people from Canada counted")
user_country["Bulgaria"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Sofia', '$options':'i'}}).count()
print("people from Bulgaria counted")
user_country["Bolivia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'La Paz', '$options':'i'}}).count()
print("people from Bolivia counted")
user_country["Afghanistan"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Kabul', '$options':'i'}}).count()
print("people from Afghanistan counted")
user_country["Czech Republic"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Prague', '$options':'i'}}).count()
print("people from Czech Republic counted")
user_country["Bangladesh"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Dhaka', '$options':'i'}}).count()
print("people from Bangladesh counted")
user_country["Russia"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Moscow', '$options':'i'}},{'user.time_zone': {'$regex': 'Saint Petersburg', '$options':'i'}},{'user.time_zone': {'$regex': 'Irkutsk', '$options':'i'}},{'user.time_zone': {'$regex': 'Volgograd', '$options':'i'}},{'user.time_zone': {'$regex': 'Yakutsk', '$options':'i'}},{'user.time_zone': {'$regex': 'Vladivostok', '$options':'i'}},{'user.time_zone': {'$regex': 'Novosibirsk', '$options':'i'}},{'user.time_zone': {'$regex': 'Ekaterinburg', '$options':'i'}},{'user.time_zone': {'$regex': 'Krasnoyarsk', '$options':'i'}},]}).count()
print("people from Russia counted")
user_country["Greece"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Athens', '$options':'i'}}).count()
print("people from Greece counted")
user_country["Iran"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Tehran', '$options':'i'}}).count()
print("people from Iran counted")
user_country["Sweden"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Stockholm', '$options':'i'}}).count()
print("people from Sweden counted")
user_country["United Arab Emirates"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Abu Dhabi', '$options':'i'}}).count()
print("people from United Arab Emirates counted")
user_country["Myanmar"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Rangoon', '$options':'i'}}).count()
print("people from Myanmar counted")
user_country["Georgia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Tbilisi', '$options':'i'}}).count()
print("people from Georgia counted")
user_country["Venezuela"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Caracas', '$options':'i'}}).count()
print("people from Venezuela counted")
user_country["Indonesia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Jakarta', '$options':'i'}}).count()
print("people from Indonesia counted")
user_country["Peru"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Lima', '$options':'i'}}).count()
print("people from Peru counted")
user_country["Africa"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Africa', '$options':'i'}}).count()
print("people from Africa counted")
user_country["Zimbabwe"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Harare', '$options':'i'}}).count()
print("people from Zimbabwe counted")
user_country["Mexico"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Chihuahua', '$options':'i'}},{'user.time_zone': {'$regex': 'Mazatlan', '$options':'i'}},{'user.time_zone': {'$regex': 'Monterrey', '$options':'i'}},{'user.time_zone': {'$regex': 'Tijuana', '$options':'i'}},{'user.time_zone': {'$regex': 'Chihuahua', '$options':'i'}},{'user.time_zone': {'$regex': 'Mexico City', '$options':'i'}},]}).count()
print("people from Mexico counted")
user_country["Romania"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Bucharest', '$options':'i'}}).count()
print("people from Romania counted")
user_country["Central Africa"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'West Central Africa', '$options':'i'}}).count()
print("people from Central Africa counted")
user_country["Serbia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Belgrade', '$options':'i'}}).count()
print("people from Serbia counted")
user_country["Japan"]  = db.TSAtweets.find({ "$or": [{'user.time_zone': {'$regex': 'Sapporo', '$options':'i'}},{'user.time_zone': {'$regex': 'Tokyo', '$options':'i'}},{'user.time_zone': {'$regex': 'Osaka', '$options':'i'}},]}).count()
print("people from Japan counted")
user_country["Germany"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Berlin', '$options':'i'}}).count()
print("people from Germany counted")
user_country["Croatia"]  = db.TSAtweets.find({'user.time_zone': {'$regex': 'Zagreb', '$options':'i'}}).count()
print("people from Croatia counted")

########################################################################################################################
# code snippet 3: plot percentage of first 10 countries according to users
# get the indexes of most user countries
most_user = sorted(user_country,key=user_country.get,reverse=True)[:10]
df = {
    'type': [],     # country names
    'count': [],    # user count
}
for n in most_user:
    print(n, user_country[n])
    df['type'].append(str(n))
    df['count'].append(user_country[n])
print(most_user)
print(df)
total_user = sum(user_country.values())
print("Total user:",total_user)
# Create a figure with a single subplot
f, ax = plt.subplots(1, figsize=(10,5))
# Set bar width at 1
bar_width = 1
# positions of the left bar-boundaries
bar_l = [i for i in range(len(df['count']))]
# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width/2) for i in bar_l]
# Create the percentage of the total score the percentage value for each participant was
percentage = [(i / total_user) * 100 for i in df['count']]
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
ax.set_xlabel("Country")
plt.title('Top 10 countries according to users')
# Let the borders of the graphic
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.ylim(0, 40)
# rotate axis labels
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
# shot plot
plt.show()

########################################################################################################################

print("total time :",round(clock()-start_time,2),"seconds")