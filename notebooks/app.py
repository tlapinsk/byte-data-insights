# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from components import Header, make_dash_table, print_button

import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# # # # # # # # #
# detail the way that external_css and external_js work and link to alternative method locally hosted
# # # # # # # # #
external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

for css in external_stylesheets:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

# read data for tables (one df per table)
df_items_purchased = pd.read_csv("~/Desktop/items_purchased.csv")
df_product_info = pd.read_csv("../data/product_info.csv")

# Items purchased
df_items_purchased_head = df_items_purchased.head()

report = df_items_purchased.groupby('product_id').product_id.count().reset_index(name ='count')
report = report.sort_values(by='count', ascending=False)
popular = report.head(n=10)

## Page layouts
app.layout = html.Div([  # page 1

        print_button(),

        html.Div([
            Header(),

            # Row 3
            html.Div([

                html.Div([
                    html.H6('Insights',
                            className="gs-header gs-text-header padded"),


                    html.Br([]),

                    html.P("\
                            This page provides a sample of mockups for a web based report \
                            that could be used by Byte Foods. Instructions for running this \
                            locally are found below:"),
                    html.P("\
                            pip install dash==0.28.2  # The core dash backend"),
                    html.P("\
                            pip install dash-html-components==0.13.2  # HTML components"),
                    html.P("\
                            pip install dash-core-components==0.30.2  # Supercharged components"),
                    html.P("\
                            cd /byte-foods-insights/notebooks"),
                    html.P("\
                            python app.py"),
                    html.P("\
                            Navigate to http://127.0.0.1:8050/"),
                ], className="six columns"),

            ], className="row "),

            # html.Div([

            #     html.Div([
            #         html.H6('Items Purchased',
            #                 className="gs-header gs-text-header padded"),

            #         html.Table(make_dash_table(df_items_purchased_head))
            #     ], className="six columns"),

            # ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6('Most Popular Products',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-1",
                        figure={
                            'data': [
                                go.Bar(
                                    x = ["4207", "2360", "4793", "4202", "4061"],
                                    y = ["24443", "	26496", "27828", "32361", "68369"],
                                    marker = {
                                      "color": "rgb(23, 55, 79)",
                                      "line": {
                                        "color": "rgb(23, 55, 79)",
                                        "width": 2
                                      }
                                    },
                                    name = "Products"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.189563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 10,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),


                html.Div([
                    html.H6("Time of Day",
                            className="gs-header gs-table-header padded"),
                        dcc.Graph(
                            id='sns_pie_1',
                            figure={
                                "data": [
                                    go.Pie(
                                        labels= ['Morning','Afternoon','Evening'],
                                        values= [226988, 274805, 613779],
                                        marker={"colors": ["#B0D0E8", "#3A88C4", "#17374F"]},
                                    )
                                ],
                            'layout': go.Layout(
                                autosize = False,
                                title = "",
                                font = {
                                    "family": "Raleway",
                                    "size": 10
                                },
                                height = 200,
                                width = 340,
                                hovermode = "closest",
                                legend = {
                                    "x": -0.0277108433735,
                                    "y": -0.142606516291,
                                    "orientation": "h"
                                },
                                margin = {
                                    "r": 20,
                                    "t": 20,
                                    "b": 20,
                                    "l": 50
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6('Top Purchasers',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-3",
                        figure={
                            'data': [
                                go.Bar(
                                    x = ["648", "680", "686", "698", "745", "787", "791", "1444", "1688", "24467"],
                                    y = ["MKK", "nJq", "mvq", "bNa", "3jT", "RT0", "V+t", "y4u", "sZc", "pxW"],
                                    marker = {
                                        "color": "rgb(23, 55, 79)",
                                        "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "Total purchases",
                                    orientation='h'
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                    "family": "Raleway",
                                    "size": 10
                                },
                                height = 275,
                                hovermode = "closest",
                                legend = {
                                    "x": -0.0228945952895,
                                    "y": -0.189563896463,
                                    "orientation": "h",
                                    "yanchor": "top"
                                },
                                margin = {
                                    "r": 0,
                                    "t": 20,
                                    "b": 10,
                                    "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 700,
                                xaxis = {
                                    "autorange": True,
                                    "range": [-0.5, 4.5],
                                    "showline": True,
                                    "title": "",
                                    "type": "category"
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="twelve columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")


if __name__ == '__main__':
    app.run_server(debug=True)

                # html.Div([
                #     html.H6("Hypothetical growth of $10,000",
                #             className="gs-header gs-table-header padded"),
                #     dcc.Graph(
                #         id="graph-2",
                #         figure={
                #             'data': [
                #                 go.Scatter(
                #                     x = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"],
                #                     y = ["10000", "7500", "9000", "10000", "10500", "11000", "14000", "18000", "19000", "20500", "24000"],
                #                     line = {"color": "rgb(53, 83, 255)"},
                #                     mode = "lines",
                #                     name = "500 Index Fund Inv"
                #                 )
                #             ],
                #             'layout': go.Layout(
                #                 autosize = False,
                #                 title = "",
                #                 font = {
                #                     "family": "Raleway",
                #                     "size": 10
                #                 },
                #                 height = 200,
                #                 width = 340,
                #                 hovermode = "closest",
                #                 legend = {
                #                     "x": -0.0277108433735,
                #                     "y": -0.142606516291,
                #                     "orientation": "h"
                #                 },
                #                 margin = {
                #                     "r": 20,
                #                     "t": 20,
                #                     "b": 20,
                #                     "l": 50
                #                 },
                #                 showlegend = True,
                #                 xaxis = {
                #                     "autorange": True,
                #                     "linecolor": "rgb(0, 0, 0)",
                #                     "linewidth": 1,
                #                     "range": [2008, 2018],
                #                     "showgrid": False,
                #                     "showline": True,
                #                     "title": "",
                #                     "type": "linear"
                #                 },
                #                 yaxis = {
                #                     "autorange": False,
                #                     "gridcolor": "rgba(127, 127, 127, 0.2)",
                #                     "mirror": False,
                #                     "nticks": 4,
                #                     "range": [0, 30000],
                #                     "showgrid": True,
                #                     "showline": True,
                #                     "ticklen": 10,
                #                     "ticks": "outside",
                #                     "title": "$",
                #                     "type": "linear",
                #                     "zeroline": False,
                #                     "zerolinewidth": 4
                #                 }
                #             )
                #         },
                #         config={
                #             'displayModeBar': False
                #         }
                #     )
                # ], className="six columns"),

    #         # Row 5

    #         html.Div([

    #             html.Div([
    #                 html.H6('Price & Performance (%)',
    #                         className="gs-header gs-table-header padded"),
    #                 html.Table(make_dash_table(df_items_purchased_head))
    #             ], className="six columns"),

    #             html.Div([
    #                 html.H6("Risk Potential",
    #                         className="gs-header gs-table-header padded"),
    #                 dcc.Graph(
    #                     id='graph-3',
    #                     figure = {
    #                         'data': [
    #                             go.Scatter(
    #                                 x = ["0", "0.18", "0.18", "0"],
    #                                 y = ["0.2", "0.2", "0.4", "0.2"],
    #                                 fill = "tozerox",
    #                                 fillcolor = "rgba(31, 119, 180, 0.2)",
    #                                 hoverinfo = "none",
    #                                 line = {"width": 0},
    #                                 mode = "lines",
    #                                 name = "B",
    #                                 showlegend = False
    #                             ),
    #                             go.Scatter(
    #                                 x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
    #                                 y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
    #                                 fill = "tozerox",
    #                                 fillcolor = "rgba(31, 119, 180, 0.4)",
    #                                 hoverinfo = "none",
    #                                 line = {"width": 0},
    #                                 mode = "lines",
    #                                 name = "D",
    #                                 showlegend = False
    #                             ),
    #                             go.Scatter(
    #                                 x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
    #                                 y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
    #                                 fill = "tozerox",
    #                                 fillcolor = "rgba(31, 119, 180, 0.6)",
    #                                 hoverinfo = "none",
    #                                 line = {"width": 0},
    #                                 mode = "lines",
    #                                 name = "F",
    #                                 showlegend = False
    #                             ),
    #                             go.Scatter(
    #                                 x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
    #                                 y = ["0.2", "0.2", "1", "0.8", "0.2"],
    #                                 fill = "tozerox",
    #                                 fillcolor = "rgb(31, 119, 180)",
    #                                 hoverinfo = "none",
    #                                 line = {"width": 0},
    #                                 mode = "lines",
    #                                 name = "H",
    #                                 showlegend = False
    #                             ),
    #                             go.Scatter(
    #                                 x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
    #                                 y = ["0.2", "0.2", "1.2", "1", "0.2"],
    #                                 fill = "tozerox",
    #                                 fillcolor = "rgba(31, 119, 180, 0.8)",
    #                                 hoverinfo = "none",
    #                                 line = {"width": 0},
    #                                 mode = "lines",
    #                                 name = "J",
    #                                 showlegend = False
    #                             ),
    #                         ],
    #                         'layout': go.Layout(
    #                             title = "",
    #                             annotations = [
    #                                 {
    #                                   "x": 0.69,
    #                                   "y": 0.6,
    #                                   "font": {
    #                                     "color": "rgb(31, 119, 180)",
    #                                     "family": "Raleway",
    #                                     "size": 30
    #                                   },
    #                                   "showarrow": False,
    #                                   "text": "<b>4</b>",
    #                                   "xref": "x",
    #                                   "yref": "y"
    #                                 },
    #                                 {
    #                                   "x": 0.0631034482759,
    #                                   "y": -0.04,
    #                                   "align": "left",
    #                                   "font": {
    #                                     "color": "rgb(44, 160, 44)",
    #                                     "family": "Raleway",
    #                                     "size": 10
    #                                   },
    #                                   "showarrow": False,
    #                                   "text": "<b>Less risk<br>Less reward</b>",
    #                                   "xref": "x",
    #                                   "yref": "y"
    #                                 },
    #                                 {
    #                                   "x": 0.92125,
    #                                   "y": -0.04,
    #                                   "align": "right",
    #                                   "font": {
    #                                     "color": "rgb(214, 39, 40)",
    #                                     "family": "Raleway",
    #                                     "size": 10
    #                                   },
    #                                   "showarrow": False,
    #                                   "text": "<b>More risk<br>More reward</b>",
    #                                   "xref": "x",
    #                                   "yref": "y"
    #                                 }
    #                               ],
    #                               autosize = False,
    #                               height = 200,
    #                               width = 340,
    #                               hovermode = "closest",
    #                               margin = {
    #                                 "r": 10,
    #                                 "t": 20,
    #                                 "b": 80,
    #                                 "l": 10
    #                               },
    #                               shapes = [
    #                                 {
    #                                   "fillcolor": "rgb(255, 255, 255)",
    #                                   "line": {
    #                                     "color": "rgb(31, 119, 180)",
    #                                     "width": 4
    #                                   },
    #                                   "opacity": 1,
    #                                   "type": "circle",
    #                                   "x0": 0.621,
    #                                   "x1": 0.764,
    #                                   "xref": "x",
    #                                   "y0": 0.135238095238,
    #                                   "y1": 0.98619047619,
    #                                   "yref": "y"
    #                                 }
    #                               ],
    #                               showlegend = True,
    #                               xaxis = {
    #                                 "autorange": False,
    #                                 "fixedrange": True,
    #                                 "range": [-0.05, 1.05],
    #                                 "showgrid": False,
    #                                 "showticklabels": False,
    #                                 "title": "<br>",
    #                                 "type": "linear",
    #                                 "zeroline": False
    #                               },
    #                               yaxis = {
    #                                 "autorange": False,
    #                                 "fixedrange": True,
    #                                 "range": [-0.3, 1.6],
    #                                 "showgrid": False,
    #                                 "showticklabels": False,
    #                                 "title": "<br>",
    #                                 "type": "linear",
    #                                 "zeroline": False
    #                             }
    #                         )
    #                     },
    #                     config={
    #                         'displayModeBar': False
    #                     }
    #                 )
    #             ], className="six columns"),