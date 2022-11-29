import pandas as pd
import numpy as np
from IPython.display import display

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

data = pd.DataFrame(pd.read_excel("class_enrollment_summary_fall_2022.xlsx"))
data.columns = data.iloc[2]

data.drop(labels = [0, 1, 2, 2866, 2867, 2868, 2869, 2870, 2871], axis = 0, inplace = True)

#enrollment = data.groupby('Course Department')['Total'].sum().reset_index()

# looking just at undergrad
u_enrollment = data.groupby('Course Department')['UGrad'].sum().reset_index()
display(u_enrollment[(u_enrollment['UGrad'] > 0)].sort_values(by="UGrad", ascending = False).head(20))

# looking just at grad
g_enrollment = data.groupby('Course Department')['Grad'].sum().reset_index()
display(g_enrollment[(g_enrollment['Grad'] > 0)].sort_values(by="Grad", ascending = False).head(20))

# colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title = {'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':18, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)', 
                'title':{'font':{'size':18, 'family':"Helvetica", 'color':monochrome_colors[0]}}, 
                'font':{'size':14, 'family':"Helvetica"}, 
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True, 
                'cauto':True, 
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)

fig = go.Figure(layout=go.Layout(barmode='stack'))

df1 = u_enrollment[(u_enrollment['UGrad'] > 0)].sort_values(by="UGrad", ascending = False).head(10).reset_index()

fig.add_trace(go.Bar(
    x=df1['Course Department'],
    y=df1['UGrad'],
    name='undergrad',
    marker_color=primary_colors[2],
))


fig.update_layout(title="Undergraduate Course Enrollment by Department", 
                xaxis={'title':{'text':'Course Department'}}, 
                yaxis={'title':{'text':'Undergraduate Enrollment'}}, 
                legend={'title':{'text':'Political Party'}},
                template=theme_hodp)

fig.show()


"""
fig2 = go.Figure(layout=go.Layout(barmode='stack'))

df2 = g_enrollment[(g_enrollment['Grad'] > 0)].sort_values(by="Grad", ascending = False).head(10).reset_index()

fig2.add_trace(go.Bar(
    x=df2['Course Department'],
    y=df2['Grad'],
    name='grad',
    marker_color=primary_colors[0],
))


fig2.update_layout(title="Graduate Course Enrollment by Department", 
                xaxis={'title':{'text':'Course Department'}}, 
                yaxis={'title':{'text':'Graduate Enrollment'}}, 
                legend={'title':{'text':'Political Party'}},
                template=theme_hodp)

fig2.show()
"""
