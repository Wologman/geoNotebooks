import os, sys
#from dotenv import load_dotenv


#CURRENTLY THE WAY TO SET THIS TEMPORARILY FIRST IS    export $LD_LIBRARY_PATH=/usr/lib    
# in the terminal BEFORE RUNNING THE CODE.  But it still doesn't fix the import problems below

ld_library_path = os.environ.get('LD_LIBRARY_PATH', '')

# Print the value
print(f'LD_LIBRARY_PATH: {ld_library_path}')


#This is isn't the Pythonic way, and it doesn't help our editor recognise the extra packages for syntax assistance
#The VSCode way to do this is to create a settings.json for the editing with the extra paths
#and also a launch.json to launch the script uising for the extra paths.  Both sit under the project workspace for transparency.
#PyCharm and probably Spyder would directly recognise the .env and add the relevant paths, so best to include a .env file too.

#load_dotenv()

#print('PYTHONPATH:', os.environ['PYTHONPATH'])




#extra_paths = ['/usr/share/qgis/python/plugins/','/usr/share/qgis/python/', '/usr/lib/python3/dist-packages/']



#This is from sys.path inside qgis console:
extra_paths = [#'usr/share',
               '/usr/share/qgis/python', 
               '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python', 
               '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python/plugins', 
               '/usr/share/qgis/python/plugins', 
               #'/usr/lib/python310.zip', ModuleNotFoundError: No module named 'qgis._gui'
               '/usr/lib/python3.10',
               '/usr/lib/python3/dist-packages', 
               '/home/olly/.local/share/QGIS/QGIS3/profiles/default/python']

#print(sys.executable)  in qgis console I get:    '/usr/bin/python3'    The imports work as expected if I switch from my coda enironment to this interpreter.

#print('PYTHONPATH:', os.environ['PYTHONPATH'])
#for path in os.environ['PYTHONPATH'].split(':'):    #not sure why this doesn't work

#This approach works to set sys.path,  not sure why the other one doesn't yet.  Revisit this later
for path in extra_paths:
    if path not in sys.path:
        sys.path.append(path)
        print(f'Appending {path} to sys.path')
print('sys.path:', sys.path)

import qgis                 #Only works with the same interpreter as qgis its self.
from qgis.gui import *      #ModuleNotFoundError: No module named 'qgis._gui'   when using the interpreter from Conda
from qgis.core import *
from qgis.utils import plugins
from qgis.analysis import QgsNativeAlgorithms 
from PyQt5.QtCore import *
 

QgsApplication.setPrefixPath('/usr', True)
app = QgsApplication([], False)
#app.initQgis()                #something is wrong
#import processing             #something is wrong

   

# ImportError: libgsl.so.25: cannot open shared object file: No such file or directory
# Goes wrong from here,  likely connected to this comment from here 
# http://geospatialdesktop.com/2009/02/creating_a_standalone_gis_application_1/
# "If there are any errors you may have to set the path to the QGIS libraries using the LD_LIBRARY_PATH on OS X and Linux"
# Also discussed in the developer cookbook:
# https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#running-custom-applications    #This gives the explanation, but the solution doesn't work.
# https://subscription.packtpub.com/book/programming/9781783984985/1/ch01lvl1sec10/installing-qgis-for-development    #Same advice on dynamic links.
# so I think I'm onto something here  need to keep digging.


#The current problem seems to be that the Conda qgis version points to the wrong things, hence even with the right paths setup, I get this libgsl.so.25  not found error
#The goal here is to use all the qgis libraries from the installed api,  plus other stuff from Conda.  
# ideally also use the interpreter from Conda?  This shouldn't really matter if it is the same version.  Maybe better to use the QGIS default interpreter.



'''
#from qgis import processing  #This works but doesn't seem to load the module I'm looking for
#import processing  #This doesn't
#from processing.core import Processing  #This doesn't
#from processing.core.Processing import Processing
#Processing.initialize()







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