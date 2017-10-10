class Monster(object):

    is_scary = True

    def __init__(self, ssn = None, name = None):
        self.crimes = []
        self._isMisunderstood = True
        self.name = name
        self._ssn = ssn
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

class Vampire(Monster):

    def __init__(self, ssn, name, master):
        Monster.__init__(self, ssn, name)
        self.master = master

    def murder(self, victimName):
        super(Vampire, self).murder(victimName)
        return Vampire(None, victimName, self.name)
