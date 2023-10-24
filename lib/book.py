#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def get_page_count(self):
        return self._new_count
    
    def set_page_count(self, newCount):
        if isinstance(newCount, int):
            self._new_count = newCount
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    

the_hobbit = Book(title="The Hobbit", page_count=287)
print(the_hobbit.page_count)