import arcpy
from arcpy import env
env.workspace = "Lab_3_Exploring_Spatial_Data/Data-Lab_3_Exploring_Spatial_Data/"
shape_exists = arcpy.Exists("cities.shp")
print shape_exists
