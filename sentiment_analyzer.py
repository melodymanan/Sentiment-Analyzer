import sys
sys.setExecutionLimit(500000)

punctuation_char = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(Str):
    for pointer in punctuation_char:
        Str = Str.replace(pointer, "")
    return Str

def get_pos(Str):
    newStr = strip_punctuation(Str)
    lstNewStr = newStr.split()
    counter = 0
    for word in lstNewStr:
        word = word.lower()
        for pointer in positive_words: 
            
            if word == pointer:
                counter += 1
    return counter

def get_neg(Str):
    newStr = strip_punctuation(Str)
    lstNewStr = newStr.split()
    counter = 0
    for word in lstNewStr:
        word = word.lower()
        for pointer in negative_words:  
            if pointer == word:
                counter += 1
    return counter            

TwitterFile = open("project_twitter_data.csv","r")
resultFile = open("resulting_data.csv","w")
def gettingOutput(resultFile):
    resultFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultFile.write("\n")
    linesTwitter = TwitterFile.readlines()
    noHeader = linesTwitter.pop(0)
    for lines in linesTwitter:
        lst = lines.strip().split(',')
        resultFile.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))    
        resultFile.write("\n")

        
gettingOutput(resultFile)
resultFile.close()
TwitterFile.close()
