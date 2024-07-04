LibTXReSciCollPy is a Python library for generating the item-level metadata files required by the USGS "ReSciColl" scientific sample collection.  It contains a series of common item types with pre-configured fields, but these are meant primarily to be extended by the user to customize them for his or her particular situation.

Installation:
1.  Clone this repository
2.  Copy ./LibTXReSciCollPy to your project directory
3.  Import LibTXReSciCollPy in your Python script using the following
	import LibTXReSciCollPy as rsc

Usage:  For a full usage example, see TestConvertCorePhotoData.py.  This file contains a typical example of item-level records being exported to the ReSciColl from an existing data source.

A simpler example:

```
import LibTXReSciCollPy as rsc

#Path to our output file.
outFilePath = ".\\core_photos.csv"

#Create a samples object - This represents the collection
rss = rsc.RSCSamples()

#Create an item
s = rsc.RSCOGWellCorePhotos()
 
#Fill in the item's properties.
s.localID = "000001"

s.apiNumber = "42127000001"
s.leaseName = "Example Lease Name"
s.operatorName = "Bob's Oil Field Services"
s.wellNumber = "#1"
s.stateName = "Texas"
s.countyName = "Dimmit"
s.countryName = "USA"
    
s.coordinatesLatitude = 28.45554997499842
s.coordinatesLongitude = -99.75494921582204

s.verticalExtentTop = 5000
s.verticalExtentBottom = 10000
s.verticalExtentUnits="Ft"

s.freeImageCount = 1
s.paidImageCount = 0

s.onlineResource = "https://www.yourwebsitehere.com/path/to/this/sample/record/000001"
s.publicationDate = datetime.now()

rss.addSample(s)

rss.toRSCCsvFile(outFilePath)

```

