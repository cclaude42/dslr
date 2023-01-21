import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Utils
def read_file (filename : str) -> pd.DataFrame:
    with open(filename) as csvfile:
        csvdata = csv.reader(csvfile)
        df = pd.DataFrame(csvdata)
        df.columns = df.iloc[0]
        df = df[1:]
        return df


# Histogram
def histogram (filename : str):
    df = read_file(filename)

    _, axes = plt.subplots(nrows=3, ncols=5)
    
    for ax, clss in zip(axes.flatten()[:13], ['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying']):
        ax.title.set_text(clss)
        for house, color in [("Gryffindor", "firebrick"), ("Slytherin", "lime"), ("Ravenclaw", "royalblue"), ("Hufflepuff", "gold")]:
            ax.hist(df.loc[df['Hogwarts House'] == house, clss].replace('', np.nan).dropna().astype(float), color=color, alpha=0.75)

    plt.show()


def main ():
    histogram("../datasets/dataset_train.csv")


if __name__ == "__main__":
    main()