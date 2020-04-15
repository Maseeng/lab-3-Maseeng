import arcpy
from arcpy import env
env.workspace = "C:\Users\MMasitha\Downloads\Lab_3_Exploring_Spatial_Data (1)\Lab_3_Exploring_Spatial_Data"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    arcpy.CopyFeatures_management (fc, "/Results/" + fc)

import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:\Users\MMasitha\Downloads\Lab_3_Exploring_Spatial_Data (1)\Lab_3_Exploring_Spatial_Data/"
fieldlist = arcpy.ListFields("cities.shp")
for field in fieldlist:
    print field.name + " " + field.type
