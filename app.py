import os
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output



script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'allchapters.csv')
allchapters = pd.read_csv(csv_path)



# Load sentiment for the individual chapters broken down by paragraphs
folder_path = os.path.join(script_dir, 'chapter_paragraphs')
chapter_dfs = {}  # Load all individual chapter DataFrames dynamically
for i in range(1, 59):
    file_name = f'chapter_{i}_paragraphs.csv'
    file_path = os.path.join(folder_path, file_name)
    chapter_dfs[f'chp{i}'] = pd.read_csv(file_path)

# Initialize Dash app
app = dash.Dash(__name__)

# Create the main line plot for 'allchapters'
main_fig = px.line(
    allchapters, 
    x='Chapter Number', 
    y='Average Compound Score', 
    markers=True, 
    title="<i>The Shining</i><br>Sentiment Breakdown by Chapter"
)

# Add hover info
main_fig.update_traces(
    hovertemplate='Chapter: %{x}<br>Score: %{y}<br>Sentiment: %{customdata}<extra></extra>',
    customdata=allchapters['Sentiment']
)

# Marker/line colors
main_fig.update_traces(
    line=dict(color='#D36D6D'),  # Set line color to a much lighter red
    marker=dict(
        color='#800020',  # Set marker color to burgundy
    )
)

# Configuring x-axis
main_fig.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=allchapters['Chapter Number'].unique(),
        range=[allchapters['Chapter Number'].min(), allchapters['Chapter Number'].max()],
        tickangle=-45,
        tickfont=dict(size=12, family='Arial', weight='bold'),
    ),
    shapes=[dict(
        type='line',
        x0=allchapters['Chapter Number'].min(),
        x1=allchapters['Chapter Number'].max(),
        y0=0,
        y1=0,
        line=dict(
            color='black',
            width=1.5,
            dash='solid'
        )
    )],
    plot_bgcolor='#f5f5f5',
    width=1200,
    title=dict(
        x=0.5,
        xanchor='center',
        yanchor='top',
    )
)

# Layout of the app
app.layout = html.Div([
    dcc.Graph(id='main-graph', figure=main_fig, style={'width': '1200px'}),
    dcc.Graph(id='detail-graph', style={'width': '1200px'})
])

# Callback to update the detailed graph when clicking a chapter in the main graph
@app.callback(
    Output('detail-graph', 'figure'),
    Input('main-graph', 'clickData')
)
def update_detail_graph(click_data):
    if click_data:
        chapter_num = click_data['points'][0]['x']
        ch_df = chapter_dfs.get(f'chp{int(chapter_num)}', pd.DataFrame())

        if not ch_df.empty:
            detail_fig = px.line(
                ch_df,
                x='Paragraph Number',
                y='Compound Score',
                markers=True,
                title=f"Sentiment Breakdown for Chapter: {int(chapter_num)}"
            )

            detail_fig.update_traces(
                hovertemplate='Paragraph: %{x}<br>Score: %{y}<br>Sentiment: %{customdata}<extra></extra>',
                customdata=ch_df['Classification']
            )

            detail_fig.update_traces(
                line=dict(color='#D36D6D'),
                marker=dict(color='#800020')
            )

            detail_fig.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=ch_df['Paragraph Number'].unique(),
                    tickangle=-45,
                    tickfont=dict(size=12, family='Arial', weight='bold'),
                    range=[ch_df['Paragraph Number'].min(), ch_df['Paragraph Number'].max()]
                ),
                shapes=[dict(
                    type='line',
                    x0=ch_df['Paragraph Number'].min(),
                    x1=ch_df['Paragraph Number'].max(),
                    y0=0,
                    y1=0,
                    line=dict(
                        color='black',
                        width=1.5,
                        dash='solid'
                    )
                )],
                plot_bgcolor='#f5f5f5',
                width=1200,
                height=500,
                title=dict(
                    x=0.5,
                    xanchor='center',
                    yanchor='top',
                )
            )

            return detail_fig
    return {}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
