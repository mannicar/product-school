class Monster(object):

    is_scary = True

    def __init__(self, ssn = None, name = None):
        self.crimes = []
        self._isMisunderstood = True
        self.name = name
        self._ssn = ssn # Because even Monsters pay taxes
        self.victims = set([])

    def roar(self):
        print 'ROAR!  MY NAME IS ' + self.name

    def isMisunderstood(self):
        return self._isMisunderstood

    def murder(self, victimName):
        self._isMisunderstood = False
        self.victims.add(victimName)
        self.crimes.append('Murder of ' + victimName)
        cryForHelp = None
        if self.name:
            print 'HELP! ' + self.name + ' murdered ' + victimName + '!'

    # properties should be used to access variables
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    # Implement victims setter and getter

    # Implement SSN setter and getter

    # =========== ADVANCED =========== 
    # 1. Ensure that all items in crimes are strings
    # 2. Add a date to all crimes.  HINT: Use a dictionary or a tuple.  You may have to modify the code you implemented in step one.

class Vampire(Monster):

    def __init__(self, ssn, name, master):
        # A subclass should initialize its parent class
        Monster.__init__(self, ssn, name)
        self.master = master

    # This method overrides the murder method in the Monster class
    def murder(self, victimName):
        super(Vampire, self).murder(victimName)
        return Vampire(None, victimName, self.name)

    def drink_blood(self, victimName):
        return 'Not Implemented'
        ## Implement me

    def getTanned(self):
        return 'Not Implemented'

    # How do setters and getters work in here?
    # If you did the VERY ADVANCED exercise, how will that change affect ssn and name setters and getters?   

# =========== VERY ADVANCED =========== 
class Person(object):

    ## Implement me and make Vampire inherit from Person as well.  Remember people also have SSN!