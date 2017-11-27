# Minimal Google Ngram Viewer

The goal of this project is to create a simple local version of Google Ngram Viewer, 
which can be found here https://goo.gl/7feVzf.

## Overview
The Jupyter notebook, prototype.ipynb, is the notebook I used to test different components of the application,
and create a prototype web application using bokeh.  

The python file, ngram_counter.py is a module that provides model needed for ngram_viewer.

The python file, ngram_viewer.py is the main file of the Bokeh web application for the ngram viewer.

## Environment Setting and test

### Prototype notebook
To run the Jupyter notebook, you need Python 2.7.12, Jupyter notebook 5.0.0.,
Bokeh 0.12.7.. and ipywidgets 6.0.  
The ipywidgets need to be install for Jupyter notebook using the following command:
```
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension
``` 

### Ngram Viewer Web Application
For environment setting, you need Python 2.7.12 and Bokeh 0.12.7.
To run the web application, please set the working directory to task, and run the following command:
```
bokeh serve --show ngram_viewer.py
```
You can only enter one ngram at a time.