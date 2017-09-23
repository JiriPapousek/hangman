# -*- coding: utf-8 -*-
from __future__ import division
import frequention
import random


basic_freq = frequention.find_basic_freq(frequention.NAME_OF_DICT)
dict_file = open(frequention.NAME_OF_DICT, "r")
words = dict_file.readlines()

#Strategie nahodneho tipovani znaku
class random_strategy:
    mistakes = 0

    def play_round(self,state_of_play,guesses):
        not_played_yet = False
        while not not_played_yet:
            i = random.randint(0,len(basic_freq)-1)
            if basic_freq[i] not in guesses:
                not_played_yet = True
        return basic_freq[i]

    def made_mistake(self):
        self.mistakes += 1

#Strategie zalozená na frekvenci pismen v ceskem jazyce
class simple_freq_strategy:
    mistakes = 0

    def play_round(self,state_of_play,guesses):
        return basic_freq[len(guesses)]

    def made_mistake(self):
        self.mistakes += 1

#Fce odehraje jednu hru obesence na zaklade vstupniho slova a strategie.
def play_a_game(strategy, word):
    guesses = []
    state_of_play = ""
    for i in range(len(word)):
        state_of_play = state_of_play+" "
    print state_of_play
    while state_of_play != word:
        letter = strategy.play_round(state_of_play,guesses)
        guesses.append(letter)
        print letter
        guess_success = False
        for i in range(len(word)):
            if letter == word[i]:
                state_of_play = state_of_play[0:i] + letter + state_of_play[i+1:]
                print "Stav hry:" + state_of_play
                guess_success = True
        if not guess_success:
            strategy.made_mistake()
    return strategy.mistakes

rand_strat = random_strategy()
simple_strat = simple_freq_strategy()

for i in range(300):
    print "----------------------------"
    print u"Hra č.", i
    print "----------------------------"

    #Vylosovani nahodneho slova ze slovniku
    i = random.randint(0,len(words)-1)
    word = words[i].decode("cp1250").strip()

    play_a_game(rand_strat,word)
    "------------------------"
    play_a_game(simple_strat,word)

#Vypise prumerny pocet chybne tipnutych pismen u jednotlivych strategii.
print u"Strategie náhodně losovaných písmen:", rand_strat.mistakes/300
print u"Strategie podle frekvence písmen v jazyce:", simple_strat.mistakes/300
