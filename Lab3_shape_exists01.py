import arcpy
from arcpy import env
env.workspace = "C:\Users\MMasitha\Downloads\Lab_3_Exploring_Spatial_Data (1)\Lab_3_Exploring_Spatial_Data"
shape_exists = arcpy.Exists("cities.shp")
print (shape_exists)
