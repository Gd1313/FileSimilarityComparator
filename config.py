from show import compareImg,compareText
import re
functions={
    '.bmp': compareImg,
    '.txt': compareText
}

def task(array, path,inputPercent):
        for item1, item2 in array:
            if re.findall(r'\..+', item1)[0] == re.findall(r'\..+', item2)[0]:
                percent = functions[re.findall(r'\..+', item1)[0]](path+item1, path+item2)
                if percent > inputPercent/100:
                    print('File {0} simular to file {1} with {2} %'.format(item1,item2,percent*100))
        return

