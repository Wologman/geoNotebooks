import os, sys
from dotenv import load_dotenv

load_dotenv()

for path in os.environ['PYTHONPATH'].split(':'):
    if path not in sys.path:
        sys.path.append(path)

print('PYTHONPATH:', os.environ['PYTHONPATH'])
print('sys.path:', sys.path)

try:
    import qgis
    import processing
    print('Libraries imported successfully!')
except ImportError as e:
    print(f'Error importing libraries: {e}')

from qgis.gui import *
from qgis.core import *
from qgis.utils import plugins
from PyQt5.QtCore import *
from qgis.analysis import QgsNativeAlgorithms


QgsApplication.setPrefixPath('/usr', True)
app = QgsApplication([], False)
app.initQgis()


from processing.core.Processing import Processing
Processing.initialize()

QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
for alg in QgsApplication.processingRegistry().algorithms():
        print(alg.id(), "--->", alg.displayName())


### Do some processing  ###
input_layer = QgsVectorLayer('/path/to/your/shapefile.shp', 'input_layer', 'ogr')
buffer_output = '/path/to/output/buffer.shp'

processing.run("native:buffer", {
    'INPUT': input_layer,
    'DISTANCE': 100,
    'OUTPUT': buffer_output
})


app.exitQgis()
app.exit()