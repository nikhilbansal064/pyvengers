# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:48:47 2018

@author: Nikhil Bansal

    * Class - Template to create object. Each class creat a new data type.
   
    * Object - Encapsulation of variables(property) adn function(behaviour) in single entity.
    
    * data members - Data attributes need not be declared.like local variables, 
                   they spring into existence when they are first assigned to.
                   Example - love variable in TItal class (not declared in class but came in
                   for thanos(only for thanos not for thanos 2) at line 61)
                   
    * instance variable - data that is unique for each instance of that class.
    * class variable - data that is shared by every instance of that class.              
    
"""


class Titan:
    
    #constructor
    def __init__(self, life = 3):
        #here life is an "instance variable"  for this class
        self.life = life
    
    
    #class variable i.e each titan has the same goal
    goal = "To win the world"
    
    # behaviours
    def getGoal(self):
        print(self.goal)
        
    def getLove(self):
        print(self.love)
        
    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print("You cant kill me. I have %d life left." % (self.life))

    
    # When u attack a titan, U actually offering him one more life, U fool.
    def attacked(self):
        print("Ha Ha Ha .Thanks for the life, U fool.")
        self.life += 1

    # U can onle take life of a tital if you take a headshot
    def headShot(self):
        print("Ouch")
        self.life -= 1


thanos = Titan()
thanos.checkLife()
thanos.love = "Gamora"
thanos.getGoal()
thanos.getLove()
thanos2 = Titan(6)
thanos2.checkLife()
thanos2.getGoal()
