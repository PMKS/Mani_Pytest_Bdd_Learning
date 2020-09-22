'''
example only consider from below link for liearning purpose
https://github.com/PMKS/tau-pytest-bdd/blob/master/cucumbers.py

About this file

There is a Basket which is capable of holding maximum 9 items
if exceds raise Value Error when try to keep more than 9 items in the baseket
and similarly raises Value Error when trying to remove any item when Basket is empty

'''


class Basket:

    def __init__(self, initial_count=0, max_count=9):
        if initial_count < 0:
            raise ValueError("Count should not be negitive")
        elif max_count > 10:
            raise ValueError("Max 9 items can only be palced in to basket")

        self._count = initial_count
        self._maxcount = max_count

    @property
    def count(self):
        return self._count

    @property
    def isFull(self):
        return self._count == self._maxcount

    @property
    def isEmpty(self):
        return self._count == 0

    @property
    def max_count(self):
        return self._maxcount

    def addItem(self, count=1):
        new_count = self._count + count
        if new_count > self._maxcount:
            raise ValueError("Exceeeds Max Limit")
        self._count = new_count

    def removeItem(self, count=1):
        new_count = self._count - count
        if new_count < 0:
            raise ValueError("Trying to remove item when Basket is Empty")
        self._count = new_count
