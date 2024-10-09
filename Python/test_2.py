#To run from terminal, using the environment file:  export $(grep -v '^#' .env | xargs) && python3 test.py
import sys
print(sys.executable)
print(sys.version)

#There is something going wrong here.  We are apparently still using the Conda installed interpreter.  I was hoping to use the system one.  
#So this is the root cause of most trouble right now.  The key to this is to use the conda environment for the packages, but the QGIS interpreter.

from qgis.gui import *
from qgis.core import *
from qgis.utils import plugins
from qgis.analysis import QgsNativeAlgorithms 
from PyQt5.QtCore import *


#conda imports
#import seaborn  #something goes wrong with this
import piexif 
import geopandas as gpd


QgsApplication.setPrefixPath('/usr', True)
app = QgsApplication([], False)
#app.initQgis()     #If using conda environment This throws up:   HDF5-DIAG: Error detected in HDF5 (1.10.10) thread 1:


#app.exit()

