import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        # html.Div([
        #     html.Img(src='https://bytefoods.co/wp-content/uploads/2017/05/Byte-Foods-Logo-WHITE.png', background='black',height='40', width='160')
        # ], className="ten columns padded"),

        # html.Div([
        #     dcc.Link('Full View   ', href='/dash-vanguard-report/full-view')
        # ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Byte Foods Insights')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        html.A("Byte Foods Website", href='https://bytefoods.co/', target="_blank", className="tab first"),
        
        html.A("Byte Foods Insights Repo", href='https://github.com/tlapinsk/byte-data-insights', target="_blank", className="tab"),
        
        html.A("Dash by Plotly", href='https://plot.ly/products/dash/', target="_blank", className="tab")

    ], className="row ")
    return menu
