import os, sys
from dotenv import load_dotenv

#This is isn't the Pythonic way, and it doesn't help our editor recognise the extra packages for syntax assistance
#The VSCode way to do this is to create a settings.json for the editing with the extra paths
#and also a launch.json to launch the script uising for the extra paths.  Both sit under the project workspace for transparency.
#PyCharm and probably Spyder would directly recognise the .env and add the relevant paths, so best to include a .env file too.

load_dotenv()

print('PYTHONPATH:', os.environ['PYTHONPATH'])




#extra_paths = ['/usr/share/qgis/python/plugins/','/usr/share/qgis/python/', '/usr/lib/python3/dist-packages/']
#This is from sys.path inside qgis console:
extra_paths = ['/usr/share/qgis/python', 
               '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python', 
               '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python/plugins', 
               '/usr/share/qgis/python/plugins', 
               #'/usr/lib/python310.zip', 
               #'/usr/lib/python3.10', 
               '/usr/lib/python3.10/lib-dynload', 
               '/usr/local/lib/python3.10/dist-packages', 
               '/usr/lib/python3/dist-packages', 
               '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python']


#print('PYTHONPATH:', os.environ['PYTHONPATH'])
#for path in os.environ['PYTHONPATH'].split(':'):    #not sure why this doesn't work

#This approach works to set sys.path,  not sure why the other one doesn't yet.  Revisit this later
for path in extra_paths:
    if path not in sys.path:
        sys.path.append(path)
        print(f'Appending {path} to sys.path')
print('sys.path:', sys.path)

import qgis   #note- this one comes from the conda environment, not from the sys paths
from qgis.gui import *
from qgis.core import *
from qgis.utils import plugins
from PyQt5.QtCore import *
 

QgsApplication.setPrefixPath('/usr', True)
app = QgsApplication([], False)
app.initQgis()

#import processing             #something is wrong
import qgis.analysis           #also not there     

# ImportError: libgsl.so.25: cannot open shared object file: No such file or directory
# Goes wrong from here,  likely connected to this comment from here 
# http://geospatialdesktop.com/2009/02/creating_a_standalone_gis_application_1/
# "If there are any errors you may have to set the path to the QGIS libraries using the LD_LIBRARY_PATH on OS X and Linux"
# Also discussed in the developer cookbook:
# https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#running-custom-applications
# so I think I'm onto something here  need to keep digging.


'''
#from qgis import processing  #This works but doesn't seem to load the module I'm looking for
#import processing  #This doesn't
#from processing.core import Processing  #This doesn't
#Processing.initialize()


#from qgis import analysis   #doesn't work
#from qgis.analysis import QgsNativeAlgorithms  #won't wrok unless qgis.analysis is sorted





#QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
#for alg in QgsApplication.processingRegistry().algorithms():
#        print(alg.id(), "--->", alg.displayName())

### Do some processing  ###
#input_layer = QgsVectorLayer('/path/to/your/shapefile.shp', 'input_layer', 'ogr')
#buffer_output = '/path/to/output/buffer.shp'

#processing.run("native:buffer", {
#    'INPUT': input_layer,
#    'DISTANCE': 100,
#    'OUTPUT': buffer_output
#})

#app.exitQgis()
#app.exit()
'''