"""
Helper script to plot mutation stats from mutation-stats-manual-analysis.csv
"""


import pandas as pd
import numpy as np
import holoviews as hv
from holoviews import opts

hv.extension('bokeh')

df = pd.read_csv('../mutation-stats-manual-analysis.csv')


def points_bars(df, x_column, y_columns):
    """
    Plot counts of each replicate, then plot the mean of y_columns as bars
    and the individual values as points in a layout
    then save as an html file and return the plot

    args:
        df: pandas dataframe
        x_column: column to plot on x axis
        y_columns: list of columns to plot on y axis

    returns:
        plots: hv.Layout
    """
        
    # add count column to original df
    df['replicates'] = df.groupby(x_column)[y_columns[0]].transform('count')
    # plot counts of each different polymerase
    replicates_plot = hv.Bars(df, 'nonsynonymous TPDNAP mutations', vdims=['replicates', 'hex_color']).opts(color='hex_color', tools=['hover'], width=800, height=600, xrotation=70, show_legend=False, fontsize={'title':16,'labels':14,'xticks':10,'yticks':10})

    aggs = {'hex_color':'first'}
    aggs.update({col:'mean' for col in y_columns})
    avg_df = df.groupby(x_column, sort=False).agg(aggs).reset_index()
    plots = [replicates_plot]
    for col in y_columns:
        # Create the HoloViews objects
        points = hv.Points(df[df['replicates']>1], [x_column, col]).opts(tools=['hover']).opts(color='black', alpha=0.7, jitter=0.2, size=6)
        bars = hv.Bars(avg_df, x_column, vdims=[col,'hex_color']).opts(color='hex_color', tools=['hover'])

        plot = bars * points

        # Apply the options
        plots.append(plot.opts(width=800, height=600, xrotation=70, show_legend=False, fontsize={'title':16,'labels':14,'xticks':10,'yticks':10}))

    plots = hv.Layout(plots).cols(1)

    hv.save(plots, 'TPDNAP-mutation-stats.html')

    return plots

points_bars(df, 'nonsynonymous TPDNAP mutations', ['total_seqs', 'mean_NT_mutations_per_seq', 'transitions per sequence', 'transversions per sequence', 'unique transversions per sequence'])
