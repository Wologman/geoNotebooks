# Geospatial analysis with Conda, Jypyter and PyQGIS
My goal for this project is to bring together the strengths of two  approaches to working with Geospatial data: 
- **QGIS** | An awesome open-source GIS package with a Python API
- **Jupyter Notebooks** | A great way to explore and visualise data sequentially in Python
- **Conda** | For reproducibility and package management

## Introduction
Let's consider the strengths of each element, that when brought together, create advantages one or the other misses.

### Advantages from QGIS
- Makes beautiful maps
- Brings together a bunch of open-source third-party Python tools, but with a consistent wrapper, making them easier to learn & work with.
- Has some advanced geoprocessing tools not easily found from standard Python libraries.

### Advantages from Conda
- Reproducibility
- The Conda package battle between packages is done for you at the solver stage.
- Works with all the main Python machine learning libraries and frameworks such as Scikit-Learn, PyTorch or Tensorflow

### Advantages from Juypter

- The entire workflow and any mathematical or logical arguments are preserved step by step.  Great for visualising spatial workflows.
- Statistical results can be plotted nicely with dedicated plotting libraries for later publication or presentation.
- Mathematical and logical arguments can be presented with the combined presentability of Markdown and LaTeX.
- The whole notebook can be converted to interactive `html` files, and the code can even be hidden for non-technical audiences.
- In theory we could run some stuff in other languages and continue with the results.
- Can work directly with rasters as NumPy arrays for speed and memory efficiency, or even do some processes on GPU with Pytorch or Tensorflow.
- Functions and classes written from one project be imported easily in future projects.

Since these are some awesome wins, this seems like quite a worthwhile endevour. 

### The Catch
- Is a pain dealing with any conflicting dependency versions shared between Conda-QGIS resources.  Currently I can't seem to use Seaborn or Ipyleaflet.
- Jupyter on Windows can't do multi-core processing in-place.
- Interaction with some IDEs can be a bit buggy.
- The complexity of the setup, needing to reference both .env variables and Conda.

Those are all pretty annoying at times, but things I can live with.

## Who might want to do this?
What role would these notebooks fill and for who?

**For students**  
The reproducibility and logic to the workflows are such key concepts here, this is a great way to learn to work with spatial data, even if it is a little slower to begin with.

**For specialist science roles**  
For example monitoring biodiversity, erosion, land-use change etc.  This approach could make working with spatial data faster, more presentable and more repeatable. Especially for projects that may get repeated a few times in similar ways. If a dataset needs updatating every year, and all the package versions are nicely locked down, the code should keep running smoothly.

**For Spatial Data Scientists & Machine Learning specialists**  
Or really for anybody who is providing that next level of Python & spatial data expertise to the subject specialists mentioned above.  This would cover data exploration, data cleaning, posssibly even feature engineering.  Also lifting the presentability of visualisation of our for our final models.

**For software engineers for spatial tools and QGIS plugin development**  
Working initially in notebooks can be a convenient way to do initial prototyping, visualise outcomes and troubleshoot our ideas as we go along.  Once that phase is over, everything can be moved into .py scripts for QGIS pluggin or application development.

## Setup


### QGIS Setup in Ubuntu

[From here](https://qgis.org/en/site/forusers/alldownloads.html)

```bash
sudo apt install gnupg software-properties-common

sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```

Now we open a text editor in `/etc/apt/sources.list.d`

```bash
sudo nano /etc/apt/sources.list.d/qgis.sources
```

Then in the case of Jammy Jellyfish paste the following.   For any other Linux release, check the release code first and replace the jammy. To check the release code type: `lsb_release -cs` and replace jammy with that.

```bash
Types: deb deb-src  
URIs: https://qgis.org/debian  
Suites: jammy  
Architectures: amd64  
Components: main  
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg 
``` 
If this worked there should be a new file `qgis.sources` located in `/etc/apt/sources.list.d`.

- Control O to write to the permission directory, then enter
- Control X to exit the nano editor
- Then:  
`sudo apt update`  
`sudo apt install qgis qgis-plugin-grass`

### Conda in Ubuntu

[Install miniConda as per the website](https://docs.anaconda.com/miniconda/)  

Make sure Conda is initialised in this process.  (It doesn't happen automatically if using the block of commands in the linux instructions)

To turn off auto activation into the base environment

`conda config --set auto_activate_base false`


[Set the solver to Mamba as per instructions here](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community)

```Bash
conda update -n base conda
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
conda config --set auto_activate_base False #optional but I think it's best because you never really want to use base for much.
```

### Setup a Python Environment with Conda

This is really important. It ensures we are being transparent and consitant with all our package and Python versions between projects.  A method shouldn't fall over randomly some day just because some underlying package has been updated.  

Open a terminal in the location of your environment.yaml files and run  
 `conda env create -f my_environment.yaml`
 replacing `my_environment.yaml` with what ever env yaml file you are working with.

Once it's complete, run `conda activate my_fancy_environment_name`  followed by `conda list` to check you've got all the packages you expected.

If some or all of the packages in the list aren't pinned to a particular version, you can do that at the end of your project.  Or at least before you start working on another machine.
  

# Load environment variables from .env file


- Make the conda env using same python version and shared package versions.
- Set INTERPRETERPATH, PYTHONPATH, LD_LIBRARY_PATH  
- Use the QGIS interpreter (The system python for UBUNTU)
- Form terminal source the .env then run with the interpreter from $INTERPRETER_PATH
- For VSCode need to set up launcher, linter, debugger in the `.vscode` json file
- You do NOT run directly though Conda, since this over-writes the environment variables

## Environment Variables for our Python Path
