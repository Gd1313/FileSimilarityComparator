from show import compareImg,compareText
functions={
    'image': compareImg,
    'text': compareText,
}

def useFunc(what, firstFile,secondFile):
    functions[what](firstFile,secondFile)
    return;

filters={
    '.bmp':useFunc('image',firstFile,secondFile),
    '.txt':useFunc('text',firstFile,secondFile)
}


