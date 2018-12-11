import pandas as pd
import zlib
import bokeh_plot


def compress(x):
    return zlib.compress(bytes(x, 'utf8'))


if __name__ == '__main__':
    df = pd.read_csv('data/billboard.csv')
    df = df[df.Lyrics.astype(str).apply(len) > 20]
    df['Original_len'] = df.Lyrics.astype(str).apply(len)
    df['Compress_len'] = df.Lyrics.astype(str).apply(compress).apply(len)

    df['Ratio'] = df.Compress_len / df.Original_len
    bokeh_plot.bokeh_plot(df)
