
#___________________________________________________________________________________
class Mage:
    def __init__(self,nom):

        self.__nom=nom
        self.__pv=30
        self.__mana=3
        self.__maxMana=10
        self.__main = []
        self.__defausse = []
        self.__zone = []

    def getNom(self):
        return self.__nom
    def getPV(self):
        return self.__pv
    def getMana(self):
        return self.__mana
    
    def setPDV(self,value):
        self.__pv+=value
        if self.__pv<0 :
            return True
    def setMana(self,value):
        self.__mana+=value
        if self.__mana<0 :
            self.__mana = 0
        if self.__mana>self.__maxMana:
            self.__mana = self.__maxMana
    def afficheMain(self):
        for i in range(len(self.__main)):
            print(self.__main[i].getNom())
    def tirerCarte(self):
        self.__main.extend()
    def useCarte(self,choix):
        if self.__main[choix].getSort() == True:
            self.__main[choix].fonction()
        else:
            self.setMana(-(self.__main[choix].getCout()))
            self.__zone.extend(self.__main[choix])
            del self.__main[choix]
    def detruireCarte(self,zone):
        print(self.__zone[zone].getNom()," est détruit et part dans votre défausse")
        self.__defausse.extend(self.__zone[zone])
        del self.__zone[zone]




#___________________________________________________________________________________