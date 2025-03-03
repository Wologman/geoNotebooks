# Readme

* This repo is for my journey towards standardising the way I work with Jupyter Notebooks & Conda with the PyQGIS API for geoprocessing & visualisation.
 
* This is a non-trivial thing.  My approach is a little hacky, and I'm aware that [Quantstack](https://quantstack.net/) may be working on a more elegent Jupyter-QGIS solution.

* Once I have perfected some practical examples, I will move all the common classes and methods to a stand-alone module so they don't clutter up the notebooks, and can be used across projects.

* I'm mostly working on-site with the New Zealand [Department of Conservation](https://www.doc.govt.nz/) terrestrial biodiversity group, but I would be interested to collaborate with others, and apply this to a variety of use-cases.  Eventually I might try producing a training course or something similar.

* Notebooks are my prefered way to begin a data project, and work well for sequential investigations, typical of geospatial workflows.  But they don't need to be the final outcome.  This could be any of a number of things:
  - The notebook its self, with all the code for maximum transparency.
  - The noteook with the code cells hidden, or functions and classes moved to a `.py` script for re-use in future projects, leaving only the data story. Saved to `.html` for easy distribution.
  - An interactive notebook hosted on a web server.
  - Just the derived outputs, like maps and plots for use in reports & publications.
  - With one more step, we can copy the functioning code into `.py` scripts, and package with the dependencies into a QGIS plugin or a custom QGIS application.
 
 * The main prize here is to to have the efficiency, reproducibility and convenience of Conda for data & ML projects + the geospatial awesomeness of QGIS, plus the logical workflow, flexibility and presentability of Jupyter notebooks.
