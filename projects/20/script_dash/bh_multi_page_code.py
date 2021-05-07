import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output
from dash_table import DataTable

import plotly.graph_objects as go
import numpy as np
import sys

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.

#df = pd.read_csv('corr_rhino_taxonomy.csv', header=0)
df = pd.read_csv('corr_ALL_METADATA_rhinolophus_taxonomy.csv', header=0)

# re-order df columns
# ,SpeciesName,NCBI_TaxID,accession,author,journal,gene,country,specimen_voucher,phylum,class_name,order,family,genus,species
df = df[['SpeciesName','NCBI_TaxID','accession','gene','country','specimen_voucher','phylum','class_name','order','family','genus','species','journal','author']]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Summary', href='/page-1'),
    html.Br(),
    dcc.Link('World map visualization', href='/page-2'),
])



# define level
species_indicators = df['species'].unique()
genus_indicators = df['genus'].unique()
family_indicators = df['family'].unique()
order_indicators = df['order'].unique()
class_indicators = df['class_name'].unique()
phylum_indicators = df['phylum'].unique()
# set layout
page_1_layout  = html.Div([

    html.H1('Summary'),
    html.H2('Select filters to apply:'),

    html.Div([

        html.Label('Phylum'),
        dcc.Dropdown(
            id = 'phylum-column',
            options = [{'label': i, 'value': i} for i in phylum_indicators])

    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Class'),
        dcc.Dropdown(
            id = 'class-column',
            options = [{'label': i, 'value': i} for i in class_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Order'),
        dcc.Dropdown(
            id = 'order-column',
            options = [{'label': i, 'value': i} for i in order_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Family'),
        dcc.Dropdown(
            id = 'family-column',
            options = [{'label': i, 'value': i} for i in family_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Genus'),
        dcc.Dropdown(
            id = 'genus-column',
            options = [{'label': i, 'value': i} for i in genus_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Species'),
        dcc.Dropdown(
            id = 'species-column',
            options = [{'label': i, 'value': i} for i in species_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),



    html.Br(),
    html.Br(),

    # tabella vuota
    html.H3('Unique values:'),

    html.Table([
        html.Tr([html.Td('TaxIDs'), html.Td(id='taxids')]),
        html.Tr([html.Td('Accessions'), html.Td(id='accession')]),
        html.Tr([html.Td('Genes'), html.Td(id='gene')]),
        html.Tr([html.Td('Countries'), html.Td(id='country')]),
        html.Tr([html.Td('Specimen vouchers'), html.Td(id='specimen_voucher')])]),

    html.Br(),

    html.H3('Filtered table:'),
    html.Div([
        DataTable(
            id='table',
            data=[],
            page_size = 10,
            style_table={'overflowX': 'auto'}
        )
    ]),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('World map visualization', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

# popolamento tabella con dropdown
@app.callback(
    [Output('taxids', 'children'),
     Output('accession', 'children'),
     Output('gene', 'children'),
     Output('country', 'children'),
     Output('specimen_voucher', 'children'),
     Output("table", "data"), Output('table', 'columns')],
    [Input('phylum-column', 'value'),
     Input('class-column', 'value'),
     Input('order-column', 'value'),
     Input('family-column', 'value'),
     Input('genus-column', 'value'),
     Input('species-column', 'value')]
)

def output_count_values(phylum_column, class_column, order_column,
                        family_column, genus_column, species_column):

    filtered_df = df

    if phylum_column != None:
        filtered_df = filtered_df[filtered_df['phylum'] == phylum_column]

    if class_column != None:
        filtered_df = filtered_df[filtered_df['class_name'] == class_column]

    if order_column != None:
        filtered_df = filtered_df[filtered_df['order'] == order_column]

    if family_column != None:
        filtered_df = filtered_df[filtered_df['family'] == family_column]

    if genus_column != None:
        filtered_df = filtered_df[filtered_df['genus'] == genus_column]

    if species_column != None:
        filtered_df = filtered_df[filtered_df['species'] == species_column]

    #counts_output = filtered_df.count()


    if phylum_column == None and class_column == None and order_column == None and family_column == None and genus_column == None and species_column == None:
        columns = [{'name': i, 'id': i} for i in df.columns]
        return 0, 0, 0, 0, 0, df.to_dict('records'), columns
    else:

        columns = [{'name': i, 'id': i} for i in filtered_df.columns]

        #return counts_output[2], counts_output[3], counts_output[6], counts_output[7], counts_output[8], filtered_df.to_dict('records'), columns
        return filtered_df['NCBI_TaxID'].nunique(), filtered_df['accession'].nunique(), filtered_df['gene'].nunique(), filtered_df['country'].nunique(), filtered_df['specimen_voucher'].nunique(), filtered_df.to_dict('records'), columns


page_2_layout = html.Div([
    html.H1('World map visualization'),
    html.H2('Select filters to apply:'),
    html.Div([

        html.Label('Phylum'),
        dcc.Dropdown(
            id = 'phylum-column',
            options = [{'label': i, 'value': i} for i in phylum_indicators])

    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Class'),
        dcc.Dropdown(
            id = 'class-column',
            options = [{'label': i, 'value': i} for i in class_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Order'),
        dcc.Dropdown(
            id = 'order-column',
            options = [{'label': i, 'value': i} for i in order_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Family'),
        dcc.Dropdown(
            id = 'family-column',
            options = [{'label': i, 'value': i} for i in family_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Genus'),
        dcc.Dropdown(
            id = 'genus-column',
            options = [{'label': i, 'value': i} for i in genus_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.Div([
        html.Label('Species'),
        dcc.Dropdown(
            id = 'species-column',
            options = [{'label': i, 'value': i} for i in species_indicators])
    ], style={'width': '30%', 'display': 'inline-block', 'padding': 2}),

    html.H2('Geographical heatmap'),
    html.Div([dcc.Graph(id = 'Heatmap-accessions',
                        figure = {"layout": {
                                    "title": "My Dash Graph",
                                    "height": 700  # px
                                    }
                                }
    )]),

    html.Br(),
    html.Br(),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Summary', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(
    [Output('Heatmap-accessions','figure')],
    [Input('phylum-column', 'value'),
     Input('class-column', 'value'),
     Input('order-column', 'value'),
     Input('family-column', 'value'),
     Input('genus-column', 'value'),
     Input('species-column', 'value')])

def update_figure(phylum_column, class_column, order_column,
                  family_column, genus_column, species_column):

    df2 = df
    df2['frequency'] = 1
    groupByColumns = ['phylum', 'country']

    if phylum_column != None:
        groupByColumns = ['phylum', 'country']
        df2 = df2[df2['phylum'] == phylum_column]

    if class_column != None:
        groupByColumns = ['class_name', 'country']
        df2 = df2[df2['class_name'] == class_column]

    if order_column != None:
        groupByColumns = ['order', 'country']
        df2 = df2[df2['order'] == order_column]

    if family_column != None:
        groupByColumns = ['family', 'country']
        df2 = df2[df2['family'] == family_column]

    if genus_column != None:
        groupByColumns = ['genus', 'country']
        df2 = df2[df2['genus'] == genus_column]

    if species_column != None:
        groupByColumns = ['species', 'country']
        df2 = df2[df2['species'] == species_column]

    df2 = df2.groupby(groupByColumns).agg({'frequency': sum}).reset_index()

    df2['frequency'] = np.log(df2['frequency'])
    df2['country'] = df2['country'].astype(str)
    # df1 = df1[df1['species'] == species_column]

    # df1 = df.copy()
    # df1 = df1.groupby(['species','country']).agg({'frequency': sum}) # add groupby
    # df1.reset_index(level=0, inplace=True)
    # df1['frequency'] = np.log(df1['frequency'])
    # df1 = df1[df1['species'] == species_column]


    #plotly heatmap
    fig = go.Figure(data=go.Choropleth(
        locationmode= 'country names',
        locations=df2['country'], #
        z=df2['frequency'], #
        colorscale='Viridis',
        marker_line_color='white',
        marker_line_width=0.5
    ))

    # fig.update_layout(
    #     title_text='Accessions Distribution',
    #     title_x=0.5,
    #     geo=dict(
    #         showframe=False,
    #         showcoastlines=False,
    #         projection_type='natural earth'
    #     ),
    #)


    return [fig]

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)
