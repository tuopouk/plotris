# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:33:37 2022

An app to play with Plotly animations.

@author: tuomas.poukkula
"""

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash_bootstrap_templates import ThemeChangerAIO
from dash_iconify import DashIconify
import random

dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")

external_stylesheets = [
                        
                          dbc.themes.YETI,
                          dbc_css,
                          dbc.icons.BOOTSTRAP
                          
                        ]

theme_changer = ThemeChangerAIO(aio_id="theme", 
                                button_props={'title':'Change Color Theme',
                                                 'size':'sm',
                                              'children' : 'Change Color Theme',
                                              'outline':False,
                                              'style':{'font-weight': 'bold'},
                                              'color':'success'},
                                offcanvas_props={'title':"Select a Color Theme",
                                                 
                                                  'scrollable':True},
                                radio_props={"value":dbc.themes.YETI})


navbar = dbc.Navbar(
    
      dbc.Container([
    
    dbc.Row([
        
   
        dbc.Col([
            dbc.NavItem(theme_changer),
            
            ], align='center'),#xl = 4, lg = 4, md = 6, sm = 6),

        
        ], align='center',
        className = "d-flex justify-content-start"
        ),
    


        dbc.Row([
                    dbc.Col(
                        [
                         
                           dbc.Collapse(
                            dbc.Nav([
                                dbc.NavbarBrand("by: Tuomas Poukkula",style={'font-style':'italic'}, className="ms-2"),
                                dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"), href="https://github.com/tuopouk/",external_link=True, target='_blank') ),
                                dbc.NavItem(dbc.NavLink(html.I(className="bi bi bi-twitter"), href="https://twitter.com/TuomasPoukkula",external_link=True, target='_blank') ),
                                dbc.NavItem(dbc.NavLink(html.I(className="bi bi-linkedin"), href="https://www.linkedin.com/in/tuomaspoukkula/",external_link=True, target='_blank') ),
                                
                                
                            ]
                            ),
                             id="navbar-collapse",
                             is_open=False,
                             navbar=True
                           )
                          ]
                    )
                ],align="center", className = "d-flex justify-content-end"),
        dbc.Row([
            dbc.Col(DashIconify(
        icon="simple-icons:plotly",
        width=30,
    ), align = 'center')
            
              ], align = 'center', className = "d-flex justify-content-end")


    
      ],className='d-flex justify-content-between', fluid=True
        ),
                            
    color="primary",
    dark=True,
    className = 'navbar fixed-top'
    )

frames = []

frame = 0.00

for i in range(1000):
    
    if frame > .30:
        frame = 0.00
    
    frames.append(
        
        go.Frame(data=[
             go.Pie(labels = ['1','2','3','4','5','6'],
                    values = [.20,.20,.20,.20,.20,frame], 
                    showlegend=False,
                    sort=False,
                    textinfo='text',
                    text = ['●','','','','',''],
                    textfont=dict(size=80,color='black'),
                    textposition='inside',
                    hoverinfo='none',
                   marker=dict(colors=['yellow','yellow','yellow','yellow','yellow','white'],
                               )
                    )
             ])
        
        )
    frame = frame + 0.01
    

figure = go.Figure(data=[
    
    go.Pie(labels = ['1','2','3','4','5','6'],
           values = [.20,.20,.20,.20,.20,.30], 
           showlegend=False,
           sort=False,
           textinfo='text',
           text = ['●','','','','',''],
           textfont=dict(size=80,color='black'),
           textposition='inside',
           hoverinfo='none',
          marker=dict(colors=['yellow','yellow','yellow','yellow','yellow','white'],
                      )
           )
    
    ],
    layout = go.Layout(plot_bgcolor='black',
                       
                       legend=None,
                       height=800
                       ),
    frames=frames

    )
    
figure.update_layout(updatemenus=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 20, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "▶",
                                               method = "animate")],
                                type='buttons',
                                showactive=False,
                                y=1.2,
                                x=.5,
                                xanchor='right',
                                yanchor='top')])    

app = Dash(__name__,
           external_stylesheets = external_stylesheets)

server = app.server

app.title = 'Pacmanimation'

app.layout = dbc.Container([
    
        navbar,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1('Pacmanimation',
                style = {
                            'font-size':'80px',
                           'text-align':'center',
                           'margin-bottom': '50px'}
        ),
        html.H2('Pac-Man on Plotly',
                style = {
                            'font-size':'52px',
                           'text-align':'center',
                           'margin-bottom': '30px'}),
        html.P('Press play button below to start animation',
               style = {
                           'font-size':22,
                          'text-align':'center'}),
        dcc.Loading(children = [dcc.Graph(id = 'pacman', 
                  figure = figure)],
                    type = random.choice(['graph', 'cube', 'circle', 'dot' ,'default'])),
        html.Br(),
        html.P('This graph was produced by animating a Plotly pie chart.',
               style = {
                           'font-size':22,
                          'text-align':'center'}),
        html.Label(['Check the Project on ', 
                html.A('GitHub', href='https://github.com/tuopouk/pacmanimation')
                ],style={
                            'font-size':22,
                           'text-align':'center'})
        
    
    
    ], fluid = True, className = 'dbc')

if __name__ == "__main__":
    app.run_server(debug=False)