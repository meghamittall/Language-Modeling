"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    file = open(filename, "r")
    words_lst = []
    for line in file:
        if len(line) > 1:
            line = line.strip()
            wordString = line.split()
            words_lst.append(wordString)
    file.close()
    return words_lst

'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    corpus_length = sum(len(row) for row in corpus)
    return corpus_length


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    unique_unigrams_lst =[]
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            if corpus[i][j] not in unique_unigrams_lst:
                unique_unigrams_lst.append(corpus[i][j])
    # print(unique_unigrams_lst)
    return unique_unigrams_lst


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    unigrams_count_dict = {}
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            if corpus[i][j] not in unigrams_count_dict:
                unigrams_count_dict[corpus[i][j]] = 0
            unigrams_count_dict[corpus[i][j]] += 1
    # print(unigrams_count_dict)
    return unigrams_count_dict


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    start_words_lst = []
    for i in range(len(corpus)):
        if corpus[i][0] not in start_words_lst:
            start_words_lst.append(corpus[i][0])
    # print(start_words_lst) 
    return start_words_lst


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    start_words_count_dict = {}
    for i in range(len(corpus)):
        if corpus[i][0] not in start_words_count_dict:
            start_words_count_dict[corpus[i][0]]=0
        start_words_count_dict[corpus[i][0]]+=1
    # print(start_words_count_dict)
    return start_words_count_dict


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    bigrams_dict={}
    for i in range(len(corpus)):
        for j in range(len(corpus[i])-1):
            if corpus[i][j] not in bigrams_dict.keys():
                bigrams_dict[corpus[i][j]] = {}
            if corpus[i][j+1] not in bigrams_dict[corpus[i][j]].keys():
                bigrams_dict[corpus[i][j]][corpus[i][j+1]]= 1
            else:
                bigrams_dict[corpus[i][j]][corpus[i][j+1]]+= 1
    # print(bigrams_dict)
    return bigrams_dict


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    uniform_prob_lst=[]
    for i in range(len(unigrams)):
        w=1/len(unigrams)
        uniform_prob_lst.append(w)
    # print(uniform_prob_lst)
    return uniform_prob_lst


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    unigrams_probs_lst=[]
    for i in range(len(unigrams)):
        for key, value in unigramCounts.items():
            if key == unigrams[i]:
                prob = value/totalCount
                unigrams_probs_lst.append(prob)
    # print(unigrams_probs_lst)
    return unigrams_probs_lst


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    bigram_prob_dict = {}
    for prevWord in bigramCounts:
        words=[]
        probs=[]
        for key, value in bigramCounts[prevWord].items():
            prob = value/unigramCounts[prevWord]
            words.append(key)
            probs.append(prob)
            temp_dict={}
        temp_dict["words"]=words
        temp_dict["probs"]=probs
        # print(temp_dict)
        bigram_prob_dict[prevWord]=temp_dict
    # print(dict)
    return bigram_prob_dict


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    top_words_dict={}
    words_dict = {}                                                                                                   
    for i in range(len(words)):
        if words[i] not in ignoreList:
            words_dict[words[i]]=(probs[i])
    for key, value in sorted(words_dict.items(), key=lambda item: item[1], reverse=True):
        top_words_dict[key]=value
        if len(top_words_dict) == count:
            break
    print(top_words_dict)
    return top_words_dict


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    sentence=" "
    for x in range(count):
        lst = choices(words, weights=probs)
        
        sentence+=lst[0]+" "
        # print(lst[0])
    #  words_list.append(lst[0])
    # sentence=" "
    # print(sentence.join(words_list))
    return sentence


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    words_lst = []
    for x in range(count):
        if (len(words_lst)==0 or words_lst[-1]=="."):
            word=choices(startWords, startWordProbs)
            words_lst.append(word[0])
        else:
            key=words_lst[-1]
            # print(key)
            word_prob_dict=bigramProbs[key]
            word=choices(word_prob_dict['words'], word_prob_dict['probs'])
            words_lst.append(word[0])
    #print(words_lst)
    sentence=" "
    #print(sentence.join(words_lst))
    return (sentence.join(words_lst))


    


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    unique_unigrams_lst=buildVocabulary(corpus)
    unigrams_count_dict=countUnigrams(corpus)
    unigrams_probs_lst=buildUnigramProbs(unique_unigrams_lst, unigrams_count_dict, getCorpusLength(corpus))
    top_words_dict=getTopWords(50, unique_unigrams_lst, unigrams_probs_lst, ignore)
    barPlot(top_words_dict, "Graph the Top 50 Words")

    return None


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    start_words_lst=getStartWords(corpus)
    start_words_count_dict=countStartWords(corpus)
    start_words_probs_lst=buildUnigramProbs(start_words_lst, start_words_count_dict, getCorpusLength(corpus))
    top_start_words_dict=getTopWords(50, start_words_lst, start_words_probs_lst, ignore)
    barPlot(top_start_words_dict, "Graph the Top Starting Words")


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    unigrams_count_dict=countUnigrams(corpus)
    bigrams_dict=countBigrams(corpus)
    bigram_prob_dict=buildBigramProbs(unigrams_count_dict, bigrams_dict)
    top_words_dict=getTopWords(10, bigram_prob_dict[word]['words'], bigram_prob_dict[word]['probs'], ignore)
    # print(top_words_dict)
    barPlot(top_words_dict, "Graph the Top Bigram")

    return None


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    first_prob_lst=[]
    second_prob_lst=[]
    resulted_dict={}
    words_lst1, words_lst2 = buildVocabulary(corpus1), buildVocabulary(corpus2)
    count_dict1, count_dict2 = countUnigrams(corpus1), countUnigrams(corpus2)
    probs_lst1 = buildUnigramProbs(words_lst1, count_dict1, getCorpusLength(corpus1)) 
    probs_lst2 = buildUnigramProbs(words_lst2, count_dict2, getCorpusLength(corpus2))
    top_words_dict1=getTopWords(topWordCount, words_lst1, probs_lst1, ignore)
    top_words_dict2=getTopWords(topWordCount, words_lst2, probs_lst2, ignore)
    combine_lst=list(top_words_dict1.keys()) + list(top_words_dict2.keys())
    top_words_lst=list(dict.fromkeys(combine_lst))
    for i in range(len(top_words_lst)):
        if top_words_lst[i] in words_lst1:
            ind = words_lst1.index(top_words_lst[i])
            first_prob_lst.append(probs_lst1[ind])
        else:
            first_prob_lst.append(0)
        if top_words_lst[i] in words_lst2:
            ind = words_lst2.index(top_words_lst[i])
            second_prob_lst.append(probs_lst2[ind])
    resulted_dict["topWords"]=top_words_lst
    resulted_dict["corpus1Probs"]=first_prob_lst
    resulted_dict["corpus2Probs"]=second_prob_lst
    # print("resulted_dict=", resulted_dict)
    return resulted_dict
'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    resulted_dict=setupChartData(corpus1, corpus2, numWords)
    sideBySideBarPlots(resulted_dict["topWords"], resulted_dict["corpus1Probs"], resulted_dict["corpus2Probs"], name1, name2, title)
    return None


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    resulted_dict=setupChartData(corpus1, corpus2, numWords)
    scatterPlot(resulted_dict["corpus1Probs"], resulted_dict["corpus2Probs"], resulted_dict["topWords"], title)
    return None


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    #test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    test.runWeek1()
    # test.testCountBigrams()

    # Uncomment these for Week 2 ##
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    #test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()

    # test.testGenerateTextFromBigrams()
    # Uncomment these for Week 3 
    test.testSetupChartData()
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()
