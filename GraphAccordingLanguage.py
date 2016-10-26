from time import clock
start_time = clock()
import matplotlib.pyplot as plt
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb
language_count = {
    # used to store language count like below, original dict is generated later
    # 'en': 100,
    # 'bn: '200,
}

cursor = db.TSAtweets.find({},{"lang":1, "_id":0})
language_list = []  # all languages from tweets
for element in cursor:
    try:
        language_list.append(element['lang'])
    except:
        pass
unique_language_list = set(language_list)   # get the unique language names
# print(unique_language_list)
for lang in unique_language_list:   # set language count to 0 in language count
    language_count[lang] = 0
for lang in language_list:  # count every language and store them to language cunt
    language_count[lang] +=1
########################################################################################################################
# code snippet 2: data and graph them according to first 10 language
language_count['und'] = 0
most_user = sorted(language_count, key=language_count.get, reverse=True)[:5]
df = {
    'type': [],     # country names
    'count': [],    # user count
}
for n in most_user:
    df['type'].append(str(n))
    df['count'].append(language_count[n])
# print(most_user)
# print(df)
total_user = sum(language_count.values())
# print("Total user:",total_user)
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
ax.set_xlabel("Language")
plt.title('Top 5 languages used')
# Let the borders of the graphic
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.ylim(0, 75)
# rotate axis labels
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
# shot plot
plt.show()

########################################################################################################################

########################################################################################################################
# Code    Language (region) used by twitter
# af      Afrikaans
# ar-ae   Arabic (U.A.E.)
# ar-bh   Arabic (Bahrain)
# ar-dz   Arabic (Algeria)
# ar-eg   Arabic (Egypt)
# ar-iq   Arabic (Iraq)
# ar-jo   Arabic (Jordan)
# ar-kw   Arabic (Kuwait)
# ar-lb   Arabic (Lebanon)
# ar-ly   Arabic (Libya)
# ar-ma   Arabic (Morocco)
# ar-om   Arabic (Oman)
# ar-qa   Arabic (Qatar)
# ar-sa   Arabic (Saudi Arabia)
# ar-sy   Arabic (Syria)
# ar-tn   Arabic (Tunisia)
# ar-ye   Arabic (Yemen)
# be      Belarusian
# bg      Bulgarian
# ca      Catalan
# cs      Czech
# cy      Welsh
# da      Danish
# de      German (Standard)
# de-at   German (Austria)
# de-ch   German (Switzerland)
# de-li   German (Liechtenstein)
# de-lu   German (Luxembourg)
# el      Greek
# en      English
# en-au   English (Australia)
# en-bz   English (Belize)
# en-ca   English (Canada)
# en-gb   English (United Kingdom)
# en-ie   English (Ireland)
# en-jm   English (Jamaica)
# en-nz   English (New Zealand)
# en-tt   English (Trinidad)
# en-us   English (United States)
# en-za   English (South Africa)
# es      Spanish (Spain)
# es-ar   Spanish (Argentina)
# es-bo   Spanish (Bolivia)
# es-cl   Spanish (Chile)
# es-co   Spanish (Colombia)
# es-cr   Spanish (Costa Rica)
# es-do   Spanish (Dominican Republic)
# es-ec   Spanish (Ecuador)
# es-gt   Spanish (Guatemala)
# es-hn   Spanish (Honduras)
# es-mx   Spanish (Mexico)
# es-ni   Spanish (Nicaragua)
# es-pa   Spanish (Panama)
# es-pe   Spanish (Peru)
# es-pr   Spanish (Puerto Rico)
# es-py   Spanish (Paraguay)
# es-sv   Spanish (El Salvador)
# es-uy   Spanish (Uruguay)
# es-ve   Spanish (Venezuela)
# et      Estonian
# eu      Basque
# fa      Farsi
# fi      Finnish
# fo      Faeroese
# fr      French (Standard)
# fr-be   French (Belgium)
# fr-ca   French (Canada)
# fr-ch   French (Switzerland)
# fr-lu   French (Luxembourg)
# ga      Irish
# gd      Gaelic (Scotland)
# he      Hebrew
# hi      Hindi
# hr      Croatian
# hu      Hungarian
# id      Indonesian
# is      Icelandic
# it      Italian (Standard)
# it-ch   Italian (Switzerland)
# ja      Japanese
# ji      Yiddish
# ko      Korean
# ko      Korean (Johab)
# ku      Kurdish
# lt      Lithuanian
# lv      Latvian
# mk      Macedonian (FYROM)
# ml      Malayalam
# ms      Malaysian
# mt      Maltese
# nl      Dutch (Standard)
# nl-be   Dutch (Belgium)
# nb      Norwegian (Bokmål)
# nn      Norwegian (Nynorsk)
# no      Norwegian
# pa      Punjabi
# pl      Polish
# pt      Portuguese (Portugal)
# pt-br   Portuguese (Brazil)
# rm      Rhaeto-Romanic
# ro      Romanian
# ro-md   Romanian (Republic of Moldova)
# ru      Russian
# ru-md   Russian (Republic of Moldova)
# sb      Sorbian
# sk      Slovak
# sl      Slovenian
# sq      Albanian
# sr      Serbian
# sv      Swedish
# sv-fi   Swedish (Finland)
# th      Thai
# tn      Tswana
# tr      Turkish
# ts      Tsonga
# uk      Ukrainian
# ur      Urdu
# ve      Venda
# vi      Vietnamese
# xh      Xhosa
# zh-cn   Chinese (PRC)
# zh-hk   Chinese (Hong Kong)
# zh-sg   Chinese (Singapore)
# zh-tw   Chinese (Taiwan)
# zu      Zulu
########################################################################################################################

print("total time :",round(clock()-start_time,2),"seconds")