import os
import re
import math
import sys
import string

dictionary = {}
dictionaryCount = set()
wordCount = {}

stopWords=['great','me','are','one','rooms','stayed','an','up','out','no']

symbols= set(string.punctuation)

def removeSymbol(word):
    for symbol in symbols:
        word = word.replace(symbol,'')
    return word




def NBlearn(fileLocation):
    with open(fileLocation) as f:
        NBclass = ''
        if 'positive' in fileLocation:
            NBclass += 'Positive'
        else:
            NBclass += 'Negative'
        if 'deceptive' in fileLocation:
            NBclass += 'Deceptive'
        else:
            NBclass += 'Truthful'

        data = re.split(r"[,;!#^&*()\.\- ]+", f.read())
        for word in data:
            words = removeSymbol(word)
            words = words.lower()
            if words not in stopWords and words != '':
                dictionaryCount.add(words)
                if NBclass in dictionary:
                    wordList = dictionary[NBclass]
                    if words in wordList:
                        wordList[words] += 1
                    else:
                        wordList[words] = 1
                else:
                    dictionary[NBclass] = {words: 1}
                if NBclass in wordCount:
                        wordCount[NBclass] += 1
                else:
                        wordCount[NBclass] = 1

if len(sys.argv) != 2:
    print "Enter the location of the training data"
else:
    rootFolder = sys.argv[1]
    data = []
    for root, dirs, files in os.walk(rootFolder, topdown=False):
        for name in files:
            if name.endswith(".txt") and not name.startswith('README'):
                data.append(os.path.join(root, name))
    for d in data:
        NBlearn(d)

with open('nbmodel.txt','w') as fileObject:
    for NBclass, wordList in dictionary.iteritems():
        for word, count in wordList.iteritems():
            probability = float(count+1)/(wordCount[NBclass]+len(dictionary))
            finalProbability =  math.log(probability)
            fileObject.write(word+'<<'+NBclass+'<<'+str(finalProbability) + '\n')
        probability = float(1)/(wordCount[NBclass]+len(dictionary))
        finalProbability =  math.log(probability)
        fileObject.write('>><<'+NBclass+'<<'+str(finalProbability) + '\n')
        print('>><<'+NBclass+'<<'+str(finalProbability) + '\n')

       
