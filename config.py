from show import compareImg,compareText
import re
functions={
    '.bmp': compareImg,
    '.txt': compareText,
}

def only_same(array):
    new_array = []
    for item1, item2 in array:
        if re.findall(r'\..+', item1)[0] == re.findall(r'\..+', item2)[0]:
                new_array.append(item1)
                new_array.append(item2)

    return new_array;
'''def useFunc(what, firstFile,secondFile):
    functions[what](firstFile,secondFile)
    return;'''

'''filters={
    '.bmp':useFunc('image',firstFile,secondFile),
    '.txt':useFunc('text',firstFile,secondFile)
}'''

