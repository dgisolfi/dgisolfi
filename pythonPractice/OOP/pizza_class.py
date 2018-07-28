#!/usr/bin/python3
# person_class.py
# 2018-07-28
# Purpose: To review python Object Oriented Programming

# To run an instance of this file in a interactive python shell add the -i tag when running
# EX: python3 -i class.py

class Food:
    def __init__(self, dish_name, place_origin, is_healthy):
        self.dish_name = dish_name
        self.place_origin = place_origin
        self. is_healthy = is_healthy
        print('creating food object')
    
    def getDishName(self):
        return self.dish_name

    def getOrigin(self):
        return self.place_origin

    def getIsHealthy(self):
        return self.is_healthy
    
    def __del__(self):
        print('destroying food object')

class Pizza(Food):
    def __init__(self, toppings, size, price):
        Food.__init__(self, 'Pizza', 'Italy', False)
        self.toppings = toppings
        self.size = size
        self.price = price

    def getToppings(self):
        return self.toppings
    
    def getSize(self):
        return self.size
    
    def getPrice(self):
        return self.price
        
    
large_pepperoni_pie = Pizza(['pepperoni', 'cheese'], 'Large', 17.99)