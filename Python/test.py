#To run from terminal, using the environment file:  export $(grep -v '^#' .env | xargs) && python3 test.py
import sys
print(sys.executable)

import os, sys, time

'''
This is from sys.path inside qgis console:
    '/usr/share/qgis/python', 
    '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python', 
    '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python/plugins', 
    '/usr/share/qgis/python/plugins', 
    '/usr/lib/python3.10',
    '/usr/lib/python3/dist-packages', 
    '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python']

sys.path: /usr/bin/python3
sys.version: 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0]

To make this work:
    (1)  The extra pythonpaths need to be in our PYTHONPATH environment
    (2)  LD_LIBRARY_PATH from both QGIS and Conda need to be added to LD_LIBRARY_PATH
    (3)  We also need to add any extra paths for our Conda environment to PYTHONPATH, but without actually activating it
    (4)  The interpreter path for the environmnet must be the same one that QGIS uses
    (5)  Where there is overlap between conda and QGIS dependencies, they need and they involve C libraries they need to match. eg. libtiff
    (6)  Some mysterious unresolved problem with seaborn and ipyleaflet to do with lists.

To run in from terminal, go to the folder holding the scripts and the .env, then:
    source .env                             (Setus up all the paths and stores in environment variables)
    $PYTHON_INTERPRETER my_test_script.py   (Uses the interpreter from the .env to run the Python script)
    
To make this work in a fancy IDE:
    - The IDE settings need to recognise steps (1),(2),(3),(4) for linting, debugging, launch.  
    - In VSCode, those are all seperate things, and you can't just set the conda environment like normal, or it over-rides the .env
'''

from qgis.gui import *
from qgis.core import *
from qgis.utils import plugins
from qgis.analysis import QgsNativeAlgorithms 
from PyQt5.QtCore import *

#Conda imports
from osgeo import gdal
import cv2
import piexif 
import matplotlib
import pandas as pd
import geopandas as gpd
import sklearn as skl
import scipy
import shapely
import cartopy
import folium
from PIL import Image
import geoviews
import dotenv
import plotly.express as px
import arrow
import yaml
import fastparquet
import xmltodict
import rasterio    
import rasterstats
import contextily

#Troublemakers:
#import ipyleaflet   # In Ubuntu 24: TypeError: type 'List' is not subscriptable
#import seaborn      # In Ubuntu 24: TypeError: type 'List' is not subscriptable

#QGIS
QgsApplication.setPrefixPath('/usr', True)
app = QgsApplication([], False)
app.initQgis()                

project = QgsProject.instance()
project.read('testdata/01_project.qgs')
print(project.fileName())

#Do some actual data stuff
project.write()
project.write('testdata/my_new_qgis_project.qgs')

QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
for alg in QgsApplication.processingRegistry().algorithms():
       print(alg.id(), "--->", alg.displayName())

#Do something with the processing module
from processing.core.Processing import processing

shapefile_path = '/media/olly/Blue Samsung SSD/Documents/GIS/Notebooks/Data/kx-doc-huts-SHP/doc-huts.shp'
input_layer = QgsVectorLayer(shapefile_path, 'input_layer', 'ogr')  
buffer_output_path = '/home/olly/Desktop/temp_stuff/buffer.shp'

processing.run("native:buffer", {
    'INPUT': input_layer,
    'DISTANCE': 100,
    'OUTPUT': buffer_output_path
})

app.exit()


#Second Example. - Custom application
second_app = QgsApplication([], True)   #This is OK, but I wonder why it doesn't open the gui
second_app.initQgis()
#This is how to make a qgis 'custom application', with it's own custom gui. 
# https://docs.qgis.org/3.34/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-custom-applications 
#To do this we still need to construct the gui. But this could be really useful at DOC.
second_app.exit()

print('\033[1m' + '\033[94m' + "Awesome, success, God damn it Gump you're goddamn genius" + '\033[0m')