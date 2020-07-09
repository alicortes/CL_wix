#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:24:22 2020

@author: micahswann
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import pandas as pd
import plotly.io as pio
from scipy.io import loadmat
import numpy as np
import datetime as dt
import urllib

#import plotly.express as px
pio.renderers.default = 'svg'
pio.renderers.default = 'browser'

# convert matlab to python datetime
def matlab2datetime(matlab_datenum):
    day = dt.datetime.fromordinal(int(matlab_datenum))
    dayfrac = dt.timedelta(days=matlab_datenum%1) - dt.timedelta(days = 366)
    return day + dayfrac


# set current working directory
cdir = '/Users/micahswann/Documents/GitHub/CL_wix/Met/Data'
os.chdir(cdir)

fname ="20200707_KNB.txt" 
mat_dict = loadmat('20200626_BKP_gapfilled.mat', squeeze_me=True)

# load in met variables
AirT = mat_dict['AirT'] 
RH = mat_dict['RH'] 
SWin = mat_dict['SWin'] 
WDir = mat_dict['WDir']
WS = mat_dict['WS']
doy = mat_dict['doy']
atmP = mat_dict['atmP']

# convert matlab datetimes to python datetimes
my_doy = [matlab2datetime(tval) for tval in mat_dict['doy']]
date_strings = [d.strftime('%m-%d-%Y') for d in my_doy]

# create dataframe
df = pd.DataFrame(data=[my_doy,date_strings,AirT,RH,SWin,WDir,WS,atmP
                          ]).transpose()
df.columns=['doy','dates','AirT','RH','SWin','WDir','WS','atmP']
df.set_index('doy')

# initliaze subplot
fig = make_subplots(rows=3, cols=1,shared_xaxes=True,
                    specs=[[{"secondary_y": False}],
                           [{"secondary_y": False}],
                           [{"secondary_y": True}]],
                           row_heights=[1,1,1])
#Add Traces
# Air Temp
fig.add_trace(
    go.Scatter(x=df.index, y=df.AirT, name="Air Temp [C]",
     line=dict(color='black')),
    row=1, col=1, secondary_y=False,
)
    
# SWin
fig.add_trace(
    go.Scatter(x=df.index, y=df.SWin, name="SWin [w/m^2]",
     line=dict(color='black')),
    row=2, col=1, secondary_y=False,
    
)
    

# AtmP
fig.add_trace(
    go.Scatter(x=df.index,
               y=df.atmP, 
               name="atmP [cfs]",
               line=dict(color='black')),
    row=3, col=1, secondary_y=False,
    
)
    
# Wx
fig.add_trace(
    go.Scatter(x=df.index,
               y=df.WS, name="WX [m/s]",
               line=dict(color='blue')),
    row=3, col=1, secondary_y=True,
)

# Update yaxis properties
fig.update_yaxes(title_text="Air T ",autorange="reversed", row=1, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black'))
fig.update_yaxes(title_text="SWin ", row=2, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black'))
fig.update_yaxes(title_text="AtmP", secondary_y=False, row=3, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black'))
fig.update_yaxes(title_text="Wx ", secondary_y=True, row=3, col=1,
                 tickfont=dict(color='blue'),
                 title_font=dict(color='blue'))

# Set title
fig.update_layout(
    title_text= mat_dict['station'],
    title={
    'y':0.92,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})

# Update layout
fig.update_layout(
    dragmode="zoom",
    hovermode="x",
    margin=dict(
        t=100,
        b=100
    ),
)
# add range selector
fig.update_layout(  
                   xaxis=dict(
                                # Range selector with buttons
                                 rangeselector=dict(
                                     # Buttons for selecting time scale
                                     buttons=list([
                                         # 1 month
                                         dict(count=1,
                                              label='1m',
                                              step='month',
                                              stepmode='backward'),
                                         # 1 week
                                         dict(count=7,
                                              label='1w',
                                              step='day',
                                              stepmode='todate'),
                                         # 1 day
                                         dict(count=1,
                                              label='1d',
                                              step='day',
                                              stepmode='todate'),
                                         # 12 hours
                                         dict(count=12,
                                              label='12h',
                                              step='hour',
                                              stepmode='backward'),
                                          # Entire Scale                                                   
                                         dict(step='all')
                                     ])
                                 )))
fig.update_layout(
        xaxis3=dict(
                                         # Sliding for selecting time window
                                        rangeslider=dict(visible=True),
                                       side='right')
)
#
#fig.update_layout(                    annotations = [dict(xref='paper',
#                                        yref='paper',
#                                        x=0.5, y=-0.35,
#                                        showarrow=False,
#                                        text ="This data is PROVISIONAL. 2020 turbidity data has not been QAQC'd. Turbidity sensor was deployed Dec '18 - Jul '19 and Nov '19 - June '20.")])
## show fig
#pio.show(fig)

#write html
pio.write_html(fig, file='index.html', auto_open=True)
