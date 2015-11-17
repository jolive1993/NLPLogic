import wikipedia
import sys, os
from pymongo import MongoClient
from uprint import *
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

class Database:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.wikitext
        self.content = self.db.content
        self.trainSet = self.db.trainset
        self.unrelated = self.db.unrelated
    def archiveWiki(self, className, pageName):
        page = wikipedia.page(str(pageName))
        result = className.insert_one({
            "title":page.title,
            "url":page.url,
            "content":page.content,
            "links":page.links
            })
    def checker(self):
        print(self.content.count())
    def contentGrabber(self, pageName):
        result = self.content.find_one({'title':str(pageName)})
        content = result['content']
        return content
    def extractDataSet(self, name):
        trimmedSentList = []
        content = self.contentGrabber(str(name))
        blob = TextBlob(content)
        for sentence in blob.sentences:
            if sentence.sentiment.polarity > .3:
                trimmedSentList.append(sentence)
        return trimmedSentList   
class Classify:
    def __init__(self):
        train = []
        self.classifer = NaiveBayesClassifier(train)
    def doclass(self, dataSet):
        for sentence in dataSet:
            if (self.classifer.classify(sentence)) == "rel":
                uprint(sentence + " rel")
    def updateTrainPos(self, dataSet):
        train = []
        for sentence in dataSet:
            train.append((sentence, "rel"))
        self.classifer.update(train)
    def updateTrainNeg(self, dataSet):
        train = []
        for sentence in dataSet:
            train.append((sentence, "irel"))
        self.classifer.update(train)
        
        


database = Database()
classify = Classify()
buckets = database.contentGrabber("Ontology")
uprint(buckets)

