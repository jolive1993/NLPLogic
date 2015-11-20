import json

class File:
    def __init__(self):
        self.file = open('relationships.json', 'r+')
        self.file.close()
    def update(self, dict):
        newDict = {}
        self.file = open('relationships.json', 'w')
        for x in dict:
            if x != "_id":
                newDict[x] = dict[x]
        json.dump(newDict, self.file)
        self.file.close()
    def updateSeconndLevel(self, dict):
        self.file = open ('secondrelations.json', 'w')
        json.dump(dict, self.file)
        self.file.close()