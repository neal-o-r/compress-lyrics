import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, Div


def bokeh_plot(df):

    output_file("html/plot.html", title="Billboard Top 100 Song Lyrics 1964-2015")
    df['Colour'] = "olive"
    df['Alpha'] = [0.8] * len(df)

    desc = Div(text=open("html/description.html", 'r').read(), width=800)
    source = ColumnDataSource(data=dict(x=[],
            y=[], artist=[], colour=[], song=[], year=[], alpha=[]))

    source.data = dict(
                    y=df['Ratio'],
                    x=df['Year'],
                    artist=df['Artist'],
                    colour=df['Colour'],
                    song=df["Song"],
                    year=df["Year"],
                    alpha=df["Alpha"],
            )

    hover = HoverTool(tooltips=[
        ("Title", "@song"),
        ("Artist", "@artist"),
        ("Year", "@year"),
    ])


    title = "%d songs selected"%len(df)

    p = figure(plot_width=1200, plot_height=800,
            title=title, toolbar_location="below", tools=[hover])


    p.circle(x='x', y='y', size=7, color='colour', source=source, line_color=None, fill_alpha='alpha')

    p.yaxis.axis_label = "Lyrics Compression Ratio"
    p.xaxis.axis_label = "Year"

    show(p)
