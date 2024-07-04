from LibTXReSciCollPy import RSCSampleFromOGWell

class RSCOGWellCorePhotos(RSCSampleFromOGWell):
    
    """This represents a group of photos of an oil or gas well-derived core sample.  Note that this is intended to represent more than one file, as the Bureau of Economic Geology's catalog addresses them by the sample they come from."""

    def __init__(self):
        super().__init__()

        self.dataType = "Photographs"
        self.sampleTypeDesc = "Core photos";
        
    @property
    def freeImageCount(self):
        return self.__freeImageCount

    @freeImageCount.setter
    def freeImageCount(self, val):
        self.__freeImageCount = val

    @property
    def paidImageCount(self):
        return self.__paidImageCount

    @paidImageCount.setter
    def paidImageCount(self, val):
        self.__paidImageCount = val


    def composeAbstractElements(self):
        """
        Composes the abstract elements for this core photo group.  Also an example of how to put elements before the superclass's elements.
        """
        ret =[]

        ret.insert(0, "This is a collection of core photos containing the following: ")

        self.addAbstractElement(self.freeImageCount, "Free Images", ret)
        self.addAbstractElement(self.paidImageCount, "Paid Images", ret)
        ret.append("") #An empty line

        ret2 =  super().composeAbstractElements()
        
        return ret + ret2