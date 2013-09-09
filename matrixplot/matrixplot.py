#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv
import os.path



def csv2matrix(filename):
    # see http://docs.python.jp/2/library/csv.html
    myReader = csv.reader(open(filename, 'rU'))     # see http://stackoverflow.com/questions/6726953/open-the-file-in-universal-newline-mode-using-csv-module-django
    matrix = []
    for row in myReader:
        #    print([float(i) for i in row])
        matrix.append(map(float,row))
    return matrix




def matrix2pdf(matrix, pdffilename, maxval, cmap):

    # code from http://stackoverflow.com/questions/5821125/how-to-plot-confusion-matrix-with-string-axis-rather-than-integer-in-python

    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    res = ax.imshow(np.array(matrix),
                    cmap=plt.cm.get_cmap(cmap),
                    norm=matplotlib.colors.Normalize(vmin=0.0, vmax=maxval),
                    interpolation='nearest')

    width = len(matrix)
    height = len(matrix[0])

    for x in xrange(width):
        for y in xrange(height):
            ax.annotate(str('{:.3f}'.format(matrix[x][y])),
                        xy=(y, x),
                        size=8,
                        color = str(1 if 1-(maxval-matrix[x][y])/maxval > 0.5 else 0),
                        horizontalalignment='center',
                        verticalalignment='center')


    cb = fig.colorbar(res) # this shows color bar
    
    plt.xticks(range(width),  map(str,range(1,width+1)))
    plt.yticks(range(height), map(str,range(1,width+1)))

    plt.savefig(pdffilename, bbox_inches='tight', format='pdf')





csvfiles = [
            # ['csv_filename.csv', maximum_value, 'colormap_name'],
            
            ['data_matrix.csv', 0.2, 'Greys'], # cmap is here http://matplotlib.org/examples/color/colormaps_reference.html
            ['data_matrix.csv', 0.6, 'Greys'],
            
            ['data_matrix.csv', 0.2, 'jet'],
            ['data_matrix.csv', 0.2, 'rainbow'],
            ]

for fm in csvfiles:
    f = fm[0]
    maxval = fm[1]
    cmap = fm[2]
    root, ext = os.path.splitext(f)
    mat = csv2matrix(f)
    matrix2pdf(mat, root + str(maxval) + cmap + '.pdf', maxval, cmap)





