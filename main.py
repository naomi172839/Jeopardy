import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

filename = 'C:/Users/naomi/Downloads/all.tsv'

dataset = pd.read_csv(filename, delimiter='\t', quoting=3)

catTemp = []
comTemp = []
ansTemp = []
queTemp = []

for i in range(0, 349675):
    if i % 1000 == 0:
        print(i)
    # removes special characters from all columns
    category = re.sub('[^a-zA-Z]', ' ', dataset['category'][i])
    comments = re.sub('[^a-zA-Z]', ' ', dataset['comments'][i])
    answer = re.sub('[^a-zA-Z]', ' ', dataset['answer'][i])
    question = re.sub('[^a-zA-Z]', ' ', dataset['question'][i])

    # makes all lowercase
    category = category.lower()
    comments = comments.lower()
    answer = answer.lower()
    question = question.lower()

    # makes string into list so that stopwords can be removed
    category = category.split()
    comments = comments.split()
    answer = answer.split()
    question = question.split()

    # Lemmatization uses dictionary lookup to determine the base root of the words
    l = nltk.stem.WordNetLemmatizer()

    # remove words without significance
    category = [l.lemmatize(word) for word in category if not word in set(stopwords.words('english'))]
    category = ' '.join(category)
    catTemp.append(category)
    comments = [l.lemmatize(word) for word in comments if not word in set(stopwords.words('english'))]
    comments = ' '.join(comments)
    comTemp.append(comments)
    answer = [l.lemmatize(word) for word in answer if not word in set(stopwords.words('english'))]
    answer = ' '.join(answer)
    ansTemp.append(answer)
    question = [l.lemmatize(word) for word in question if not word in set(stopwords.words('english'))]
    question = ' '.join(question)
    queTemp.append(question)

strVer = str(catTemp)
strVer = strVer.replace("'", "")
strVer = strVer.replace(",", "")
strVer = ' '.join(word for word in strVer.split() if len(word)>2)
tokens = nltk.tokenize.word_tokenize(strVer)
fd1 = nltk.FreqDist(tokens)
plt.figure(figsize=(15,10))
plt.title("Categories")
plt.xlabel("Word")
plt.ylabel("Use Frequency")
fd1.plot(20, cumulative=False)
plt.show()

strVer = str(ansTemp)
strVer = strVer.replace("'", "")
strVer = strVer.replace(",", "")
strVer = strVer.replace("one", "")
strVer = ' '.join(word for word in strVer.split() if len(word)>2)
tokens = nltk.tokenize.word_tokenize(strVer)
fd2 = nltk.FreqDist(tokens)
plt.figure(figsize=(15,10))
plt.title("Answers")
plt.xlabel("Word")
plt.ylabel("Use Frequency")
fd2.plot(20, cumulative=False)
plt.show()

strVer = str(queTemp)
strVer = strVer.replace("'", "")
strVer = strVer.replace(",", "")
strVer = ' '.join(word for word in strVer.split() if len(word)>2)
tokens = nltk.tokenize.word_tokenize(strVer)
fd3 = nltk.FreqDist(tokens)
plt.figure(figsize=(15,10))
plt.title("Questions")
plt.xlabel("Word")
plt.ylabel("Use Frequency")
fd3.plot(20, cumulative=False)
plt.show()

strVer = str(comTemp)
strVer = strVer.replace("'", "")
strVer = strVer.replace(",", "")
strVer = strVer.replace("alex", "")
strVer = ' '.join(word for word in strVer.split() if len(word)>2)
tokens = nltk.tokenize.word_tokenize(strVer)
plt.figure(figsize=(15,10))
plt.title("Comments")
plt.xlabel("Word")
plt.ylabel("Use Frequency")
fd4 = nltk.FreqDist(tokens)
fd4.plot(20, cumulative=False)
plt.show()
