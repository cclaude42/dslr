#%%
import sys, csv, math
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
    return None

# Histogram
def histogram (filename : str):
    df = read_file(filename)

    # fig, axes = plt.subplots(nrows=3, ncols=5)
    
    # for ax, legend in zip(axes.flatten()[:13], ['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying']):
    #     ax.plot(range(10), 'r')
    #     print(legend)

    # print(df.loc[df['Hogwarts House'] == 'Slytherin', 'Arithmancy'])

    plt.hist([1, 2, 3, 4, 5, 18, 2, 40, 36, 34, 42, 23, 31])

    # plt.title('About as simple as it gets, folks')
    plt.show()

def main ():
    histogram("../datasets/dataset_train.csv")

if __name__ == "__main__":
    main()
# %%