def find_basic_freq(dict,encoding):
    """
    Function returns list of characters sorted by their frequention
    in dictionary file.
    """
    dict_file = open(dict, "r",encoding=encoding)
    freq = {}
    for line in dict_file:
        word = line.strip()
        for i in range(len(word)):
            if word[i] in freq:
                freq[word[i]] += 1
            else:
                freq[word[i]] = 1
    sorted_freq = sorted(freq, key=freq.get)[::-1]
    return sorted_freq

def find_freq_of_two_letters(dict,encoding):
    """
    Function returns dictionary of lists of characters sorted by their
    frequention in dictionary file.
    """
    dict_file = open(dict,"r",encoding=encoding)
    freq = {}
    for line in dict_file:
        word = line.strip()
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