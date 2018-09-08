from diffimg import diff
from difflib import SequenceMatcher

def compareImg(firstFile,secondFile):
  return round(diff(firstFile, secondFile), 2)


def compareText(firstFile,secondFile):
    return round((SequenceMatcher(None, open(firstFile).read(), open(secondFile).read())).ratio(),2)