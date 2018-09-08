from config import task
import itertools
import os
import re

path=raw_input()
percent=float(raw_input())
information=[]


for fileName in os.walk(path):
    information.extend(fileName)
files = information[2]

array = itertools.combinations(files, 2)
task(array, path,percent)
