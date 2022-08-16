# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:06:53 2022

@author: tuomas.poukkula
"""

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash_bootstrap_templates import ThemeChangerAIO
from dash_iconify import DashIconify
import random


class Block:
    
    color = 'white'
    figure = []
    
    def __init__(self, colors, xs, ys):
        
        self.color = colors
        self.figure = [go.Bar(x = [x], 
                              y = [y], 
                              width=[1],
                              offset = 0,
                              showlegend=False,
                              hoverinfo='none',
                              marker  = dict(color=color)) for x, y, color in zip(xs,ys,colors)]



col1 = Block(xs = 22*[1], 
             ys = 22*[1], 
             colors = ['orange']+4*['cyan']+17*['grey']).figure
col2 = Block(xs = 22*[2], 
             ys = 22*[1], 
             colors = ['orange']+2*['red']+3*['purple']+16*['grey']).figure
col3 = Block(xs = 22*[3], 
             ys = 22*[1], 
             colors = 2*['orange']+2*['red']+1*['purple']+3*['orange']+14*['grey']).figure
col4 = Block(xs = 22*[4], 
             ys = 22*[1], 
             colors = 2*['blue']+1*['purple']+2*['red']+1*['orange']+3*['blue']+13*['grey']).figure
col5 = Block(xs = 22*[5], 
             ys = 22*[1], 
             colors = 1*['blue']+3*['purple']+2*['red']+2*['yellow']+1*['blue']+13*['grey']).figure
col6 = Block(xs = 22*[6], 
             ys = 22*[1], 
             colors = 1*['blue']+2*['#32CD32']+1*['red']+2*['blue']+2*['yellow']+14*['grey']).figure
col7 = Block(xs = 22*[7], 
             ys = 22*[1], 
             colors = 2*['#32CD32']+2*['red']+1*['blue']+1*['orange']+2*['yellow']+14*['grey']).figure
col8 = Block(xs = 22*[8], 
             ys = 22*[1], 
             colors = 2*['yellow']+1*['red']+1*['purple']+1*['blue']+1*['orange']+2*['yellow']+4*['#32CD32']+10*['grey']).figure
col9 = Block(xs = 22*[9], 
             ys = 22*[1], 
             colors = 2*['yellow']+3*['purple']+2*['orange']+4*['#32CD32']+11*['grey']).figure
col10 = Block(xs = 22*[10], 
             ys = 22*[1], 
             colors = 22*['grey']).figure

fig1 = col1+col2+col3+col4+col5+col6+col7+col8+col9+col10



frames = []

block_len = 1

for i in range(1,23):
    
    fig = col1+col2+col3+col4+col5+col6+col7+col8+col9
    
    first_blacks = 22-i
    last_blacks = 22-first_blacks-block_len
            
    fig+= Block(xs = 22*[10], 
                  ys = 22*[1], 
                  colors = first_blacks*['grey']+block_len*['cyan']+last_blacks*['grey']).figure
    
    if i < 22:
        for j in range(2):
            frames.append(go.Frame(data=fig))
    else:
        frames.append(go.Frame(data=fig))
    
    if block_len < 4:
        block_len+=1
        
        
complete_fig = col1+col2+col3+col4+col5+col6+col7+col8+col9+Block(xs = 22*[10], 
              ys = 22*[1], 
              colors = 4*['cyan']+18*['grey']).figure


col12 = Block(xs = 22*[1], 
             ys = 22*[1], 
             colors = 4*['white']+1*['cyan']+17*['grey']).figure
col22 = Block(xs = 22*[2], 
             ys = 22*[1], 
             colors = 4*['white']+2*['purple']+16*['grey']).figure
col32 = Block(xs = 22*[3], 
             ys = 22*[1], 
             colors = 4*['white']+1*['purple']+3*['orange']+14*['grey']).figure
col42 = Block(xs = 22*[4], 
             ys = 22*[1], 
             colors = 4*['white']+1*['red']+1*['orange']+3*['blue']+13*['grey']).figure
col52 = Block(xs = 22*[5], 
             ys = 22*[1], 
             colors = 4*['white']+2*['red']+2*['yellow']+1*['blue']+13*['grey']).figure
col62 = Block(xs = 22*[6], 
             ys = 22*[1], 
             colors = 4*['white']+2*['blue']+2*['yellow']+14*['grey']).figure
col72 = Block(xs = 22*[7], 
             ys = 22*[1], 
             colors = 4*['white']+1*['blue']+1*['orange']+2*['yellow']+14*['grey']).figure
col82 = Block(xs = 22*[8], 
             ys = 22*[1], 
             colors = 4*['white']+1*['blue']+1*['orange']+2*['yellow']+4*['#32CD32']+10*['grey']).figure
col92 = Block(xs = 22*[9], 
             ys = 22*[1], 
             colors = 4*['white']+1*['purple']+2*['orange']+4*['#32CD32']+11*['grey']).figure
col102 = Block(xs = 22*[10], 
             ys = 22*[1], 
             colors = 4*['white']+18*['grey']).figure

flash_fig = col12+col22+col32+col42+col52+col62+col72+col82+col92+col102

for k in range(2):
    frames.append(go.Frame(data=flash_fig))
    frames.append(go.Frame(data=complete_fig))
    

col13 = Block(xs = 22*[1], 
             ys = 22*[1], 
             colors = 1*['cyan']+21*['grey']).figure
col23 = Block(xs = 22*[2], 
             ys = 22*[1], 
             colors = 2*['purple']+20*['grey']).figure
col33 = Block(xs = 22*[3], 
             ys = 22*[1], 
             colors = 1*['purple']+3*['orange']+18*['grey']).figure
col43 = Block(xs = 22*[4], 
             ys = 22*[1], 
             colors = 1*['red']+1*['orange']+3*['blue']+17*['grey']).figure
col53 = Block(xs = 22*[5], 
             ys = 22*[1], 
             colors = 2*['red']+2*['yellow']+1*['blue']+17*['grey']).figure
col63 = Block(xs = 22*[6], 
             ys = 22*[1], 
             colors = 2*['blue']+2*['yellow']+18*['grey']).figure
col73 = Block(xs = 22*[7], 
             ys = 22*[1], 
             colors = 1*['blue']+1*['orange']+2*['yellow']+18*['grey']).figure
col83 = Block(xs = 22*[8], 
             ys = 22*[1], 
             colors = 1*['blue']+1*['orange']+2*['yellow']+4*['#32CD32']+14*['grey']).figure
col93 = Block(xs = 22*[9], 
             ys = 22*[1], 
             colors = 1*['purple']+2*['orange']+4*['#32CD32']+15*['grey']).figure
col103 = Block(xs = 22*[10], 
             ys = 22*[1], 
             colors = 22*['grey']).figure

finished_fig = col13+col23+col33+col43+col53+col63+col73+col83+col93+col103

frames.append(go.Frame(data=finished_fig))


figure = go.Figure(data = fig1,
                   layout = go.Layout(template = 'plotly_dark',
                                      height= 1000,
                                      # margin=dict(
                                      #      l=10,
                                      #      r=10,
                                      #     #  b=10,
                                      #        t=1,
                                      #      # pad=4
                                      # ),
                                      xaxis = dict(showticklabels=False,showgrid=False,zeroline=False),
                                      yaxis=dict(showticklabels=False,showgrid=False,zeroline=False),
                                      barmode='stack'),
                   frames = frames) 

figure.update_layout(updatemenus=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 10, 
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


dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")

external_stylesheets = [
                        
                          dbc.themes.VAPOR,
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
                                radio_props={"value":dbc.themes.VAPOR})


navbar = dbc.Navbar(
    
      dbc.Container([
    
    dbc.Row([
        
        dbc.Col([
            html.A([
                html.Img(src = 'assets/gofore_logo_white.svg',
                          height="60px")
                ],
                href = 'https://gofore.com/', 
                target='_blank')
            ]),#xl = 4, lg = 4, md = 12, sm = 12),
   
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

app = Dash(__name__,
           external_stylesheets = external_stylesheets)

server = app.server

app.title = 'Plotris'

app.layout = dbc.Container([
    
        navbar,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        # html.H1('Plotris',
        #         style = {
        #                     'font-size':'80px',
        #                    'text-align':'center',
        #                    'margin-bottom': '50px'}
        # ),
        dbc.Row([dbc.Col([
            
            html.Img(src = '/assets/Plotris.png', 
                     style={
                           # 'text-align':'center',
                           # 'position' : 'center',
                           'height' : '120px',
                           # 'width':'400px'
                           # 'padding-left':50
                     }),
            
            
            ],xl=3,lg=3,md=3,sm=12,xs=12,className='"d-flex justify-content-center"')
            
            
            ],justify='center'),
        dbc.Row([
            dbc.Col([
                
                html.Br(),
                html.H2('Tetris on Plotly',
                        style = {
                                    'font-size':'52px',
                                   'text-align':'center',
                                   'margin-bottom': '30px'}),
                html.P('Press play button below to start music',
                       style = {
                                   'font-size':22,
                                  'text-align':'center'}),
                html.Div([
                    html.Audio(src='/assets/Tetris.mp3',controls=True, autoPlay = True),
                    
                ], style={'textAlign':'center'}),
                
                
                html.P('Press play button below to start animation',
                       style = {
                                   'font-size':22,
                                  'text-align':'center'}),
                ])
            ], justify = 'center'),
        
        dbc.Row([
            dbc.Col([
            dcc.Loading(children = [dcc.Graph(id = 'tetris', 
                      figure = figure,
                      config = {'displaylogo': True,
                                'modeBarButtonsToRemove': ['zoom', 'pan', 'select', 'zoomIn', 'zoomOut', 'autoScale', 'resetScale','lasso2d']})],
                        type = random.choice(['graph', 'cube', 'circle', 'dot' ,'default']))
            ], xl=3,lg=6,md=6,sm=12,xs=12)
            ],justify='center'),
        html.Br(),
        html.P('This graph was produced by animating a Plotly bar chart.',
               style = {
                           'font-size':22,
                          'text-align':'center'}),
        
        html.Div([html.Label(['Check the Project on ', 
                html.A('GitHub', href='https://github.com/tuopouk/plotris')
                ],style={
                            'font-size':22,
                           'text-align':'center'})]),
        html.Div([html.Label([
                  html.A('Music source', href = "https://archive.org/details/TetrisThemeMusic",target="_blank")
                ],style={
                            'font-size':22,
                           'text-align':'center'})]),
        html.Div([html.Label(['Design adapted from ',
                  html.A('The New York Times', href = "https://archive.nytimes.com/takingnote.blogs.nytimes.com/2015/07/15/video-games-could-be-good-for-your-mind/",target="_blank")
                ],style={
                            'font-size':22,
                           'text-align':'center'})]),           
        
    
    
    ], fluid = True, className = 'dbc')

if __name__ == "__main__":
    app.run_server(debug=False)