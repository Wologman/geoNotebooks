'''
This is from sys.path inside qgis console (Linux):
    '/usr/share/qgis/python', 
    '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python', 
    '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python/plugins', 
    '/usr/share/qgis/python/plugins', 
    '/usr/lib/python3.10',
    '/usr/lib/python3/dist-packages', 
    '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python']

sys.path: /usr/bin/python3
sys.version: 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0]

Paths from QGIS Python console in Windows:
    C:/PROGRA~1/QGIS33~1.2/apps/qgis/./python;
    C:/Users/ollyp/AppData/Roaming/QGIS/QGIS3\\profiles\\default/python;
    C:/Users/ollyp/AppData/Roaming/QGIS/QGIS3\\profiles\\default/python/plugins;
    C:/PROGRA~1/QGIS33~1.2/apps/qgis/./python/plugins;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\grass\\grass84\\etc\\python;
    C:\\Users\\ollyp\\Documents;
    C:\\Program Files\\QGIS 3.38.2\\bin\\python312.zip;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\Python312\\DLLs;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\Python312\\Lib;C:\\Program Files\\QGIS 3.38.2\\bin;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\Python312;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\Python312\\Lib\\site-packages;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\Python312\\Lib\\site-packages\\win32;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\Python312\\Lib\\site-packages\\win32\\lib;
    C:\\PROGRA~1\\QGIS33~1.2\\apps\\Python312\\Lib\\site-packages\\Pythonwin;
    
To make this work:
    (1)  The extra pythonpaths need to be in our PYTHONPATH environment variable
    (2)  Linux only: LD_LIBRARY_PATH from QGIS need to be added to LD_LIBRARY_PATH environment variable
    (3)  The relavent extra paths need adding to the settings in code-workspace, for python.envFile, 
                                                                                     python.analysis.extraPaths, 
                                                                                     python.autoComplete.extraPaths,
                                                                                     jupyter.notebookFileRoot
                                                                                     terminal.integrated.env.linux
                                                                                     terminal.integrated.env.windows 
                                                                                     launch: {envFile:path/to/env/file}   for debugging
'''
#Standard Python
import platform
from pathlib import Path
import joblib

# QGIS Imports
from qgis.analysis import QgsNativeAlgorithms
from qgis.core import QgsProject, QgsApplication, QgsVectorLayer
from qgis.gui import *
from qgis.utils import plugins
from PyQt5.QtCore import *

# Conda imports
import numpy as np
from osgeo import gdal
import matplotlib
import pandas as pd
import geopandas as gpd
import sklearn as skl
import scipy
import shapely
import cartopy
import folium
import piexif
import cv2
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

# Setup
class Colour:
    '''To colour print statements nicely'''
    S = '\033[1m' + '\033[94m'
    E = '\033[0m'

if platform.system() =='Windows':
    PROJECT_PATH = Path("F:/Documents/GIS/geoNotebooks")
    QGS_PREFIX = "C:/Program Files/QGIS 3.38.2"
else:
    PROJECT_PATH = Path("/media/olly/Blue_SSD/Documents/GIS/geoNotebooks")
    QGS_PREFIX = '/usr'

working = PROJECT_PATH / 'Working'
data = PROJECT_PATH / 'Data'
results = PROJECT_PATH / 'Results'

PROJECT_FILE_PATH = str(working / 'geo_test_project.qgz')
SHAPEFILE_PATH = str(data / 'kx-doc-huts-SHP/doc-huts.shp')
BUFFERED_PATH = str(working / 'buffer.shp')

print(Colour.S + f'The project root is located at {PROJECT_PATH}' + Colour.E)

QgsApplication.setPrefixPath(QGS_PREFIX, True)  #Needs to come before importing processing
from processing.core.Processing import processing


# Initialise
qgs = QgsApplication([], False)
qgs.initQgis()
project = QgsProject.instance()
project.read(PROJECT_FILE_PATH)
print(project.fileName())


# Verify with some processing
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
for idx, alg in enumerate(QgsApplication.processingRegistry().algorithms()):
    if idx <10:
        print(alg.id(), "--->", alg.displayName())

input_layer = QgsVectorLayer(SHAPEFILE_PATH, 'input_layer', 'ogr')

processing.run("native:buffer", {
    'INPUT': input_layer,
    'DISTANCE': 100,
    'OUTPUT': BUFFERED_PATH
})


#Close & release resources
project.write(PROJECT_FILE_PATH)
qgs.exit()

print(Colour.S + "God damn it Gump you're goddamn genius. \n"
      "That's the most outstanding answer I've ever heard.\n"
      "You must have a goddam IQ of 160.\n"
      "You are goddam gifted private Gump." + Colour.E)
