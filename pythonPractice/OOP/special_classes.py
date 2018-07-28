#!/usr/bin/python3
# person_class.py
# 2018-07-28
# Purpose: To review python Object Oriented Programming

# To run an instance of this file in a interactive python shell add the -i tag when running
# EX: python3 -i class.py

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __del__(self):
        #Destroys instance of class
        print('Animal Destroyed :(')

class FourLegs:
    def hasLegs(self):
        return 4

#Dog Class inherits the Animal and FourLegs class methods and properties
class Dog(Animal, FourLegs):
    
    def __init__(self, name, breed, is_big):
        Animal.__init__(self, name, 'Dog')
        self.breed = breed
        self.is_big = is_big
        print('Creating DOGO: ' + self.getName())
    
    #Overide getSpecies method inherited from the Animal class    
    def getSpecies(self):
        return self.species, self.breed
    
    def getis_big(self):
        return self.is_big
    

#Intialize a instance of the Animal class
kevin = Dog('Kevin', 'Shiba Inu', False)