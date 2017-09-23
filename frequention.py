NAME_OF_DICT = "Czech.3-2-5.dic"

#Funkce vrati slovnik listu pismen ceske abecedy serazenych podle cetnosti.
def find_freq_of_two_letters(dict):
    dict_file = open(dict,"r")
    freq = {}
    for line in dict_file:
        word = line.decode("cp1250").strip()
        for i in range(len(word)-1):
            if word[i] in freq:
                if word[i+1] in freq[word[i]]:
                    freq[word[i]][word[i+1]] += 1
                else:
                    freq[word[i]][word[i+1]] = 1
            else:
                freq[word[i]] = {}
                freq[word[i]][word[i + 1]] = 1
    for letter in freq:
        freq[letter] = sorted(freq[letter], key=freq[letter].get)[::-1]
    return freq

#Funkce vrati list pismen ceske abecedy serazenych podle cetnosti.
def find_basic_freq(dict):
    dict_file = open(dict, "r")
    freq = {}
    for line in dict_file:
        word = line.decode("cp1250").strip()
        for i in range(len(word)):
            if word[i] in freq:
                freq[word[i]] += 1
            else:
                freq[word[i]] = 1
    sorted_freq = sorted(freq, key=freq.get)[::-1]
    return sorted_freq

#Seznam pismen ceske abecedy serazenych podle cetnosti.
#basic_freq = find_basic_freq(NAME_OF_DICT)
#for i in basic_freq:
#    print i

#two_letters_freq = find_freq_of_two_letters(NAME_OF_DICT)
#for i in two_letters_freq:
#    print i + ": "
#    print two_letters_freq[i]