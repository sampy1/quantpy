# Quantpy
A platform to do quantitative unit trading analysis. The idea is to combine a stock
screener using unittests with a real time trading platform based on patterns.

# Installation
This section describes hot to setup a machine to with all the relavent packages.

## Setting up your Enviorment.
This library was built under a conda enviorment. The file
enviorment file is called quantpy.yml

Use the following command to  load the enviorment from a file
(assuming you have conda installed)

```
conda env create -f quantpy.yml
```
# Application Structure

+ com
  + This folder is a common locations for python modules that can be called but other scripts.
  It acts as a library to both the jupyter files and test scripts when a patter is found to be
  repeably used.
+ db
  + This folder will contain code relating to the collection of data that the test will run 
  on. It is import to keep the collection of information seperate from the processing of
  the data in terms of how the code is structured.
+ img
  + Folder Containing images that .md or documenation files will work under.
+ research
  + This is a jupyter lab folder is is best run in this enviroment.
+ run
+ test
  + Folder containing unit test to be called but test runners found in the run folder. 
  Although it is possible to run these test using unittest interface directly typically 
  there is a script in the run folder that is created to run these test suites. This way 
  groups of test can be organized for documentation and study purposes.
+ <img src="https://render.githubusercontent.com/render/math?math=\TeX"> 
  + folder containing <img src="https://render.githubusercontent.com/render/math?math=\LaTeX> 
    files that can be used to gernerate documentation. However
  most documentation will be found in the from of .md files.

# Running the application

# Research Folder

This folder contains .ipynb files that jupyter lab executes on. Here is a link 
that describes how to use [Jupyter Lab](https://jupyter.org/).
