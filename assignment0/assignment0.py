#!/usr/bin/python
import datetime
import json
import random
import sys
import urllib

print("\nI love the Crimson tech department!\n")

################################################################
# FIZZ BUZZ                                                    #
################################################################

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0:
            sys.stdout.write("Fizz")
        if i % 5 == 0:
            sys.stdout.write("Buzz")
        elif i % 3 != 0:
           sys.stdout.write(str(i))
        sys.stdout.write("\n")

print("FIZZ_BUZZ TEST:")
fizz_buzz()
print ""

################################################################
# SWAPCHARS                                                    #
################################################################

def swapchars(s):
    letters = dict()
    for char in s:
        # make char lowercase because we want "T" and "t" to be treated the same
        char = char.lower()
        # check that char is a letter
        if ord(char) - ord("a") in range(26):
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

    most_frequent  = None
    least_frequent = None
    chars_sorted = sorted(letters.keys(), key=lambda c: letters[c])
    if not chars_sorted:
        return s
    least_frequent = chars_sorted[0]
    most_frequent = chars_sorted[len(chars_sorted) - 1]


    output = ""
    for char in s:
        # break into five cases to conserve capitalization
        if char == most_frequent:
            output += least_frequent
        elif char.lower() == most_frequent:
            output += least_frequent.upper()
        elif char == least_frequent:
            output += most_frequent
        elif char.lower() == least_frequent:
            output += most_frequent.upper()
        else:
            output += char
    
    return output

print "SWAPCHARS TESTS:"
print 'swapchars("There were a lot of escopeoples in the elevator on Tuesday.") = ' + swapchars("There were a lot of escopeoples in the elevator on Tuesday.")
print 'swapchars("The quick brown fox jumped over the lazy dog.")               = ' + swapchars("The quick brown fox jumped over the lazy dog.")
print 'swapchars("aaaaaaaaaaaaaaaaaaaaaaaaaa")                                  = ' + swapchars("aaaaaaaaaaaaaaaaaaaaaaaaaa")
print 'swapchars("")                                                            = ' + swapchars("")
print 'swapchars("a")                                                           = ' + swapchars("a")
print 'swapchars("ab")                                                          = ' + swapchars("ab")
print 'swapchars("aab")                                                         = ' + swapchars("aab")
print 'swapchars("AAAaaBbccC")                                                  = ' + swapchars("AAAaaBbccC")
print 'swapchars("435/3.")                                                      = ' + swapchars("435/3.")
print 'swapchars("43AAAaaBbccC5/3.")                                            = ' + swapchars("43AAAaaBbccC5/3.")
print ""

################################################################
# SORTCAT                                                      #
################################################################

def sortcat(n, *strs):
    strs = map(lambda x: str(x), strs)[:n]
    strs = sorted(strs, key=lambda s: -len(s)) 
    # added bars to make output more readable
    return " | ".join(strs)

print "SORTCAT TESTS:"
print sortcat(1, 'abc', 'bc')
print sortcat(9, 'abc', 'ab', 899)
print sortcat(3, 'cd', 'a', 'cat', 21342134, True)
print sortcat(3)
print ""

################################################################
# LOOK AWAY                                                    #
################################################################

def look_away(games):
    num_directions = 5
    forward = 0
    enemies = 3
    rounds = 5
    wins = 0

    for i in range(games):
        # reset enemies left
        enemies_left = enemies
        for j in range(rounds):
            # for each enemy
            for k in range(enemies_left):
                direction = random.randrange(num_directions)
                if direction == forward:
                    enemies_left -= 1 # doesn't affect how many times the loop executes until the end of the round
            if enemies_left <= 0:
                wins += 1
                # game over
                break

    return float(wins) / float(games)

print "LOOK AWAY TEST:"
print "Luigi wins " + str(100 * look_away(100000)) + "% of the time."
print "Sounds about right."
print ""

################################################################
# SHUTTLEBOY                                                   #
################################################################

def quad_to_mass_ave():
    start = "Quad"
    end = "Mass Ave Garden St"
    url = "http://shuttleboy.cs50.net/api/1.2/trips?a=" + start + "&b=" + end + "&output=json"
    raw_json = urllib.urlopen(url).read()
    stops = json.loads(raw_json)

    for stop in stops:
        for key in stop:
            stop[key] = datetime.datetime.strptime(stop[key], "%Y-%m-%dT%H:%M:%S")
    
    stops = sorted(stops, key = lambda s: stop["departs"])[:3]
    for stop in stops:
        print "Shuttle leaving at " + str(stop["departs"]) + " (Time from now: " + str((stop["departs"] - datetime.datetime.now()))

quad_to_mass_ave()






