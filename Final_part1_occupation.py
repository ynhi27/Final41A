# Y Nhi Tran
# Final part 1
# This program write a menu-driven program for De Anza College Food Court.
# Final_part1_occupation.py

class Occupation:
    _tax: float

    def __init__(self):
        self._tax = 0.0
        
    def tax(self):
        return self._tax

class Student(Occupation):
    def __init__(self, tax=0.0):
        super().__init__()
        self._tax = tax

    @property
    def tax(self):
        return self._tax


class Staff(Occupation):
    def __init__(self, tax=9/100):
        super().__init__()
        self._tax = tax

    @property
    def tax(self):
        return self._tax










