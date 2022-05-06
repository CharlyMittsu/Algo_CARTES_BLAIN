import random

#___________________________________________________________________________________
#___________________________________________________________________________________
#___________________________________________________________________________________
class Mage:#la classe du joueur
    def __init__(self,player,nom):

        self.__player=player
        self.__nom=nom
        self.__pv=30
        self.__mana=3
        self.__maxMana=10
        self.__main = []
        self.__defausse = []
        self.__zone = []

    def getPlayer(self):
        return self.__player  
    def getNom(self):
        return self.__nom
    def getPV(self):
        return self.__pv
    def getMana(self):
        return self.__mana
    
    def setPV(self,value):
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
            self.setMana(-(self.__main[choix].getCout()))
        else:
            self.setMana(-(self.__main[choix].getCout()))
            self.__zone.extend(self.__main[choix])
            del self.__main[choix]
    def detruireCarte(self,choix):
        print(self.__zone[choix].getNom()," est détruit et part dans votre défausse")
        self.__defausse.extend(self.__zone[choix])
        del self.__zone[choix]
    def jouerCarte(self,choix):
        if self.__zone[choix].getCout()>self.__mana:#si le cout est trop élévée
            return True
        else:
            self.__zone[choix].fonction(self)
            self.setMana(-(self.__zone[choix].getCout()))


#___________________________________________________________________________________
#___________________________________________________________________________________
#___________________________________________________________________________________
#__Mommy Class
class Carte:
    def __init__(self,nom,cout,description,sort):

        self.__nom=nom
        self.__cout=cout
        self.__description=description
        self.__sort=sort
    
    def getNom(self):
        return self.__nom
    def getCout(self):
        return self.__cout
    def getDescription(self):
        return self.__description
    def isSort(self):
        return self.__sort

#___________________________________________________________________________________
#__Daughter Class

class Cristal(Carte):
    def __init__(self, nom,cout,description):
        super().__init__(self, nom,cout,description,False)#cristal n'est pas un sort
        self.__valeur = 1
    
    def fonction(self,player):
        print(self.__description)
        player.setMana(self.__valeur)


#___________________________________________________________________________________
#__Daughter Class

class Creature(Carte):
    def __init__(self, nom,cout,description,atk,pv):
        super().__init__(self, nom,cout,description,False)#creature n'est pas un sort
        self.__atk = atk
        self.__pv = pv
    
    def getPV(self):
        return self.__pv

    def setPV(self,value):
        self.__pv+=value
        if self.__pv<0 :
            return True
    
    def fonction(self,player):
        cible = int(input("choisissez une cible"))
        print(self.__description)
        player.setMana(self.__valeur)
