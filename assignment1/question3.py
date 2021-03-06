"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

class Person:
    def __init__(self, fname, lname, gender):
        if not (gender.upper() == "M" or gender.upper() == "F"):
            raise Exception("Invalid Gender Exception")
        if (len(fname) == 0 or ord(fname[0]) - ord("a") in range(26) or
            len(lname) == 0 or ord(lname[0]) - ord("z") in range(26)):
            raise Exception("Invalid Name Exception")
        self.fname = fname
        self.lname = lname
        self.gender = gender.upper()

class Building(object):
    all_buildings = dict()

    def __init__(self, loc):
        # List of tuples (room_no, pepole_lst).  Used a list because 
        # when I iterate, I need to make sure the order stays the same
        self.rooms = []
        # self.current is a touple in the form (room_no, index)
        self.current = (0, 0)
        self.loc = loc
        if loc in Building.all_buildings.keys(): raise Exception("TwoBuildingsInOneLocation")
        else: Building.all_buildings[loc] = self

    def __iter__(self):
        return self

    def __setitem__(self, room, person):
        self.enter(person, room)

    @classmethod
    def locate(cls, location):
        if location in Building.all_buildings.keys(): 
            return Building.all_buildings[location]
        else:
            return None

    def next(self):
        (i, j) = self.current
        try:
            if j >= len(self.rooms[i][1]):
                self.current = (i + 1, 0)
                (i, j) = self.current
            n = self.rooms[i][1][j]
            self.current = (i, j + 1)
            return n
        except IndexError:
            self.current = (0, 0)
            raise StopIteration

    def enter(self, person, room_no):
        if room_no not in map(lambda x: x[0], self.rooms): 
            self.rooms.append((room_no, [person]))
        to_remove = None
        for k in range(len(self.rooms)):
            if (room_no == self.rooms[k][0] and 
                person not in self.rooms[k][1]): self.rooms[k][1].append(person)
            elif room_no != self.rooms[k][0] and person in self.rooms[k][1]:
                # Delete the room if nobody's in it
                if len(self.rooms[k][1]) == 1: to_remove = k
                else: self.rooms[k][1].remove(person)
        if to_remove is not None: self.rooms.pop(to_remove)

    def where_is(self, person):
        for room_no, people in self.rooms.iteritems():
            if person in people: return room_no
        return None

class OfficeBuilding(Building):
    def __init__(self, emp_lst, loc):
        self.emp_lst = emp_lst
        super(OfficeBuilding, self).__init__(loc)


    def enter(self, person, room_no):
        if person in self.emp_lst:
            super(OfficeBuilding, self).enter(person, room_no)
        else:
            raise Exception("INTRUDER_ALERT")

class Home():
    def __init__(self, loc):
        current = 0
        self.ppl = []
        if loc in Building.all_buildings.keys(): raise Exception("TwoBuildingsInOneLocation")
        else: Building.all_buildings[loc] = self
        
    def enter(self, person):
        if person not in self.ppl: self.ppl.append(person)

    def at_home(self, person):
        return person in self.ppl

    def next(self):
        if self.current == len(self.ppl):
            self.current = 0
            raise StopIteration
        current += 1
        return self.ppl[current - 1] 
