import scanner, classifier, uprint, filewrite
class Main:
    def __init__(self):
        database = scanner.Database()
        classy = classifier.Classify()
        file = filewrite.File()
        while True:
            sub1 = database.query()
            sub2 = database.query()
            exisiting = database.checkForRelationDB(sub1)
            if exisiting == True:
                relExisiting = database.checkForRelationSub2(sub1, sub2)
                if relExisiting == None:
                    blob1 = database.extractDataSet(sub1)
                    blob2 = database.extractDataSet(sub2)
                    relationship = classy.comparison(blob1, blob2)
                    print(relationship)
                    database.updateRelation(sub1, sub2, relationship)
                else:
                    print(relExisiting)
            else:
                blob1 = database.extractDataSet(sub1)
                blob2 = database.extractDataSet(sub2)
                relationship = classy.comparison(blob1, blob2)
                print(relationship)
                database.createNewRelation(sub1, sub2, relationship)
            dumper = database.returnRelation(sub1)
            file.update(dumper)
            dumper2 = database.returnSecondLevelRelations(dumper)
            file.updateSeconndLevel(dumper2)
        
Main()