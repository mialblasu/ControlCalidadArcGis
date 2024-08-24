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
# Copyright:   (c) miguel Blanco 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Import necessary libraries
import arcpy, os, csv


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
    arcpy.AddMessage (" Layout Alto: " + str(mxd.pageSize.height) + "mm")
    layoutAlto =(" Layout Alto: " + str(mxd.pageSize.height) + "mm")
    arcpy.AddMessage (" Layout Ancho: " + str(mxd.pageSize.width) + "mm")
    layoutAncho = (" Layout Ancho: " + str(mxd.pageSize.width) + "mm")

    for df in arcpy.mapping.ListDataFrames(mxd):
        arcpy.AddMessage ("Nombre del DataFrame: " + df.name)
        dataframeNombre =("Nombre del DataFrame: " + df.name)
        arcpy.AddMessage ("Sistema de referencia: " + df.spatialReference.name)
        sistemaReferencia =("Sistema de referencia: " + df.spatialReference.name)
        arcpy.AddMessage ("Escala 1:" + str(df.scale))
        escala =("Escala 1:" + str(df.scale))

# List to write in the repport
        row = [mxdfile, layoutAlto,layoutAncho,dataframeNombre,sistemaReferencia,escala]

            #Create a csv file with the repport.
        with open(archivo, "a") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow((row))
        csvFile.close()
# open the file (in my pc I have Excel asociate with *.csv File
os.startfile(archivo)




