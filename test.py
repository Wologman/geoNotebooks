import os, sys
#from dotenv import load_dotenv


#CURRENTLY THE WAY TO SET DYNAMIC LINKS TEMPORARILY FIRST IS    export $LD_LIBRARY_PATH=/usr/lib    
#The developer cookbook says we need to do this, but I'm not getting any import errorys, so maybe not
ld_library_path = os.environ.get('LD_LIBRARY_PATH', '') #Will be empty if the above step not done

# Print the value
print(f'LD_LIBRARY_PATH: {ld_library_path}')


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


#This is isn't the Pythonic way, and it doesn't help our editor recognise the extra packages for syntax assistance
#The VSCode way to do this is to create a settings.json for the editing with the extra paths
#and also a launch.json to launch the script uising for the extra paths.  Both sit under the project workspace for transparency.
#PyCharm and presumably Spyder would directly recognise the .env and add the relevant paths, so best to include a .env file too.


import qgis  #Only works with the same interpreter as qgis its self. So QGIS is putting useful links in with this interpreter somehow?
from qgis.gui import *   #ModuleNotFoundError: No module named 'qgis._gui'   when using the interpreter from Conda
from qgis.core import *
from qgis.utils import plugins
from qgis.analysis import QgsNativeAlgorithms 
from PyQt5.QtCore import *
 

QgsApplication.setPrefixPath('/usr', True)
app = QgsApplication([], True)
app.initQgis()                
 
#To create and work with a project
project = QgsProject.instance()
#project.read('testdata/01_project.qgs')
#print(project.fileName())
#Do some stuff
#project.write()
#project.write('testdata/my_new_qgis_project.qgs')

QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
#for alg in QgsApplication.processingRegistry().algorithms():
#       print(alg.id(), "--->", alg.displayName())

from qgis import processing
from processing.core.Processing import Processing  #What is going on here with PyLance?  Need to sort out settings.json
Processing.initialize()


shapefile_path = '/media/olly/Blue Samsung SSD/Documents/GIS/Notebooks/Data/kx-doc-huts-SHP/doc-huts.shp'
input_layer = QgsVectorLayer(shapefile_path, 'input_layer', 'ogr')  
buffer_output_path = '/home/olly/Desktop/temp_stuff/buffer.shp'

processing.run("native:buffer", {
    'INPUT': input_layer,
    'DISTANCE': 100,
    'OUTPUT': buffer_output_path
})

app.exit()
#app.exitQgis()   #Segmentation fault (core dumped) #Happens if I have opened a layer.  
#The develeper cookbook doesn't discuss this.
#app = QgsApplication([], False) a #Segmentation fault (core dumped)  #Same problem

second_app = QgsApplication([], False)   #This is OK
second_app.initQgis()
second_app.exit()           