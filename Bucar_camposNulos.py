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
# Created:     07-31-2019
# Copyright:   (c) miguel Blanco 2019
# Licence:     <your licence>

#  Serach for Null value
# Buscar valores nulos en features
#-------------------------------------------------------------------------------

#CODE run PERFECTLY
import arcpy, arcpy.da, os, csv

#Change the below line to run over each gdb that you need to know emty layer names
##arcpy.env.workspace = r"D:\1_ENTerritorio\Z2_INYPSA\POT\P11\ARIGUANI\2019_07_10\REVISION_MB\POT_RURAL_ARIGUANI.gdb"

# Buscar la geodatabase.  buscar por workspace en el parametro

arcpy.env.workspace = arcpy.GetParameterAsText(0)

# write a *.csv file. it is necesary to put "output" in parameters
archivo = arcpy.GetParameterAsText(1)

# Loop throw dataset and layers
datasetList = arcpy.ListDatasets("*", "Feature")
for dataset in datasetList:
    arcpy.AddMessage ("Dataset_= " + (dataset))
    fcList = arcpy.ListFeatureClasses("*","",dataset)
    datas = ("Dataset_= " + (dataset))
    fcList.sort()
    for fc in fcList:
        #if arcpy.GetCount_management(fc)[0] == "0":
        arcpy.AddMessage (fc)
        sc = arcpy.da.SearchCursor(fc, "*")
        for row in sc:
            if None in row:
#               arcpy.AddMessage("Valor nulo encontrado en :" + fc.rsplit("\\",1)[1])
                arcpy.AddMessage (" En el feature class: " + fc + " No hay valor en la fila {0}".format(row[0]))
                rowss = [datas, "En Featureclass. ",fc, " No hay valor en la fila {0}".format(row[0])]
#  Write a report in *.csv format

                with open(archivo, "a") as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow((rowss))
                csvFile.close()
# open the file (in my pc I have Excel asociate with *.csv File
os.startfile(archivo)
