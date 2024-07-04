from LibTXReSciCollPy import RSCSampleFromOGWell

class RSCRockCoreSample(RSCSampleFromOGWell):
    """This is a type of sample that represents a core sample."""

    def __init__(self, *args, **kwargs): 
        super().__init__()
        self.dataType = "Rock Core"

        self.sampleTypeDesc = None
        self.formationName = None
        self.formationAge = None
        
    #The formation name property
    @property
    def formationName(self):
        return self.__formationName
    
    @formationName.setter
    def formationName(self, val):
        self.__formationName = val

    #The formation age property
    @property
    def formationAge(self):
        return self.__formationAge

    @formationAge.setter
    def formationAge(self, val):
        self.__formationAge = val

    def composeAbstractElements(self):
        ret = super().composeAbstractElements()

        self.addAbstractElement(self.sampleTypeDesc, "Sample Type", ret)
        self.addAbstractElement(self.formationName, "Formation", ret)
        self.addAbstractElement(self.formationAge, "Formation Age", ret)
        
        return ret

