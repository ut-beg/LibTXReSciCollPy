import LibTXReSciCollPy as rsc

from datetime import datetime
import pandas as pd

sourceFilePath = "C:\\Users\\averetta\\Documents\\crc data\\nggdpp_update 2023\\in\\core_photos_export.csv"
outFilePath = "C:\\Users\\averetta\\Documents\\crc data\\nggdpp_update 2023\\out\\core_photos.csv"

def composeTitle(row):
    ret = None

    if row["ApiNumber"] != None:
        ret = "Core photos from API Number " + str(row["ApiNumber"])
    elif row["LeaseName"] != None and row["WellNumber"] != None and row["CountyName"] != None:
        ret = "Core photos from well: " + row["LeaseName"]

    return ret

def composeAlternateTitle(row):
    ret = None



    return ret

df = pd.read_csv(sourceFilePath)

rss = rsc.RSCSamples()

for index, row in df.iterrows():
    s = rsc.RSCOGWellCorePhotos()
    
    s.localID = row["LogId"]

    s.apiNumber = row["ApiNumber"]
    s.leaseName = row["LeaseName"]
    s.operatorName = row["OperatorName"]
    s.wellNumber = row["WellNumber"]
    s.stateName = row["StateName"]
    s.countyName = row["CountyName"]
    s.countryName = row["CountryName"]
    
    s.coordinatesLatitude = row["SurfaceLatitude"]
    s.coordinatesLongitude = row["SurfaceLongitude"]

    s.verticalExtentTop = row["TopDepth"]
    s.verticalExtentBottom = row["BottomDepth"]
    s.verticalExtentUnits="Ft"

    s.freeImageCount = row["FreeScanCount"]
    s.paidImageCount = row["PaidScanCount"]

    s.onlineResource = "https://coastal.beg.utexas.edu/continuum/#!/log/{0}".format(row["LogId"])
    s.publicationDate = datetime.now()

    rss.addSample(s)

rss.toRSCCsvFile(outFilePath)

"""


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
"""
