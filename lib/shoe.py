#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size 
        self._condition = "Used"

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,brand):
        self._brand = brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if isinstance(size,int):
         self._size = size
        else:
         print("size must be an integer")
        
    def cobble(self):
       print("Your shoe is as good as new!")
       self._condition = "New"

   

AF1 =Shoe(brand = "Nike", size = 9)
print(AF1.brand,AF1.size)
