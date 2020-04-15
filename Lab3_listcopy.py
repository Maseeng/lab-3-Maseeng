# -*- coding: cp1252 -*-
"""Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information."""

import arcpy
from arcpy import env
env.workspace = "C:\Users\MMasitha\Downloads\Lab_3_Exploring_Spatial_Data (1)\Lab_3_Exploring_Spatial_Data"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    arcpy.CopyFeatures_management (fc, "/Results/" + fc)

import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:\Users\MMasitha\Downloads\Lab_3_Exploring_Spatial_Data (1)\Lab_3_Exploring_Spatial_Data"
arcpy.CreateFileGDB_management("C:\Users\MMasitha\Downloads\Lab_3_Exploring_Spatial_Data (1)\Lab_3_Exploring_Spatial_Data\Results", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management (fc,
"…/Lab_3_Exploring_Spatial_Data/Results/NM.gdb/" + fcdesc.basename)
