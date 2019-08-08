import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pickle
import os


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
    strver = ' '.join(word for word in strver.split() if len(word) > 2)
    tokens = nltk.tokenize.word_tokenize(strver)
    fd1 = nltk.FreqDist(tokens)
    plt.figure(figsize=(25, 20))
    plt.title(title)
    plt.xlabel("Word")
    plt.ylabel("Use Frequency")
    fd1.plot(20, cumulative=False)
    plt.show()


def saveprocessed(saved):
    pickle.dump(saved, open("jep.s", "wb"))


def loadprocessed():
    return pickle.load(open("jep.s", "rb"))


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

plotfreq(data[0], "Categories")
plotfreq(data[2], "Answers")
plotfreq(data[3], "Questions")
plotfreq(data[1], "Comments")
