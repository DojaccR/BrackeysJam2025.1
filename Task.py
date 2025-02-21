class Task:
    def __init__(self, location):
        self.location = location
        self.complete = False
        pass

    def isComplete(self):
        if self.complete == True:
            return True
        else:
            return False

    def getLocation(self):
        return self.location

    def run(self):
        pass
