import random
from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple,
    common_words_safe)
from question2 import parse_links_regex, parse_links_xpath
from question3 import *
from question4 import GITHUB_URL
# fill in the rest!

print "==testing question 1=="
print "common_words... ",
pprint(common_words("words.txt"))

print "common_words_min 2... ",
pprint(common_words_min("words.txt", 2))

print "common_words_min 5... ",
pprint(common_words_min("words.txt", 5))

print "common_words_min 9... ",
pprint(common_words_min("words.txt", 9))

print "common_words_tuple w/ min 5... ",
pprint(common_words_tuple("words.txt", 5))

print "common_words_safe... ",
pprint(common_words_safe("words_fail.txt", 5))
print


print "==testing question 2=="
print "regex... ",
pprint(parse_links_regex("crimson.html"))
print "\nxpath... "
pprint(parse_links_xpath("crimson.html"))
print


print "==testing question 3=="
print "Creating people..."
people_data = [("Josh", "Palay", "M"), ("invalid", "name", "m"), ("Invalid", "Gender", "L"), 
               ("Joe", "Smith", "M"),("Jane", "Smith", "F"),("Human", "Female", "F")]
people = []
for d in people_data:
	try: people.append(Person(d[0], d[1], d[2]))
	except: print "Failed to create person using data {}".format(d)
pprint(map(lambda p: p.__dict__, people))

print "Creating empty building..."
b = Building((1,2))
pprint(b.__dict__)

print "Filling empty building..."
for person in people:
	b.enter(person, random.randrange(3))
pprint(b.__dict__)
for person in b:
	pprint(person.__dict__)

print "Rearranging the building... "
for person in people:
	b.enter(person, random.randrange(3))
pprint(b.__dict__)
for person in b:
	pprint(person.__dict__)

print "Creating empty office building..."
ob = OfficeBuilding(people[:2], (2,1))
pprint(ob.__dict__)
for person in ob.emp_lst:
	pprint(person.__dict__)

print "Filling office building..."
for person in people:
	try: ob.enter(person, random.randrange(3))
	except: print "{} was denied entry".format(person.__dict__)
pprint(ob.__dict__)
for person in ob:
	pprint(person.__dict__)

family = people[:2]

print "Building a house..."
h = Home((3,1))
pprint(h.__dict__)

print "Family coming in..."
for person in family:
	h.enter(person)
pprint(h.__dict__)
for person in family:
	pprint(person.__dict__)

print "Is Josh Palay at home? {}".format("Yes!" if h.at_home(people[0]) else "No :(")
print "Is Human Female at home? {}".format("Yes!" if h.at_home(people[3]) else "No :(")

print "What's at (3, 1)?  ",
pprint(Building.locate((3, 1)))
print "What's at (9, 9)?  ",
pprint(Building.locate((9, 9)))

print "Let's stick Joe Biden in room zero of the building!!"
jb = Person("Joe", "Biden", "M")
b[0] = jb
pprint(b.__dict__)
for person in b:
	pprint(person.__dict__)

print "==testing question 4=="
print "github url: {}".format(GITHUB_URL)
print


print "==testing question 5=="
# ???
print