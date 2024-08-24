# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:  ENTerritorio Data Qualyty and Quality Assurance
#
# Author:      migue
#
# Created:     03-06-2019
# Copyright:   (c) miguel Blanco 2019
# Licence:     <your licence>

#  Searach for all empties featureclass in a gdb
#-------------------------------------------------------------------------------

#CODE run PERFECTLY
import arcpy, csv, os

#Parameter to put on ArcToolbox POTM
arcpy.env.workspace = arcpy.GetParameterAsText(0)

# write a *.csv file. it is necesary to put "file"+ "output" in parameters
archivo = arcpy.GetParameterAsText(1)

#Change the below line to run over each gdb that you need to know emty layer nam
##arcpy.env.workspace = r"D:\1_ENTerritorio\0_PAQUETE_SIG_DNP\ESQUEMAS GDB\MODELO GEODATABASE\POT_RURAL_CHIA2.gdb"

datasetList = arcpy.ListDatasets("*", "Feature")
for dataset in datasetList:
    arcpy.AddMessage ("Dataset_= " + (dataset))
    fcList = arcpy.ListFeatureClasses("*","",dataset)
    datas = ("Dataset_= " + (dataset))
##    fcList.sort()
    for fc in fcList:
        if arcpy.GetCount_management(fc)[0] == "0":
            arcpy.AddMessage (fc)
            # List to write in the repport
            row = [datas, fc]
            #Create a csv file with the repport.
            with open(archivo, "a") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow((row))
            csvFile.close()
# open the file (in my pc I have Excel asociate with *.csv File
os.startfile(archivo)