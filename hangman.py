import strategies
import frequention
import random
import numpy
import matplotlib.pyplot as plt

NUMBER_OF_GAMES = 10

dict_file = open(frequention.NAME_OF_DICT, "r",encoding=frequention.DICT_ENCODING)
words = dict_file.readlines()

strats = []
strats.append(strategies.RandomStrategy())
strats.append(strategies.SimpleFreqStrategy())
strats.append(strategies.DictStrategy())
strats.append(strategies.ImprovedDictStrategy())
strats.append(strategies.FinaDictStrategy())

for i in range(NUMBER_OF_GAMES):
    print("----------------------------")
    print("Hra č. ", i)
    print("----------------------------")

    #Vylosovani nahodneho slova ze slovniku
    i = random.randint(0,len(words)-1)
    word = words[i].strip()

    for strat in strats:
        strategies.play_a_game(strat,word)
        print("----------------------------")

score = []
names = []
for strat in strats:
    score.append(strat.mistakes/NUMBER_OF_GAMES)
    names.append(strat.short_name)

#Vypise prumerny pocet chybne tipnutych pismen u jednotlivych strategii.
for i in range(len(strats)):
    print(names[i]+": "+str(score[i]))


plt.barh(numpy.arange(len(score)),score,align="center")
plt.yticks(numpy.arange(len(score)),names)
plt.xlabel('Number of mistakes')
plt.show()
