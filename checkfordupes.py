#check for duplicates in a list of tuples
def checkForDupes(l):
    newList = []
    for i in l:
        newList.append(i[0])
        newList.append(i[1])
    if len(newList) == len(set(newList)):
        return False
    else:
        return True 
