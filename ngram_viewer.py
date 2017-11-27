''' 
Present the ngram_viwer bokeh web application

Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve --show ngram_viewer.py
at your command prompt. 
The --show option will cause a browser to open up a new tab automatically 
to the address of the running application, which in this case is:
    http://localhost:5006/ngram_viewer
in your browser.

Bo Shen
11/26/2017
'''
from ngram_counter import ngramCounter

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

# Set up data
data = []
for i in range(5):
    data.append(ngramCounter(i+1))
df2 = data[1]

results = df2.loc['I am',:] / df2.sum()
source = ColumnDataSource(data=dict(x=results.index, y=results.values))

# Set up plot
plot = figure(plot_height=400, plot_width=600, title="I am",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=(2010,2018))

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


# Set up widgets
text = TextInput(title="Enter your ngram", value='I am')


# Set up callbacks
def update_curve(attrname, old, new):
    ngram = text.value
    df = data[len(ngram.split())-1]
    if ngram not in df.index:
        plot.title.text = "Can not find the ngram in the input texts"
    else:
        plot.title.text = ngram
        results = df.loc[ngram,:] / df.sum()
        source.data = dict(x=results.index, y=results.values)



text.on_change('value', update_curve)

# Set up layouts and add to document
inputs = widgetbox(text)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Ngram viewer"