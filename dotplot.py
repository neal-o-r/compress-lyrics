import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

def dotplot(df, i=None):

    if i is None:
        song = df.sample().squeeze()
    else:
        song = df.loc[i]

    l = song.Lyrics.split()

    m = np.zeros((len(l), len(l)))
    for i, l1 in enumerate(l):
        for j, l2 in enumerate(l):
            if l1 == l2:
                m[i, j] += 1


    title = f"""{song.Song} -- {song.Artist} ({song.Year})
    Chart position: {song.Rank}
    """

    plt.title(title)
    plt.imshow(m)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f"dots/{song.Song} -- {song.Artist}.png")


def all_dots(df):
    """
    for i in df.index:
        print(i)
        dotplot(df, i)
    """
    links = []
    for i, row in df.iterrows():
        links.append(f'<a href="/images/lyrics/dots/{row.Song} -- {row.Artist}.png">link</a>')

    df['Links'] = links

    save_html(df[['Song', 'Artist', 'Year', 'Links']].to_html(index=False))


def save_html(html):
    with open("songs.html", "w") as f:
        f.write(html)


if __name__ == '__main__':
    df = pd.read_csv('data/billboard.csv')
    df["Lyrics"] = df.Lyrics.astype(str)
    all_dots(df.query("Rank == 1"))


