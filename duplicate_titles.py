import titles
from titles import titlesAll

def duplicatesF():
    duplicates=[]
    counter = 0
    for i in titlesAll:
        if i in titlesAll[counter+1:]:
            duplicates.append(i)
        else:
            pass
        counter += 1
    print('\nlista duplikatów:')
    return print(list(set(duplicates)),'\n')
