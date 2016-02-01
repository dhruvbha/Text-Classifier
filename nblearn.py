
suffixes=['ate','en','ify','fy','ize','ise',,'able','ible','al','esque','ful','ic','ical','ious','ous',
'ish','ive','less','y','acy','al','ance','ence','dom','er','or','ism','ist','ity','ty','ment','ness',
'ship','sion','tion']
def suffixStrip(word):
    if word.endswith(tuple(suffixes)):
        for suffix in suffixes:
            if not word.endswith(suffix):
                return word
            return word[:len(word)-len(suffix)]

stopWords=['a','about','above','after','again','against','all','am','an','and','any','are','as','at','be',
'because','been','before','being','below','between','both','but','by','cannot','could','did','do','does',
'doing','down','during','each','few','for','from','further','had','has','have','having','he','her','here',
'hers','herself','him','himself','his','how','i','if','in','into','is','it','its','itself','me','more',
'most','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours',
'whom','why','with','would','you','your','yours','yourself','yourselves','this','those','through','to',
'too','under','until','up','very','was','we','were','what','when','where','which','while','who','ourselves',
'out','over','own','same','she','should','so','some','such','than','that','the','their','theirs','them',
'themselves','then','there','these','they']

symbols=['?','.','!','/',';',':',',','r"','@','#','\']
def removeSymbol(word):
    for symbol in symbols:
        word = word.replace(symbol,'')
    return word

trainingData = 'op_spam_train/'
negative = 'negative_polarity/'
positive = 'positive_polarity/'
deceptive = 'deceptive_from_MTurk/'
truthful = 'truthful_from_'
truthSource = ['Web' , 'TripAdvisor']
polarity = [negative, positive]
veracity = [deceptive, truthful]

mapping = {'negative_polarity':'negative','positive_polarity': 'positive','deceptive_from_MTurk':'deceptive',
'truthful_from': 'truthful'}

for item in polarity:
   for type in veracity:
       folderName = ''
       if type.startswith('truthful') and item.startswith('negative'):
           folderName = 'truthful_from_Web'
       elif type.startswith('truthful') and item.startswith('positive'):
           folderName = 'truthful_from_TripAdvisor'
