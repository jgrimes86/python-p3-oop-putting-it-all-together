#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if type(new_size) == int:
            self._size = new_size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

nike = Shoe(brand="Nike", size=11)
print(nike.size)