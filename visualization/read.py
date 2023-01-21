import csv
import pandas as pd


def read_file (filename : str) -> pd.DataFrame:
    with open(filename) as csvfile:
        csvdata = csv.reader(csvfile)
        df = pd.DataFrame(csvdata)
        df.columns = df.iloc[0]
        df = df[1:]
        return df