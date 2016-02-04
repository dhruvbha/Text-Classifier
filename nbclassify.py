import sys
import os
import re
import math
import sys
import string
#import nblearn
#from nblearn import *


symbols= set(string.punctuation)
def removeSymbol(word):
    for symbol in symbols:
        word = word.replace(symbol,'')
    return word

def wordProbability1():
   wordProb = {}
   with open('nbmodel.txt') as data:
       information = data.readlines()

       for info in information:
           if info.startswith('>>'):
               print 'info is '+info

           info1 = info.split('<<')
           if len(info1) != 3:
               continue
           word = info1[0]
           NBclass = info1[1]
           probability = info1[2][:-1]
           if word in wordProb:
               wordProb[word][NBclass] = probability
           else:
               wordProb[word] = {NBclass: probability}
   return wordProb

stopWords=['great','me','are','one','rooms','stayed','an','up','out','no']

def NBclassify(fileLocation):
    NBclass1 = ''
    map1 = {}
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

        words_1=[]

        data = re.split(r"[,;!#^&*()\.\- ]+", f.read())

        for word in data:
            words = removeSymbol(word)

            words = words.lower()
            if words not in stopWords and words != '':
                words_1.append(words)

        # print wordProbability1()
        # print wordProbability['']
        # print "HelloWorld"
        for NBclass in ['NegativeTruthful','PositiveDeceptive','PositiveTruthful','NegativeDeceptive']:
            probability = 0
            for word in words_1:
                if word in wordProbability:
                    probWord = wordProbability[word]

                    if NBclass in probWord:
                            probability += float(probWord[NBclass])
                    else:
                        probWord = wordProbability['>>']
                        probability += float(probWord[NBclass])
                else:
                    probWord = wordProbability['>>']
                    probability += float(probWord[NBclass])

            map1[NBclass] = probability
        # print "Hello"
        NBclass='NegativeDeceptive'
        max1=map1['NegativeDeceptive']
        for NBclass, probability in map1.iteritems():

            if probability > max1:
                max1 = probability
                NBclass1 = NBclass
    print map1
    print NBclass1
    return NBclass1

# print 'starting'

wordProbability = wordProbability1()

print '=>'+str(wordProbability1()['>>'])
if len(sys.argv) != 2:
    print "Missing the location of the test data"
else:
    rootFolder = sys.argv[1]
    testFiles=[]
    for root, dirs, files in os.walk(rootFolder, topdown=False):
        for name in files:
            if name.endswith(".txt") and not name.startswith('README'):
                testFiles.append(os.path.join(root, name))

    # print 'README.md' in testFiles
    # print 'got files' + str(testFiles)
    output = open('nboutput.txt', 'w')
    for file in testFiles:
        NBclass = NBclassify(file)
        # print NBclass
        if NBclass == 'NegativeTruthful':
            output.write('truthful negative '+file)
        elif NBclass == 'PositiveDeceptive':
            output.write('deceptive positive '+file)
        elif NBclass == 'PositiveTruthful':
            output.write('truthful positive '+file)
        else:
            output.write('deceptive negative '+file)
        output.write('\n')
