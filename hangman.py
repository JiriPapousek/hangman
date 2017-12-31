import strategies
import frequention
import random
import numpy
import pylab
import matplotlib.pyplot as plt
import sys

def test_strategies(number_of_games, name_of_dict, dict_encoding, strat_names):
    dict_file = open(name_of_dict, "r",encoding=dict_encoding)
    words = dict_file.readlines()

    strats = []
    for strat_name in strat_names:
        strats.append(strat_name(name_of_dict, dict_encoding))

    #Plays specific number of games on all strategies.
    for i in range(number_of_games):
        print("----------------------------")
        print("Game number ", i)
        print("----------------------------")

        #Picks a random word from the dictionary.
        i = random.randint(0,len(words)-1)
        word = words[i].strip()

        for strat in strats:
            strategies.play_a_game(strat,word)
            print("----------------------------")

    score = []
    names = []
    for strat in strats:
        score.append(strat.mistakes/number_of_games)
        names.append(strat.short_name)

    #Prints out average number of wrong played letters by different trategies.
    for i in range(len(strats)):
        print(names[i]+": "+str(score[i]))

    #Draws a graph of results.
    plt.barh(numpy.arange(len(score)),score,align="center")
    plt.yticks(numpy.arange(len(score)),names)
    plt.xlabel('Number of mistakes')
    plt.tight_layout()
    pylab.savefig("results.png")
    plt.show()

strat_list = [strategies.RandomStrategy,
              strategies.SimpleFreqStrategy,
              strategies.ImprovedFreqStrategy,
              strategies.DictStrategy,
              strategies.SplitStrategy]

test_strategies(int(sys.argv[1]), sys.argv[2], sys.argv[3], strat_list)
