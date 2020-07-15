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

def moving_average(a, n=24) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

# select station
station = input('Enter a station ID (BKP,BVR,BEK,NIC,NLP,CLO,KNB,JGB: ')

# set current working directory
cdir = '/Users/micahswann/Documents/GitHub/CL_wix/Met/'
cdir += '%s' % station
os.chdir(cdir)

# get station name
if station == 'BEK':
    name = 'Beakbane Island'
elif station == 'BKP':
    name = 'Buckingham Point'
elif station == 'BVR':
    name = 'Big Valley Rancheria'
elif station == 'CLO':
    name = 'Clearlake Oaks'
elif station == 'KNB':
    name = 'Konocti Bay'
elif station == 'NIC':
    name = 'Nice'
elif station == 'JGB':
    name = 'Jago Bay'
elif station == 'NLP':
    name = 'North Lakeport'


fileExt =r".mat"
fname = [_ for _ in os.listdir(cdir) if _.endswith(fileExt)]
fname = fname[0]
mat_dict = loadmat(fname, squeeze_me=True)

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

# daily averages
#n = 24
#nn = 24*5
#df['AirT_avg'] = df.AirT.rolling(n).mean()
#df['RH_avg'] = df.RH.rolling(n).mean()
#df['SWin_avg'] = df.SWin.rolling(nn).mean()
#df['WDir_avg'] = df.WDir.rolling(n).mean()
#df['WS_avg'] = df.WS.rolling(n).mean()
#df['atmP_avg'] = df.atmP.rolling(n).mean()


# initliaze subplot
fig = make_subplots(rows=6, cols=1,shared_xaxes=True,
                    specs=[[{"secondary_y": False}],
                           [{"secondary_y": False}],
                           [{"secondary_y": False}],
                           [{"secondary_y": False}],
                           [{"secondary_y": False}],
                           [{"secondary_y": False}]],
                           row_heights=[1,1,1,1,1,1])
#Add Traces
# Air Temp
fig.add_trace(
    go.Scatter(x=df.doy, y=df.AirT, name="Air Temp [C]",
     line=dict(color='black')),
    row=1, col=1, secondary_y=False,
)   
# Avg Air Temp
#fig.add_trace(
#    go.Scatter(x=df.doy, y=df.AirT_avg, name="Rolling Avg Air Temp [C]",
#     line=dict(color='red')),
#    row=1, col=1, secondary_y=False,
#)

# RH
fig.add_trace(
    go.Scatter(x=df.doy, y=df.RH, name="Relative Humidity [%]",
     line=dict(color='black')),
    row=2, col=1, secondary_y=False,
)   
# RH AtmP
#fig.add_trace(
#    go.Scatter(x=df.doy, y=df.RH_avg, name="Rolling Avg Rel Hum [%]",
#     line=dict(color='red')),
#    row=2, col=1, secondary_y=False,
#)

# AtmP
fig.add_trace(
    go.Scatter(x=df.doy, y=df.atmP, name="Atmospheric Pressure [kPa]",
     line=dict(color='black')),
    row=3, col=1, secondary_y=False,
)   
# Avg AtmP
#fig.add_trace(
#    go.Scatter(x=df.doy, y=df.atmP_avg, name="Rolling Avg Atm Press [kPa]",
#     line=dict(color='red')),
#    row=3, col=1, secondary_y=False,
#)
    
# WS
fig.add_trace(
    go.Scatter(x=df.doy, y=df.WS, name="Wind Speed [m/s]",
     line=dict(color='black')),
    row=4, col=1, secondary_y=False,
)   
# Avg WS
#fig.add_trace(
#    go.Scatter(x=df.doy, y=df.WS_avg, name="Rolling Avg Wind Speed [m/s]",
#     line=dict(color='red')),
#    row=4, col=1, secondary_y=False,  
#)
    
# WDir
fig.add_trace(
    go.Scatter(mode='markers',x=df.doy, y=df.WDir, name="Wind Direction [Deg]",
            marker=dict(
            color='black',
            size=2,
            line=dict(
                color='black',
                width=1
            ))),
    row=5, col=1, secondary_y=False,
)
    
# SWin
fig.add_trace(
    go.Scatter(x=df.doy, y=df.SWin, name="Incoming Shortwave Radiation [w/m^2]",
     line=dict(color='black')),
    row=6, col=1, secondary_y=False,    
)
# Avg SWin
#fig.add_trace(
#    go.Scatter(x=df.doy, y=df.SWin_avg, name="Rolling Avg SWin [w/m^2]",
#     line=dict(color='red')),
#    row=6, col=1, secondary_y=False,
#)    

n = 12
# Update yaxis properties
fig.update_yaxes(title_text="Air Temp<br>[C]",row=1, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black',size =n))
fig.update_yaxes(title_text="RH<br>[%]", row=2, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black',size =n))
fig.update_yaxes(title_text="AtmP<br>[kPa]", secondary_y=False, row=3, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black',size =n))
fig.update_yaxes(title_text="Wx<br>[m/s]", secondary_y=False, row=4, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black',size =n))
fig.update_yaxes(title_text="WDir<br>[Deg]", secondary_y=False, row=5, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black',size =n))
fig.update_yaxes(title_text="SWin<br>[w/m^2]", secondary_y=False, row=6, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black',size =n))

# Set title
fig.update_layout(
    title_text= name + ' Meteorological Data',
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
                                         # 1 year
                                         dict(count=1,
                                              label='1y',
                                              step='year',
                                              stepmode='backward'),
                                         # 6 month
                                         dict(count=6,
                                              label='6m',
                                              step='month',
                                              stepmode='backward'),
                                         # 1 month
                                         dict(count=1,
                                              label='1m',
                                              step='month',
                                              stepmode='backward'),
                                         # 1 days
                                         dict(count=7,
                                              label='1w',
                                              step='day',
                                              stepmode='backward'),
                                          # Entire Scale                                                   
                                         dict(step='all')
                                     ])
                                 )))
fig.update_layout(
        xaxis6=dict(
                                         # Sliding for selecting time window
                                        rangeslider=dict(visible=True),
                                       side='right')
)

fig.update_layout(                    annotations = [dict(xref='paper',
                                        yref='paper',
                                        x=0.5, y=-0.35,
                                        showarrow=False,
                                        text ="Select desired date range with slider in the bottom panel above. <br> <b> This data is PROVISIONAL and has not been QAQC'd")])

#write html
pio.write_html(fig, file='index.html', auto_open=True)
