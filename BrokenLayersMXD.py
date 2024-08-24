# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      migue
#
# Created:     19-06-2019
# Copyright:   (c) migue 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Import necessary libraries
import arcpy, os,  csv


##path = (r"D:\1_ENTerritorio\Z2_INYPSA\POT\P11\ARIGUANI\2019_07_10\2. PROYECTOS DE MAPA")

path = arcpy.GetParameterAsText(0)

# write a *.csv file. it is necesary to put "output" in parameters
archivo = arcpy.GetParameterAsText(1)

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.mxd' in file:
            files.append(os.path.join(r, file))
            mxdf = file
            arcpy.AddMessage (mxdf)
            mxd_list = mxdf

for f in files:
    arcpy.AddMessage(f)
    mxdfile = (f)


    mxd = arcpy.mapping.MapDocument(f)

    #Get the file path from the MXD File
    mapPath = mxd.filePath

    #Get name of the full path
    fileName = os.path.basename(mapPath)

    #Get a list of all layers in the given MXD File
    layers = arcpy.mapping.ListLayers(mxd)


    #Identify all broken layers in  MXD File
    brknList = arcpy.mapping.ListBrokenDataSources(mxd)

    #Initiate a loop to run through each layer within the MXD File
    for layer in layers:
        #Check if support datassource.

        if layer.supports("dataSource"):
        #Determine if the layer is broken or not by comparing it to the list of broken layers
            if layer in brknList:
                broken = "Dataource_Roto"
            else:
                broken = "Datasource_Ok"

            #Compile a list of layer attributes.
            layerattributes = ["mxd= "+mxdfile,"capa= "+layer.longName, "ubicacion= "+layer.dataSource, "estado= "+broken]
            arcpy.AddMessage (layerattributes)


            #Create a csv file with the repport.
            with open(archivo, "a") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow((layerattributes))
            csvFile.close()

# open the file (in my pc I have Excel asociate with *.csv File
os.startfile(archivo)
