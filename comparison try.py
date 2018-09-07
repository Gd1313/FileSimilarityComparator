#import config
import itertools
import os

files=[]

for fileName in os.walk("task1/blur"):
    files.append(fileName)

for firstFile,secondFile in itertools.combinations(files, 2):
    print(firstFile+" "+secondFile)
'''def imageComparison( firstFile, secondFile):
    from diffimg import diff
    return round(diff(firstFile,secondFile));

def textComparison( firstFile, secondFile):
    from difflib import SequenceMatcher
    return (SequenceMatcher(None, open(firstFile).read(), open(secondFile).read())).ratio();

def collectFiles(path,percent):
    import os,glob
    files=[]
    os.chdir(path)
    for file in glob.glob("*.txt"):
        files.append(file)
    import itertools
    for a, b in itertools.combinations(files, 2):
          print("Image "+a+" simular to image "+b+" with percent "+textComparison(a, b))  
           # if textComparison(a, b)>percent
              
    return;

collectFiles ("/home/user/Desktop/task1/blur",0.7)        
######################################
    from PIL import Image
    import glob
    imageList=[]
    for filename in glob.glob(path+'/*.'+['.bmp', '.jpeg', '.png']): 
        im=Image.open(filename)
        image_list.append(im)
    import itertools
    for a, b in itertools.combinations(imageList, 2):
        if imageComparison(a, b)>percent
            print("Image "+a+" simular to image"+b+" with percent "+imageComparison(a, b))
    return;


def collectText(path,percent):
    import glob,os
    textList=[]
    for filename in glob.glob(path+'/*.'+['.txt', '.doc']): 
        im=Image.open(filename)
        image_list.append(im)
    import itertools
    for a, b in itertools.combinations(imageList, 2):
        if imageComparison(a, b)>percent
            print("Image "+a+" simular to image"+b+" with percent "+imageComparison(a, b))
    return;    

    import glob, os
os.chdir("/mydir")
for file in glob.glob("*.txt"):
    print(file)'''