import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import pandas as pd
import plotly.io as pio
import plotly.express as px
pio.renderers.default = 'svg'
pio.renderers.default = 'browser'

# request user input of station ID
#station = input('Enter a station ID (KCK, MCU, or SCS) : ')
station = 'KCK'
# set current working directory
cdir = '/Users/micahswann/Documents/GitHub/CL_wix/Streams/'
cdir += '%s' % station
os.chdir(cdir)

# get station name
if station == 'KCK':
    name = 'Kelsey Creek'
elif station == 'MCU':
    name = 'Middle Creek'
else:
    name = 'Scotts Creek'

# load in DWR data
path = '%s' % station
path += '_DWR.csv'  
df = pd.read_csv(path, index_col=0, parse_dates=True,skiprows=2, names=['index','stage','flow'])
dwr = df

## load in flow data
#path = '%s' % station
#path += '_flow_DWR.csv'
#df = pd.read_csv(path,
#                 header=[0,], index_col=4, parse_dates=True)
#flow = df;
#
## load in stage data
#path = '%s' % station
#path += '_stage_DWR.csv'
#df = pd.read_csv(path,
#                 header=[0,], index_col=4, parse_dates=True)
#stage = df;

# load in turbidity data
path = '%s' % station
path += '_Turb.csv'
df = pd.read_csv(path,
                 header=[0,], index_col=0, parse_dates=True)
turb = df;

# load in precip data
path = '%s' % station
path += '_precip_WWG.csv'
df = pd.read_csv(path,
                 header=[0,], index_col=[0,], parse_dates=True)
precip = df;

# initliaze subplot
fig = make_subplots(rows=3, cols=1,shared_xaxes=True,
                    specs=[[{"secondary_y": False}],
                           [{"secondary_y": False}],
                           [{"secondary_y": True}]],
                           row_heights=[0.5,0.5,0.7])
#Add Traces
# Precip
fig.add_trace(
    go.Scatter(x=precip.index, y=precip.Rain, name="Precipitation [in]",
     line=dict(color='black')),
    row=1, col=1, secondary_y=False,
    
)
    
# Turbidity
fig.add_trace(
    go.Scatter(x=turb.index, y=turb.Turb, name="Turbidity [NTU]",
     line=dict(color='black')),
    row=2, col=1, secondary_y=False,
    
)
    

#flow
fig.add_trace(
    go.Scatter(x=dwr.index,
               y=dwr.flow, 
               name="Flow [cfs]",
               line=dict(color='black')),
    row=3, col=1, secondary_y=False,
    
)
    
#stage
fig.add_trace(
    go.Scatter(x=dwr.index,
               y=dwr.stage, name="Stage [in]",
               line=dict(color='blue')),
    row=3, col=1, secondary_y=True,
)

# Update yaxis properties
fig.update_yaxes(title_text="Precipitation [in]",autorange="reversed", row=1, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black'))
fig.update_yaxes(title_text="Turbidity [NTU]", row=2, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black'))
fig.update_yaxes(title_text="Flow [cfs]", secondary_y=False, row=3, col=1,
                 tickfont=dict(color='black'),
                 title_font=dict(color='black'))
fig.update_yaxes(title_text="Stage [in]", secondary_y=True, row=3, col=1,
                 tickfont=dict(color='blue'),
                 title_font=dict(color='blue'))

# Set title
fig.update_layout(
    title_text=name,
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

# show fig
#pio.show(fig)

#write html
pio.write_html(fig, file='index.html', auto_open=True)
