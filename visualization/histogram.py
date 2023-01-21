import numpy as np
import matplotlib.pyplot as plt
from read import read_file


# Histogram
def histogram (filename : str):
    df = read_file(filename)

    _, axes = plt.subplots(nrows=3, ncols=5)
    
    for ax, clss in zip(axes.flatten()[:13], ['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying']):
        ax.title.set_text(clss)
        for house, color in [("Gryffindor", "firebrick"), ("Slytherin", "lime"), ("Ravenclaw", "royalblue"), ("Hufflepuff", "gold")]:
            ax.hist(df.loc[df['Hogwarts House'] == house, clss].replace('', np.nan).dropna().astype(float), color=color, alpha=0.75)

    plt.show()

if __name__ == "__main__":
    histogram("../datasets/dataset_train.csv")