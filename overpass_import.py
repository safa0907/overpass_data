import os
from osgeo import gdal

import overpass
import geojson
import json
import tempfile
import subprocess
from osgeo import gdal
from geojson import Feature, FeatureCollection, dump, MultiPolygon, MultiLineString, LineString, GeometryCollection, Polygon,Point
maxsize:1073741824
#The bounding box coordinates as inputs
def coordinates_input():
	print("\nEnter latitude min (example:'47.003436')")
	lat_min = input()
	print("\nEnter longitude min (example:'15.370560')")
	long_min = input()
	print("\nEnter latitude max (example:'47.109626')")
	lat_max = input()
	print("\nEnter longitude max (example:'15.506172')")
	long_max = input()
	return([lat_min,long_min,lat_max,long_max])   

if __name__=='__main__':
    bbox_input=coordinates_input()
    api=overpass.API()
    q=bbox_input[0]+','+bbox_input[1]+','+bbox_input[2]+','+bbox_input[3]
    print (q)
    full_query='(relation["building"]('+q+');)'
    print(full_query)
    res=api.get(full_query,responseformat="geojson",verbosity="geom")
    print ('Query completed')
    print(res) 
    #Prepare Geometry
    
   
    #Export Geojson file
    #collection =geojson.FeatureCollection(res)
    with open("D:\Buildingst.geojson", 'w+') as f:
        geojson.dump(res, f)
    #Save to shp
    # args=['ogr2ogr','-f','esri shapefile','destination_data.shp', 'res.geojson']
    # subprocess.Popen(args)
    print ('Finished exporting Geojson file')
  