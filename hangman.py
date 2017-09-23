import strategies
import frequention
import random

dict_file = open(frequention.NAME_OF_DICT, "r",encoding=frequention.DICT_ENCODING)
words = dict_file.readlines()

rand_strat = strategies.random_strategy()
simple_strat = strategies.simple_freq_strategy()

for i in range(300):
    print("----------------------------")
    print("Hra č. ", i)
    print("----------------------------")

    #Vylosovani nahodneho slova ze slovniku
    i = random.randint(0,len(words)-1)
    word = words[i].strip()

    strategies.play_a_game(rand_strat,word)
    "------------------------"
    strategies.play_a_game(simple_strat,word)

#Vypise prumerny pocet chybne tipnutych pismen u jednotlivych strategii.
print("Strategie náhodně losovaných písmen: ", rand_strat.mistakes/300)
print("Strategie podle frekvence písmen v jazyce: ", simple_strat.mistakes/300)