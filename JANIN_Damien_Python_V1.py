#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SaboteurFerroviaire:
    __pseudoSaboteur = None
 
    def __init__ (self,pseudoSaboteur):
        self.__pseudoSaboteur = pseudoSaboteur
 
    def getPseudo(self):
        return self.__pseudoSaboteur
 
class FlotteAlliee:
    __pseudoAllies = None
 
    def __init__ (self,pseudoAllies):
        self.__pseudoAllies = pseudoAllies
 
    def getPseudo(self):
        return self.__pseudoAllies
 
   ####COMPLETER ????######
 
class Resistant:
    __pseudoResist = None
    __lesMessages = None
    __flotteAlliee = None
 
    def __init__ (self,pseudoResist,lesMessages,flotteAlliee):
        self.__pseudoResist = pseudoResist
        self.__lesMessages = lesMessages
        self.__flotteAlliee = flotteAlliee
 
    def getMessages(self):
        return self.__lesMessages
  
    def getPseudo(self):
        return self.__pseudoResist
 
class RadioLondre:
    __leResistant = 0
    __lesMessages = 0
    __cptMsg = 0
    __nbMsg = 0
    __leMessageLu = 0
    __observer = []
 
    def __init__ (self,Resistant):
        self.__leResistant =  Resistant
        self.__lesMessages = Resistant.getMessages()
        self.__nbMsg = len(self.__lesMessages)
 
    def getResistant (self):
        return self.__leResistant
 
    def diffuseMessage(self):
        self.__leMessageLu = "Veuillez écouter  tout  d'abord  quelques  messages  personnels : " + self.__lesMessages[self.__cptMsg]
        return self.__leMessageLu          
 
    def arretEcoute(self):
        if self.__nbMsg == 0 or self.__cptMsg+1 > self.__nbMsg:
            self.__leMessageLu = "Fin de transmission"
            print(self.__leMessageLu)
            return False
        else:
            self.setChanged()
            self.__cptMsg += 1
            return True 

    def setChanged(self):
        for observer in self.__observer:
            observer.update()

    def addObserver(self,observer):
        self.__observer.append(observer)

    #AJOUT de cette fonction, afin de pouvoir choisir quand la radio diffuse
    def radioOn(self):
        print("Debut de diffusion : ")
        while self.arretEcoute() != False:
            print("Diffusion en cours ...")
     
class Envahisseur:
    __pseudoEnvahisseur = 0
    __radioLondres = None
    __MessageLu = []  #Liste des message recu via la radio (même si non traiter ils entendent quand même la radio)

    def __init__ (self,pseudoEnvahisseur,Radio):
        self.__pseudoEnvahisseur = pseudoEnvahisseur
        self.__radioLondres = Radio

    def jecoute(self):
        self.__MessageLu.append(self.__radioLondres.diffuseMessage())

    def update(self):
        self.jecoute()
        
    def run(self):
        print("--- Je suis " + self.__pseudoEnvahisseur + ". Arg je n'aime pas la radio de Londre ---")
 
class GroupeClandestin:
    __pseudoClandestin = None
    __radioLondres = None
    __saboteur = None
    __arretEcoute = False
    __debarquement = False
    __lesMessages = []
    __leMessageEntendu = None
    __leMessageAttendu = None

    def __init__ (self,pseudo,radio,saboteur,MsgAtt):
        self.__pseudoClandestin = pseudo
        self.__radioLondres = radio
        self.__saboteur = saboteur
        self.__leMessageAttendu = MsgAtt

    def jecoute(self):
        
        self.__leMessageEntendu = self.__radioLondres.diffuseMessage()
        self.__lesMessages.append(self.__leMessageEntendu)
        #Verifie si c'est le message attendu
        if self.__leMessageEntendu == "Veuillez écouter  tout  d'abord  quelques  messages  personnels : " + self.__leMessageAttendu: #on se fiche du début vu que c'est toujours pareil
            
            self.__arretEcoute = True
            self.__debarquement = True
            print("-- Le groupe " + self.__pseudoClandestin + " à compris le message " + str(len(self.__lesMessages)) + " --")

    def update(self):
        if self.__arretEcoute == False:
            self.jecoute()  
        
    def run(self):
        if self.__debarquement == True:
            print("--- Un débarquement est prévu ---")
        else:
            print("--- Pas de débarquement ---")
 
class Auditeur:
    __Nom = 0
    __radioLondres = None
    __MessageLu = []  #Liste des message recu via la radio
    __parler = False

    def __init__(self,Nom,Radio,parler):
        self.__Nom = Nom
        self.__radioLondres = Radio
        self.__parler = parler
    
    def jecoute(self):
        self.__MessageLu.append(self.__radioLondres.diffuseMessage())
        if self.__parler == True:
            print("Je suis " + self.__Nom + " et j'ai entendu : " + self.__radioLondres.diffuseMessage())

    def update(self):
        self.jecoute()
        
    def run(self):
        print("--- Je suis " + self.__Nom + " et j'ai écouté la radio ---")

#Main
MessagesRadio = ["Les bananes sont cuites","Haribo c'est pour les grands et le petits","Mon python est mort","Les sanglots longs des violons de l'automne blessent mon cœur d'une langueur monotone.","Le colonel moutarde dans la cuisine avec une matraque"]
LesAlliees = FlotteAlliee("Arme_Anglaise")
DeGaulle = Resistant("DeGaulle",MessagesRadio,LesAlliees)
Radio = RadioLondre(DeGaulle)

#Declaration de envahisseur, Saboteur, GroupeClandestin
Allemands = Envahisseur("Allemands",Radio)
Vomecourt = SaboteurFerroviaire("Vomecourt")
Ventriloquist = GroupeClandestin("Ventriloquist",Radio,Vomecourt,"Les sanglots longs des violons de l'automne blessent mon cœur d'une langueur monotone.")

#Declaration d'un autditeur (class en plus de l'exercice), passer à "True" pour voir les messages capter par l'auditeur
Bob = Auditeur("Bob",Radio,False)

#Ajout des observateurs
Radio.addObserver(Allemands)
Radio.addObserver(Ventriloquist)
Radio.addObserver(Bob)

#Debut de la diffusion
Radio.radioOn()

#Résultat après avoir écouté la radio
Allemands.run()
Ventriloquist.run()
Bob.run()