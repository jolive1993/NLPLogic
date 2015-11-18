import wikipedia
import sys, os
from pymongo import MongoClient
from uprint import *
from textblob import TextBlob

class Database:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.wikitext
        self.content = self.db.content
        self.relationships = self.db.relationships
    def query(self):
        sub = str(input("Enter name of subject"))
        if self.content.find_one({'title':str(sub)}) == None:
            self.archiveWiki(sub)
        return sub
    def archiveWiki(self, pageName):
        page = wikipedia.page(str(pageName))
        result = self.content.insert_one({
            "title":page.title,
            "url":page.url,
            "content":page.content,
            "links":page.links
            })
    def checker(self):
        print(self.relationships.count())
        print(self.relationships.find_one({'title':"Cat"}))
    def contentGrabber(self, pageName):
        result = self.content.find_one({'title':str(pageName)})
        content = result['content']
        return content
    def extractDataSet(self, name):
        content = self.contentGrabber(str(name))
        blob = TextBlob(content)
        return blob
    def checkForRelationDB(self, sub):
        if self.relationships.find_one({'title':str(sub)}) == None:
            result = False
        else:
            result = True
        return result
    def checkForRelationSub2(self, sub1, sub2):
        dbEntry = self.relationships.find_one({'title':str(sub1)})
        try:
            result = dbEntry[sub2]
        except:
            result = None
        return result
    def createNewRelation(self, sub1, sub2, relationship):
        self.relationships.insert_one({'title':sub1, sub2:relationship})
    def updateRelation(self, sub1, sub2, relationship):
        self.relationships.update_one({'title':sub1}, {'$set':{sub2:relationship}})
    def returnRelation(self, sub1):
        result = self.relationships.find_one({'title':sub1})
        counter = 0
        for x in result:
            try:
                print(x)
                print(result[x])
            except:
                pass
shit = Database()
shit.returnRelation("Cat")
