
class RSCSample(object):
    pass
    """This represents a strict interpretation of the NDC 'sample' entry - a member of a collection."""
    
    #initializer
    def __init__(self):

        self.__localID = None
        self.__coordinatesLatitude = None
        self.__coordinatesLongitude = None
        self.__title = None
        self.__alternateTitle = None
        self.__abstract = None
        self.__dataType = None
        self.__publicationDate = None
        self.__collectionID = None
        self.alternateGeometry = None
        self.onlineResource = None
        self.browseGraphic = None
        self.date = None
        self.verticalExtent = None

        self.__verticalExtentTop = None
        self.__verticalExtentBottom = None
        self.__verticalExtentUnit = None
        self.__igsn = None
        self.__parentIgsn = None
        self.__relIgsn = None
        self.__relationType = None
        self.__largerWorkCitation = None

        self.internalReferenceNumber1 = None
        self.internalReferenceNumber2 = None
        self.internalReferenceNumber1Description = None
        self.internalReferenceNumber2Description = None

        self.supplementalInformation = None
        self.repositoryPhoneNumber = None
        self.repositoryEmailAddress = None
        self.repositoryName = None
        self.repositoryPhysicalAddress = None
        self.repositoryMailingAddress = None
        self.supplementalInformationAdditional = None

        self.abstractMore = None
        #We don't mess with the convenience methods here.

        return super().__init__()

    #Local ID
    @property
    def localID(self):
        return self.__localID

    @localID.setter
    def localID(self, val):
        self.__localID = str(val)

    #title property
    @property
    def title(self):

        ret = None

        #If no title is set, see if we can compose one.
        if self.__title == None or self.__title == "":
            ret = self.composeTitle()
        else:
            ret = self.__title

        return ret

    @title.setter
    def title(self, val):
        self.__title = val
    
    #Abstract property
    @property
    def abstract(self):
        """ The abstract  """
        ret = None
        if(self.__abstract != None):
            ret = self.__abstract
        else:
            ret = self.composeAbstract()

        return ret

    @abstract.setter
    def abstract(self, val):
        self.__abstract = val
    
    #Data type property
    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, val):
        self.__dataType = val

    #Supplemental information property
    @property
    def supplementalInformation(self):
        ret = None

        if self.__supplementalInformation != None:
            ret = self.__supplementalInformation
        else:
            ret = self.composeSupplementalInformation()

        return ret

    @supplementalInformation.setter
    def supplementalInformation(self, val):
        self.__supplementalInformation = val
    
    #The coordinates property - note no setter.  Set this with the discrete latitude and longitude
    @property
    def coordinates(self):
        ret = None

        if(self.__coordinatesLatitude != None and self.__coordinatesLongitude != None):
            ret = str(self.__coordinatesLongitude) + "," + str(self.__coordinatesLatitude)

        return ret

    #Dataset reference date
    @property
    def publicationDate(self):
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, val):
        self.__publicationDate = val

    #Optional Properties - we can get away with not filling these in, but we should at least try.
    
    #Collection ID property.
    @property
    def collectionID(self):
        return self.__collectionID

    @collectionID.setter
    def collectionID(self, val):
        self.__collectionID = val

    #Alternate title property
    @property
    def alternateTitle(self):
        
        ret = None

        #If no title is set, see if we can compose one.
        if self.__alternateTitle == None or self.__alternateTitle == "":
            ret = self.composeAlternateTitle()
        else:
            ret = self.__alternateTitle

        return ret

    @alternateTitle.setter
    def alternateTitle(self, val):
        self.__alternateTitle = val

    #alternate geometry
    @property
    def alternateGeometry(self):
        return self.__alternateGeometry

    @alternateGeometry.setter
    def alternateGeometry(self, val):
        self.__alternateGeometry = val

    #online resource
    @property
    def onlineResource(self):
        return self.__onlineResource

    @onlineResource.setter
    def onlineResource(self, val):
        self.__onlineResource = val

    #browse graphic
    @property
    def browseGraphic(self):
        return self.__browseGraphic

    @browseGraphic.setter
    def browseGraphic(self, val):
        self.__browseGraphic = val

    #date
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, val):
        self.__date = val

    #vertical extent
    @property
    def verticalExtent(self):
        return self.__verticalExtent

    @verticalExtent.setter
    def verticalExtent(self, val):
        self.__verticalExtent = val

    @property
    def parentIgsn(self):
        return self.__parentIgsn

    @parentIgsn.setter
    def parentIgsn(self, val):
        self.__parentIgsn = val

    @property
    def relIgsn(self):
        return self.__relIgsn
    
    @relIgsn.setter
    def relIgsn(self, val):
        self.__relIgsn = val

    @property
    def relationType(self):
        return self.__relationType

    @relationType.setter
    def relationType(self, val):
        self.__relationType = val

    @property
    def largerWorkCitation(self):
        return self.__largerWorkCitation

    @largerWorkCitation.setter
    def largerWorkCitation(self, val):
        self.__largerWorkCitation = val

    #Convenience properties - These are not strictly part of the NDC data model, but they make this whole business more convenient by breaking all the compound properties out into atomic ones.

    #coordinates longitude
    @property
    def coordinatesLongitude(self): 
        return self.__coordinatesLongitude
    
    @coordinatesLongitude.setter
    def coordinatesLongitude(self, val: float):
        self.__coordinatesLongitude = val

    #coordinates latitude
    @property
    def coordinatesLatitude(self):
        return self.__coordinatesLatitude

    @coordinatesLatitude.setter
    def coordinatesLatitude(self, val: float):
        self.__coordinatesLatitude = val

    #The unit component of our vertical extent 
    @property
    def verticalExtentUnit(self):
        return self.__verticalExtentUnit

    @verticalExtentUnit.setter
    def verticalExtentUnit(self, val: str):
        if val != None and isinstance(val, str) == False:
            raise TypeError
        elif val != None and val != 'm' and val != 'ft':
            raise ValueError(True)
        else:
            self.__verticalExtentUnit = val
            self.__updateVerticalExtent()

    #The top component of our vertical extent.  Because this is a depth (positive downward), it must be a smaller number than the bottom value
    @property
    def verticalExtentTop(self):
        return self.__verticalExtentTop

    @verticalExtentTop.setter
    def verticalExtentTop(self, val: float):
        
        if val != None and isinstance(val, float) == False and isinstance(val, int) == False:
            raise TypeError
            
        self.__verticalExtentTop = val

        self.__updateVerticalExtent()
    
    #The bottom component of our vertical extent.  Because this is a depth (positive downward), it must be numerically equal to or larger than the top value
    @property
    def verticalExtentBottom(self):
        
        return self.__verticalExtentBottom

    @verticalExtentBottom.setter
    def verticalExtentBottom(self, val: float):

        if val != None and isinstance(val, float) == False and isinstance(val, int) == False:
            raise TypeError
            
        self.__verticalExtentBottom = float(val)

        self.__updateVerticalExtent()

    #calculates a string value for our vertical extent by combining the unit, top and bottom parameters.
    def __updateVerticalExtent(self):
        if self.verticalExtentUnit != None and self.verticalExtentTop != None and self.verticalExtentBottom != None:
            val = self.verticalExtentUnit  +','+ str(self.verticalExtentBottom) + ',' + str(self.verticalExtentTop)
            self.verticalExtent = val
        else:
            self.verticalExtent = None

    #The abstract more property.  This is some extra text that can be added to the abstract property 
    @property
    def abstractMore(self):
        return self.__abstractMore

    @abstractMore.setter
    def abstractMore(self, val):
        self.__abstractMore = val

    #The internal reference number 
    @property
    def internalReferenceNumber1(self):
        return self.__internalReferenceNumber1

    @internalReferenceNumber1.setter
    def internalReferenceNumber1(self, val):
        self.__internalReferenceNumber1 = val

    #A second internal reference number.
    @property
    def internalReferenceNumber2(self):
        return self.__internalReferenceNumber2

    @internalReferenceNumber2.setter
    def internalReferenceNumber2(self, val):
        self.__internalReferenceNumber2 = val
    
    #The label to be shown on the first internal reference number.  In BEG's case, this is the database PK (called 'Sample ID')
    @property
    def internalReferenceNumber1Description(self):
        return self.__internalReferenceNumber1Description

    @internalReferenceNumber1Description.setter
    def internalReferenceNumber1Description(self, val):
        self.__internalReferenceNumber1Description = val

    #The label shown on the second internal reference number.  In BEG's case, this is the accession number
    @property
    def internalReferenceNumber2Description(self):
        return self.__internalReferenceNumber2Description

    @internalReferenceNumber2Description.setter
    def internalReferenceNumber2Description(self, val):
        self.__internalReferenceNumber2Description = val

    @property
    def igsn(self):
        return self.__igsn

    @igsn.setter
    def igsn(self, var):
        self.__igsn = var

    @property
    def repositoryName(self):
        return self.__repositoryName

    @repositoryName.setter
    def repositoryName(self, val):
        self.__repositoryName = val

    @property
    def repositoryPhoneNumber(self):
        return self.__repositoryPhoneNumber

    @repositoryPhoneNumber.setter
    def repositoryPhoneNumber(self, var):
        self.__repositoryPhoneNumber = var

    @property
    def repositoryPhysicalAddress(self):
        return self.__repositoryPhysicalAddress

    @repositoryPhysicalAddress.setter
    def repositoryPhysicalAddress(self, var):
        self.__repositoryPhysicalAddress = var

    @property
    def repositoryMailingAddress(self):
        return self.__repositoryMailingAddress

    @repositoryMailingAddress.setter
    def repositoryMailingAddress(self, var):
        self.__repositoryMailingAddress = var
    
    @property
    def repositoryEmailAddress(self):
        return self.__repositoryEmailAddress

    @repositoryEmailAddress.setter
    def repositoryEmailAddress(self, val):
        self.__repositoryEmailAddress = val

    @property
    def supplementalInformationAdditional(self):
        ret = self.__supplementalInformationAdditional

    @supplementalInformationAdditional.setter
    def supplementalInformationAdditional(self, val):
        self.__supplementalInformationAdditional = val

    def addSupplementalInformationElement(self, element, label, list):
        """ Adds an element and label to the set of items to be included in our abstract text if the value is not null. """
        if element != None and label != None:
            list.append(label + ": " + element)

    def composeSupplementalInformationElements(self):
        ret = []

        self.addSupplementalInformationElement(self.repositoryName, "Repository Name", ret)
        self.addSupplementalInformationElement(self.repositoryEmailAddress, "Repository Email Address", ret)
        self.addSupplementalInformationElement(self.repositoryPhoneNumber, "Repository Phone Number", ret)
        self.addSupplementalInformationElement(self.repositoryMailingAddress, "Repository Mailing Address", ret)
        self.addSupplementalInformationElement(self.repositoryPhysicalAddress, "Repository Physical Address", ret)
        self.addSupplementalInformationElement(self.supplementalInformationAdditional, "Additional Information", ret)
        
        return ret

    def composeSupplementalInformation(self):
        ret = ""

        elementList = self.composeSupplementalInformationElements()

        ret = "\r\n".join(elementList)

        return ret

    def addAbstractElement(self, element, label, list, atBeginning = False):
        """ Adds an element and label to the set of items to be included in our abstract text if the value is not null. """
        if element != None and label != None:

            content = "{0}: {1}".format(label, element)

            if atBeginning == False:
                list.append(content)
            else:
                list.insert(0, content)

    def composeAbstractElements(self):
        """ Returns a list of strings, each representing a line in the final abstract value """
        ret = []

        refNum1Desc = "Reference 1"
        if self.internalReferenceNumber1Description != None:
            refNum1Desc = self.internalReferenceNumber1Description

        refNum2Desc = "Reference 2"
        if self.internalReferenceNumber2Description != None:
            refNum2Desc = self.internalReferenceNumber2Description

        self.addAbstractElement(self.internalReferenceNumber1, refNum1Desc, ret)
        self.addAbstractElement(self.internalReferenceNumber2, refNum2Desc, ret)
        self.addAbstractElement(self.igsn, "IGSN", ret)
        self.addAbstractElement(self.abstractMore, "More information: ", ret)
        
        return ret

    #Composes the abstract text from our custom instance variables
    def composeAbstract(self):
        ret = ""

        #Build the list 
        elementList = self.composeAbstractElements()

        ret = "\r\n".join(elementList)

        return ret

    def validateForCsv(self):
        
        #Make sure we really have a title.
        if(self.title == None or self.title == ""):
            raise ValueError("Title is required and cannot be empty.")

        #Make sure we really have an abstract value
        if(self.abstract == None or self.abstract == ""):
            raise ValueError("Abstract is required and cannot be empty.")

        #
        #if(self.dataType == None or self.dataType == ""):
        #    raise ValueError("Data type is required and cannot be empty.")

        #validate the supplemental information field.  Mainly, it needs to not be empty.
        #if(self.supplementalInformation == None or self.supplementalInformation == ""):
        #    raise ValueError("Supplemental information is required and cannot be empty.  To fix this, set the repository fields.")
        
        #validate the coordinates
        if(self.coordinates == None or self.coordinates == ""):
            raise ValueError("Coordinates are required and cannot be empty.")

        #validate dataset reference data field
        if(self.publicationDate == None or self.publicationDate == ""):
            raise ValueError("Dataset reference date is required and cannot be empty.")

    
    def composeTitle(self):
        """
        Composes a title from the object's properties. Default implementation returns null.  Override this if you need it.
        """

        ret = None
        return ret

    def composeAlternateTitle(self):
        """
        Composes a title from the object's properties. Default implementation returns null.  Override this if you need it.
        """

        ret = None
        return ret

        

    def toRSCCsvRowArray(self):

        #Validate and make sure we have what we have all the required fields.
        self.validateForCsv()

        parts = []

        parts.append(self.localID)
        parts.append(self.title)
        parts.append(self.alternateTitle)
        parts.append(self.abstract)
        parts.append(str(self.coordinatesLongitude))
        parts.append(str(self.coordinatesLatitude))

        if(self.publicationDate != None):
            parts.append(str(self.publicationDate.strftime("%Y%m%d")))
        else:
            parts.append(None)

        parts.append(self.alternateGeometry)
        parts.append(self.onlineResource)
        parts.append(self.browseGraphic)

        if(self.date != None):
            parts.append(str(self.date.strftime("%Y%m%d")))
        else:
            parts.append(None)

        parts.append(self.verticalExtent)
        parts.append(self.igsn)
        parts.append(self.parentIgsn)
        parts.append(self.relIgsn)
        parts.append(self.relationType)
        parts.append(self.largerWorkCitation)

        return parts

        


