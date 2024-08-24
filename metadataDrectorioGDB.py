# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:  ENTerritorio Data Qualyty and Quality Assurance
#
# Author:      migue
#
# Created:     03-06-2019
# Copyright:   (c) miguel Blanco 2019
# Licence:     <your licence>

#  Regresa el nombre de dataset, layesr y el sistema de referencia y metadata
#-------------------------------------------------------------------------------
# Es necesario instalar el modulo arcpy_metadata en python 2.7

#CODE run PERFECTLY


import arcpy, os, csv
import arcpy_metadata as md


#Change the below line to run over each gdb that you need to know emty layer names
##arcpy.env.workspace = r"D:\1_ENTerritorio\Z2_INYPSA\PBOT_RURAL_SAMPUES_70670.gdb"

arcpy.env.workspace = arcpy.GetParameterAsText(0)

# write a *.csv file. it is necesary to put "output" in parameters
archivo = arcpy.GetParameterAsText(1)

# Boucle pour chercher les couches, donc on a besoin
datasetList = arcpy.ListDatasets("*", "Feature")

for dataset in datasetList:
    arcpy.AddMessage ("Dataset_= " + (dataset))
    datas = ("Dataset_= " + (dataset))
    fcList = arcpy.ListFeatureClasses("*","",dataset)
    fcList.sort()
    for fc in fcList:
        if arcpy.GetCount_management(fc)[0] != "0": #si quiero buscar solamente las que tengan contenido
            arcpy.AddMessage ("Capa_=" + (fc))
    ##        if fc.supports("dataSource"): # SI SOPORTA DATASURCES
    ##            print fc.dataSource
            arcpy.AddMessage ("Sistema_de_Referencia_= " + (arcpy.Describe(fc).spatialReference.Name))
    ##        print arcpy.Describe(fc).spatialReference.Code
            metadata =md.MetadataEditor(fc)
            arcpy.AddMessage ("Metadata_Titulo=_"+(metadata.title))
            titulo =("Metadata_Titulo=_"+(metadata.title))
            arcpy.AddMessage ("Metadata_Resumen=_ " + (metadata.abstract))
            resumen = ("Metadata_Resumen=_ " + (metadata.abstract))
            arcpy.AddMessage ("Metadata_Resumen_Extendido=_ " + (metadata.purpose))
            resumenExtendido =("Metadata_Resumen_Extendido=_ " + (metadata.purpose))
            arcpy.AddMessage ("Metadata_Tags=_ " + str(metadata.tags))
            tags =("Metadata_Tags=_ " + str(metadata.tags))
            arcpy.AddMessage ("Metadata_Escala_Minima=_ " + str(metadata.min_scale))
            escMinima =("Metadata_Escala_Minima=_ " + str(metadata.min_scale))
            arcpy.AddMessage ("Metadata_Escala_Maxima=_ " + str(metadata.max_scale))
            escMaxima =("Metadata_Escala_Maxima=_ " + str(metadata.max_scale))
            arcpy.AddMessage ("Metadata_Creditos=_ " + (metadata.credits))
            creditos =("Metadata_Creditos=_ " + (metadata.credits))
            arcpy.AddMessage ("Metadata_Limitaciones_De_Uso=_ " + (metadata.limitation))
            limUso =("Metadata_Limitaciones_De_Uso=_ " + (metadata.limitation))
            arcpy.AddMessage ("Metadata_Fecha_Actualizacion=_ " + str(metadata.last_update))
            fechaActualizacion =("Metadata_Fecha_Actualizacion=_ " + str(metadata.last_update))
            arcpy.AddMessage ("Metadata_Extension=_ " + (metadata.extent_description))
            extension =("Metadata_Extension=_ " + (metadata.extent_description))

# List de tous les proprietés a mettre dans le rapport
            row = [datas, titulo,resumen,resumenExtendido,tags,escMinima,escMaxima,creditos,limUso,fechaActualizacion,extension]
            #Create a csv file with the repport.
            with open(archivo, "a") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow((row))
            csvFile.close()
# open the file (in my pc I have Excel asociate with *.csv File
os.startfile(archivo)

arcpy.AddMessage("Termia con exito")
