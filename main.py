# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Turtle, Screen
from prettytable import PrettyTable

#git remote add origin https://github.com/user/repo.git

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

table = PrettyTable()

table.add_column("Pokemon Name", ["Squirtle", "charmander", "vespiqueen"])
table.add_column("Type", ["fire", "water", "electric"])

table.align = "c"

print(table)
