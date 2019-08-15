import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pickle
import os
from sklearn.preprocessing import OneHotEncoder
from numpy import array


def preprocess(word):
    lem = nltk.stem.WordNetLemmatizer()
    result = re.sub('[^a-zA-Z]', ' ', word)
    result = result.lower()
    result = result.split()
    result = [lem.lemmatize(word) for word in result if not word in set(stopwords.words('english'))]
    return result


def plotfreq(array, title):
    strver = str(array)
    strver = strver.replace("'", "")
    strver = strver.replace(",", "")
    strver = strver.replace("[", "")
    strver = strver.replace("]", "")
    strver = ' '.join(word for word in strver.split() if len(word) > 2)
    tokens = nltk.tokenize.word_tokenize(strver)
    fd1 = nltk.FreqDist(tokens)
    plt.figure(figsize=(20, 15))
    plt.title(title)
    plt.xlabel("Word")
    plt.ylabel("Use Frequency")
    fd1.plot(20, cumulative=False)
    plt.show()
    return fd1


def wordfreq(word):
    cat_find = ans_find = que_find = comFind = ""
    for i in catFreq.most_common():
        if i[0] == word.lower():
            cat_find = "Category: " + str(i) + " Frequency: " + str(catFreq.most_common().index(i) + 1)
    for i in ansFreq.most_common():
        if i[0] == word.lower():
            ans_find = "Answer: " + str(i) + " Frequency: " + str(ansFreq.most_common().index(i) + 1)
    for i in queFreq.most_common():
        if i[0] == word.lower():
            que_find = "Question: " + str(i) + " Frequency: " + str(queFreq.most_common().index(i) + 1)
    for i in comFreq.most_common():
        if i[0] == word.lower():
            comFind = "Comments: " + str(i) + " Frequency: " + str(comFreq.most_common().index(i) + 1)
    if cat_find != "":
        print(cat_find)
    else:
        print(word + " Not found in Category!")
    if ans_find != "":
        print(ans_find)
    else:
        print(word + " Not found in Answer!")
    if que_find != "":
        print(que_find)
    else:
        print(word + " Not found in Question!")
    if comFind != "":
        print(comFind)
    else:
        print(word + " Not found in Comments!")


def saveprocessed(saved):
    pickle.dump(saved, open("jep.s", "wb"))


def loadprocessed():
    return pickle.load(open("jep.s", "rb"))


def onehot(strlist):
    token = nltk.tokenize.word_tokenize(strlist)
    token = array(token)
    token = token.reshape(1, -1)
    oe = OneHotEncoder()
    onehot_encoded = oe.fit_transform(token)
    return onehot_encoded


data = []

if os.path.exists("jep.s"):
    data = loadprocessed()
else:
    filename = 'C:/Users/naomi/Downloads/all.tsv'

    dataset = pd.read_csv(filename, delimiter='\t', quoting=3)

    catTemp = []
    comTemp = []
    ansTemp = []
    queTemp = []

    for i in range(0, 349675):
        if i % 1000 == 0:
            print(i)
        # Preprocess the data to make it useable
        cat = preprocess(dataset['category'][i])
        com = preprocess(dataset['comments'][i])
        ans = preprocess(dataset['answer'][i])
        que = preprocess(dataset['question'][i])
        catTemp.append(cat)
        comTemp.append(com)
        ansTemp.append(ans)
        queTemp.append(que)
        data = [catTemp, comTemp, ansTemp, queTemp]

    saveprocessed(data)

catFreq = plotfreq(data[0], "Categories")
ansFreq = plotfreq(data[2], "Answers")
queFreq = plotfreq(data[3], "Questions")
comFreq = plotfreq(data[1], "Comments")
