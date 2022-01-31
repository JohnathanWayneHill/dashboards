import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash(__name__) # starts the app                                          

app.layout = html.Div([html.H1("Hello"),
                      html.H2("Goodbye"),
                      html.H1("do dododdo"),
                      html.H5("dodododoodod"),
                      html.P(
                             ["Hello this is a cool paragraph!!!!", html.Br(),
                              "I am typing more stuff here"]
                      )],
                       style={"background-color": "#FF5733"}
                  )

if __name__ == "__main__": 
    app.run_server(debug=True)


