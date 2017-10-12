import frequention
import random

basic_freq = frequention.find_basic_freq(frequention.NAME_OF_DICT,frequention.DICT_ENCODING)
dict_file = open(frequention.NAME_OF_DICT, "r",encoding=frequention.DICT_ENCODING)
words = dict_file.readlines()

#Strategie nahodneho tipovani znaku
class RandomStrategy:
    def __init__(self):
        self.mistakes = 0
        self.short_name = "random"

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
class SimpleFreqStrategy:
    def __init__(self):
        self.mistakes = 0
        self.short_name = "freq_letters"

    def play_round(self,state_of_play,guesses):
        return basic_freq[len(guesses)]

    def made_mistake(self):
        self.mistakes += 1

#Strategie postupně porovnávající stav hry s každým slovem ve slovníku,
#dokud nenajde odpovídající slovo. Následně zahraje poslední ještě
#nezahrané možné písmeno ve slově.
class DictStrategy:

    def __init__(self):
        self.mistakes = 0
        self.short_name = "dict_strat"

    def play_round(self,state_of_play,guesses):
        for word in words:
            word = word.strip()
            if len(word)==len(state_of_play):
                triable = True
                letter = " "
                for i in range(len(word)):
                    if (word[i]!=state_of_play[i]) and (state_of_play[i]!=" "):
                        triable = False
                        break
                    elif (state_of_play[i]==" ") and (word[i] not in guesses):
                        letter = word[i]
                if (triable) and (letter!=" "):
                    return letter

    def made_mistake(self):
        self.mistakes += 1

class ImprovedDictStrategy:

    def __init__(self):
        self.mistakes = 0
        self.short_name = "improved_dict"

    def play_round(self,state_of_play,guesses):
        right_letters_freq = {}
        for word in words:
            word = word.strip()
            if len(word)==len(state_of_play):
                triable = True
                letter = " "
                for i in range(len(word)):
                    if (word[i]!=state_of_play[i]) and (state_of_play[i]!=" "):
                        triable = False
                        break
                    elif (state_of_play[i]==" ") and (word[i] not in guesses):
                        if word[i] in right_letters_freq:
                            right_letters_freq[word[i]] += 1
                        else:
                            right_letters_freq[word[i]] = 1
        return max(right_letters_freq, key=right_letters_freq.get)


    def made_mistake(self):
        self.mistakes += 1

class FinaDictStrategy:
    def __init__(self):
        self.mistakes = 0
        self.short_name = "final_dict"

    def play_round(self,state_of_play,guesses):
        right_letters_freq = {}
        for word in words:
            word = word.strip()
            if len(word)==len(state_of_play):
                triable = True
                counted_letters = []
                for i in range(len(word)):
                    if (word[i]!=state_of_play[i]) and (state_of_play[i]!=" "):
                        triable = False
                        break
                    elif (state_of_play[i]==" ") and (word[i] not in guesses):
                        if word[i] in right_letters_freq:
                            if word[i] not in counted_letters:
                                right_letters_freq[word[i]] += 1
                                counted_letters.append(word[i])
                        else:
                            right_letters_freq[word[i]] = 1
        return max(right_letters_freq, key=right_letters_freq.get)


    def made_mistake(self):
        self.mistakes += 1

#Fce odehraje jednu hru obesence na zaklade vstupniho slova a strategie.
def play_a_game(strategy, word):
    guesses = []
    state_of_play = ""
    for i in range(len(word)):
        state_of_play = state_of_play + " "
    print(state_of_play)
    while state_of_play != word:
        letter = strategy.play_round(state_of_play,guesses)
        guesses.append(letter)
        print(letter)
        guess_success = False
        for i in range(len(word)):
            if letter == word[i]:
                state_of_play = state_of_play[0:i] + letter + state_of_play[i+1:]
                print("Stav hry: " + state_of_play)
                guess_success = True
        if not guess_success:
            strategy.made_mistake()
    return strategy.mistakes
