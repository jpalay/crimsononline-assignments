import string
import re

#!/usr/bin/python
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
    sorted_list = sorted(words, key=lambda word: -file_contents.count(word))
    uniques = []
    for s in sorted_list: 
        if s not in uniques: uniques.append(s)
    return uniques

def common_words_min(filename, min_chars):
    file = open(filename, "r")
    file_contents = file.read()
    file.close()
    # Need to split on newline, punctuation, etc.  
    # Got it from http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators
    words = re.findall(r"[\w']+", file_contents)
    sorted_list = sorted(map(lambda w: string.lower(w), words), key=lambda word: -file_contents.count(word))
    uniques = []
    for s in sorted_list: 
        if s not in uniques and len(s) >= min_chars: uniques.append(s)
    return uniques

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    file = open(filename, "r")
    file_contents = file.read()
    file.close()
    # Need to split on newline, punctuation, etc.  
    # Got it from http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators
    words = re.findall(r"[\w']+", file_contents)
    sorted_list = sorted(map(lambda w: (string.lower(w), file_contents.count(w)), words), key=lambda wordt: -wordt[1])
    uniques = []
    for s in sorted_list: 
        if s not in uniques and len(s[0]) >= min_chars: uniques.append(s)
    return uniques

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    file = None
    try:
        file = open(filename, 'r')
        file_contents = file.read()
        file.close()
    except IOError:
        print "I can\'t find\"{}\"".format(filename)
        return

    # Need to split on newline, punctuation, etc.  
    # Got it from http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators
    words = re.findall(r"[\w']+", file_contents)
    sorted_list = sorted(map(lambda w: (string.lower(w), file_contents.count(w)), words), key=lambda wordt: -wordt[1])
    uniques = []
    for s in sorted_list: 
        if s not in uniques and len(s[0]) >= min_chars: uniques.append(s)
    return uniques
