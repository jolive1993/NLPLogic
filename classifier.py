from textblob import TextBlob
class Classify:
    def __init__(self):
        train = []
    def comparison(self, sub1, sub2):
        sharedTotal = 0
        sub1Total = 0
        sub1Counts = sub1.np_counts
        for np in sub1Counts:
            sub1Total += sub1Counts[np]
        sub2Total = 0
        sub2Counts = sub2.np_counts
        for np in sub2Counts:
            sub2Total += sub2Counts[np]
        for x in sub1Counts:
            for y in sub2Counts:
                if x == y:
                    sharedTotal += (sub1Counts[x] + sub2Counts[y])
        relationship = sharedTotal / (sub1Total + sub2Total)
        return relationship
        