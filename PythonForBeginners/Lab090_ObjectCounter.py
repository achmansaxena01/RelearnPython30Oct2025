# static field and methods
class ObjectCounter:

    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)

O1 = ObjectCounter()
O2 = ObjectCounter()
ObjectCounter.displayCount()