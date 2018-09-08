from difflib import SequenceMatcher

print(round((SequenceMatcher(None, open('sample1.pdf').read(), open('sample.pdf').read())).ratio(),2))