import matplotlib.pyplot as plt
from read import read_file


# Scatter plot
def scatter_plot (filename : str):
    SIZE = 13
    df = read_file(filename)

    _, axes = plt.subplots(nrows=SIZE, ncols=SIZE)

    ax = axes.flatten()
    classes = ['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying']

    for i, classx in enumerate(classes):
        for j, classy in enumerate(classes):
            dfc = df[(df[classx] != '') & (df[classy] != '')]
            x = dfc[classx].astype(float)
            y = dfc[classy].astype(float)
            ax = axes.flatten()[i * SIZE + j]

            ax.scatter(x, y)
            ax.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
            if i == 0:
                ax.title.set_text(classy)
            if j == 0:
                ax.set_ylabel(classx, rotation=90, fontsize=6)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    scatter_plot("../datasets/dataset_train.csv")