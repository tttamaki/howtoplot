#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import matplotlib
import os.path



def data2pdf(matrix, pdffilename, xlabel, ylabel):

    fig, ax = plt.subplots()
    #ax.set_yscale('log') # log-scale y axis
    ax.set_xscale('log') # log-scale x axis
    
    n=len(matrix)
    xs = []
    y1 = []
    y2 = []
    for i in range(n):
        xs.append(matrix[i][0])
        y1.append(matrix[i][1])
        y2.append(matrix[i][2])

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.plot(xs, y1, '^-', label=matrix.dtype.names[1])
    ax.plot(xs, y2, 'o-', label=matrix.dtype.names[2])

    legend = ax.legend(loc='best', frameon=False, fontsize=12) # http://matplotlib.org/api/axes_api.html?highlight=legend#matplotlib.axes.Axes.legend

    plt.savefig(pdffilename, bbox_inches='tight', format='pdf')






csvfiles = ['data_plots.csv',
            'data_plots2.csv',
            ]

#
# csv files format
#
#,data1,data2
#1,23668.81639,23171.30534
#2,183.9278111,0.20429081
#3,183.9822717,0.109836458
#4,184.0359456,0.065261084




for f in csvfiles:
    root, ext = os.path.splitext(f)
    mat = matplotlib.mlab.csv2rec(f) # http://matplotlib.org/api/mlab_api.html?highlight=csv2rec#matplotlib.mlab.csv2rec

    data2pdf(mat, root + '.pdf', 'number', 'values')




