class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinician = []
    def addClinicalData(self, clinical):
        self.clinical = clinical




class Clinical:
    def __init__(self, compName, compValue):
        self.cmName = compName
        self.cmValue = compValue