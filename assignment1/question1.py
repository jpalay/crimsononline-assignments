import collections
import re

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    file = open(filename, "r")
    file_contents = file.read().lower()
    file.close()
    # Need to split on newline, punctuation, etc.  
    # Got it from http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators
    words = re.findall(r"[\w']+", file_contents)
    word_count = collections.Counter(words).items()
    return map(lambda w: w[0], sorted(word_count, key=lambda w: -w[1]))

def common_words_min(filename, min_chars):
    file = open(filename, "r")
    file_contents = file.read().lower()
    file.close()
    # Need to split on newline, punctuation, etc.  
    # Got it from http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators
    words = re.findall(r"[\w']+", file_contents)
    sorted_list = map(lambda w: w[0], sorted(collections.Counter(words).items(), key=lambda w: -w[1]))
    results = []
    for w in sorted_list:
        if len(w) >= min_chars: results.append(w)
    return results

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    file = open(filename, "r")
    file_contents = file.read().lower()
    file.close()
    # Need to split on newline, punctuation, etc.  
    # Got it from http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators
    words = re.findall(r"[\w']+", file_contents)
    sorted_list = sorted(collections.Counter(words).items(), key=lambda w: -w[1])
    results = []
    for w in sorted_list:
        if len(w[0]) >= min_chars: results.append(w)
    return results

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    file = None
    try:
        file = open(filename, 'r')
        file_contents = file.read().lower()
        file.close()
    except IOError:
        print "I can\'t find \"{}\"".format(filename)
        return
    # Need to split on newline, punctuation, etc.  
    # Got it from http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators
    words = re.findall(r"[\w']+", file_contents)
    sorted_list = sorted(collections.Counter(words).items(), key=lambda w: -w[1])
    results = []
    for w in sorted_list:
        if len(w[0]) >= min_chars: results.append(w)
    return results
