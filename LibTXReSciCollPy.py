from LibTXReSciCollPy import RSCRockCoreSample
from LibTXReSciCollPy import RSCSample
from LibTXReSciCollPy import RSCSamples
from datetime import datetime

#Use the rock core sample
s = RSCSample()

s.localID = "11111"
s.title = "Test Title"
s.alternateTitle = "Test Alternate title"
s.abstract = "Test abstract"
s.coordinatesLatitude = 32.0
s.coordinatesLongitude = -95.0
s.publicationDate = datetime.now
s.alternateGeometry = "Test alternate geometry"
s.onlineResource = "https://www.beg.utexas.edu"
s.browseGraphic = "https://www.beg.utexas.edu"
s.date = datetime(2020, 1, 30)
s.verticalExtentBottom=1200
s.verticalExtentTop=800
s.verticalExtentUnit="ft"
s.IGSN = "00000001"
s.parentIgsn = "00000000"
s.relIgsn = "00000002"
s.relationType = "Beans"
s.largerWorkCitation="Larger work citation test value"

rss = RSCSamples()
rss.addSample(s)

csv = rss.toRSCCsvFile("testoutput.csv")

print(csv)

