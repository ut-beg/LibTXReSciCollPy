from LibTXReSciCollPy import RSCSample
from io import StringIO
import csv

class RSCSamples(object):
    """description of class"""

    def __init__(self):
        self._samples = []

    @property
    def samples(self):
        return self._samples

    def createSample(self):
        sample = RSCSample.RSCSample()
        return sample

    def addSample(self, sample):
        if sample not in self.samples:
            self.samples.append(sample)

    def removeSample(self, sample):
        if sample in self.samples:
            self.samples.remove(sample)

    def toRSCCsvArray(self):
        ret = []

        for samp in self.samples:
            sampX = samp.toRSCCsvRowArray()
            ret.append(sampX)

        return ret

    def toRSCCsvFile(self, outFilePath):
        
        rows = self.toRSCCsvArray()
        
        with open(outFilePath, "w", newline="") as fh:

            csvwriter = csv.writer(fh)

            #Handle the header line
            headers = self.getHeaders()

            csvwriter.writerow(headers)

            csvwriter.writerows(rows)


    def toRSCCsvString(self):
        ret = ""

        xmlObj = self.toNDCXml()

        sio = StringIO("")

        xmlObj.export(sio, 0)

        ret = sio.getvalue()

        return ret

    def initWithJson(json): 
        for jsample in json["samples"]:
            sample = RSCSample()

            sample.initWithJson(jsample)

            self.addSample(sample)

    def getHeaders(self):
        ret = [
            'localID',
            'title',
            'alternateTitle',
            'abstract',
            'coordinateLon',
            'coordinateLat',
            'publicationDate',
            'alternateGeometry',
            'onlineResource',
            'browseGraphic',
            'date',
            'verticalExtent',
            'IGSN',
            'parentIGSN',
            'relIGSN',
            'relationType',
            'largerWorkCitation'
            ]

        return ret



