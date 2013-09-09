howtoplot
=========

How to plot a data


1. matrixplot.py

input: a matrix to be visualized in csv format
output: PDF visualization of the matrix

Comment out the following line if you don't need the color bar:
    cb = fig.colorbar(res)




2. dataplot.py

input: sequences of data to be plot in csv format
output: PDF plots of the sequences

Comment out the following lines when you use a linear scale
    ax.set_yscale('log') # log-scale y axis
    ax.set_xscale('log') # log-scale x axis




