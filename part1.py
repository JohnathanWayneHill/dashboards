import dash 
import dash_core_components as dcc # don't need this yet
import dash_html_components as html 
import plotly.graph_objs as go # don't need this yet

app = dash.Dash(__name__) 

app.layout = html.Div(id='big_container', children = [ 
                         html.H1('Hello'), 
                         html.P(["this is some text", html.Br(), "this is some more text still"]),
                         html.Div( 
                             html.H3("goodbye"), 
                             style = {"background-color": "#FF33B5", "color": "#335BFF", "width": "100px"}
                         )
             ])

if __name__ == '__main__': 
    app.run_server(debug=True)
