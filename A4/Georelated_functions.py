"""
This script helps to create an interactive map, set the BBox of the map ,download map tiles and mosaic them into a single GeoTIFF file.

"""
#import libraries
import os
import leafmap
from samgeo import SamGeo, tms_to_geotiff, get_basemaps

#This line defines a function which is used to create an interactive map
def baseMap():
  m = leafmap.Map(center=[29.676840, -95.369222], zoom=19)
  m.add_basemap("SATELLITE")

  return m

#Set the area of interest 
def getBBox():
  #if m.user_roi_bounds() is not None:
  #  bbox = m.user_roi_bounds()
  #else:
  bbox = [-95.3704, 29.6762, -95.368, 29.6775]
  return bbox

#Download maps tiles and mosaic them into a single GeoTIFF file
def getImage():
  image = "satellite.tif"
  return image

def tms_to_geotiff_function(image,bbox):
  tms_to_geotiff(output=image, bbox=bbox, zoom=20, source="Satellite", overwrite=True)

#Display the downloaded image on the map.
def diaplay(m):
  m.layers[-1].visible = False  # turn off the basemap
  m.add_raster(image, layer_name="Image")
  m
