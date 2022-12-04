# encoding:utf-8

with open("copyFromArticle.txt",'r',encoding='utf-8') as myWords:

    myWords = ''.join(myWords)


def deleteEmptySpacesFromPapers(string):
    return " ".join(string.split())
    

x = deleteEmptySpacesFromPapers(myWords)
print(deleteEmptySpacesFromPapers(myWords))