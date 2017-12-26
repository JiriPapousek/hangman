import frequention
import random
import math

class Strategy:
    """
    Template for general strategy.
    """
    def __init__(self):
        self.mistakes = 0

    def made_mistake(self):
        self.mistakes += 1

class RandomStrategy(Strategy):
    """
    Strategy that plays a random character (from characters used
    in the dictionary).
    """
    def __init__(self, dict_name, dict_encoding):
        self.mistakes = 0
        self.basic_freq = frequention.find_basic_freq(dict_name, dict_encoding)
        self.short_name = "random"

    def play_round(self,state_of_play,guesses):
        not_played_yet = False
        while not not_played_yet:
            i = random.randint(0,len(self.basic_freq)-1)
            if self.basic_freq[i] not in guesses:
                not_played_yet = True
                return self.basic_freq[i]

class SimpleFreqStrategy(Strategy):
    """
    Strategy based on letters frequency in the dictionary.
    """
    def __init__(self, dict_name, dict_encoding):
        self.mistakes = 0
        self.basic_freq = frequention.find_basic_freq(dict_name, dict_encoding)
        self.short_name = "freq_letters"

    def play_round(self, state_of_play, guesses):
        return self.basic_freq[len(guesses)]

class ImprovedFreqStrategy(Strategy):
    """
    This strategy is similar to SimpleFreqStrategy, but it uses frequency
    of two neighbour letters whenever it is possible instead of general
    letter frequency.
    """
    def __init__(self, dict_name, dict_encoding):
        self.mistakes = 0
        self.basic_freq = frequention.find_basic_freq(dict_name, dict_encoding)
        self.improved_freq = frequention.find_freq_of_two_letters(dict_name, dict_encoding)
        self.short_name = "improved_freq_letters"

    def play_round(self, state_of_play, guesses):
        for i in range(len(state_of_play)-1):
            if state_of_play[i]!=" " and state_of_play[i+1]==" ":
                for x in self.improved_freq[state_of_play[i]]:
                    if x not in guesses:
                        return x
        for i in self.basic_freq:
            if i not in guesses:
                return i

def triable(state_of_play, word, guesses):
    if len(state_of_play) != len(word):
        return False
    for i in range(len(word)):
        if state_of_play[i]!=" " and state_of_play[i]!=word[i]:
            return False
        if state_of_play[i]==" " and word[i] in guesses:
            return False
    return True

class DictStrategy(Strategy):
    """
    Strategy gradually comparing the state of game with every word in the
    dictionary, until a matching word is not found. Than it plays last
    letter in this word, which hasn't been played yet.
    """
    def __init__(self, dict_name, dict_encoding):
        self.mistakes = 0
        dict_file = open(dict_name, "r", encoding=dict_encoding)
        self.words = dict_file.readlines()
        dict_file.close()
        self.short_name = "dict_strat"

    def play_round(self,state_of_play,guesses):
        for word in self.words:
            word = word.strip()
            if triable(state_of_play, word, guesses):
                for i in range(len(state_of_play)):
                    if state_of_play[i]==" ":
                        return word[i]

class SplitStrategy(Strategy):
    """
    The strategy using dictionary - except it does not return the best
    possible candidate at the moment, but the candidate that has half to
    half ratio of success.
    """
    def __init__(self, dict_name, dict_encoding):
        self.mistakes = 0
        dict_file = open(dict_name, "r", encoding=dict_encoding)
        self.words = dict_file.readlines()
        dict_file.close()
        self.short_name = "split_strat"

    def play_round(self, state_of_play, guesses):
        freq = {}
        total = 0
        for word in self.words:
            word = word.strip()
            if triable(state_of_play, word, guesses):
                total += 1
                letters_in_word = []
                for i in word:
                    if i not in letters_in_word and i not in guesses:
                        letters_in_word.append(i)
                for i in letters_in_word:
                    candidate = i
                    if i in freq:
                        freq[i] += 1
                    else:
                        freq[i] = 1
        for letter in freq:
            if math.fabs(freq[letter]-total/2)<math.fabs(freq[candidate]-total/2):
                candidate = letter
        return candidate

def play_a_game(strategy, word):
    """
    Function plays a game of hangman using a word and strategy as an input.
    """
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
                print("State of game: " + state_of_play)
                guess_success = True
        if not guess_success:
            strategy.made_mistake()
    return strategy.mistakes
