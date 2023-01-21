import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from read import read_file


# Pair plot
def pair_plot (filename : str):
    SIZE = 13
    df = read_file(filename)

    df = df[['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying']].replace('', np.nan).astype(float)

    sns.pairplot(df)

    plt.show()

if __name__ == "__main__":
    pair_plot("../datasets/dataset_train.csv")