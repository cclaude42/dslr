import sys, csv, math
import pandas as pd
import numpy as np

def is_float(element: any) -> bool:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def percentile (data : pd.DataFrame, percentile : float) -> float:
    # print(f"p {percentile} -> {(data.size - 1) * percentile}")
    i = float(percentile * (data.size - 1))
    if i.is_integer():
        return data.iloc[int(i)]
    else:
        print(i, 1 - i % 1, i % 1, math.floor(i), math.ceil(i), data.iloc[math.floor(i)], data.iloc[math.ceil(i)], data.iloc[math.floor(i)] * (1 - i % 1) + data.iloc[math.ceil(i)] * (i % i))
    return 0




def read_file (filename : str) -> pd.DataFrame:
    with open(filename) as csvfile:
        csvdata = csv.reader(csvfile)
        df = pd.DataFrame(csvdata)
        df.columns = df.iloc[0]
        df = df[1:]
        return df
    return None

# def normalize (df : pd.DataFrame) -> pd.DataFrame:
#     normalized = pd.DataFrame()
#     for col in df:
#         if is_float(df[col].iloc[0]):
#             print(df[col].replace('', np.nan).dropna().size)
#             normalized[col] = df[col].replace('', np.nan).dropna()
#             print("normed", normalized[col].size)
#     # print(normalized)
#     return normalized

def analyze_feature (feature : pd.DataFrame) -> dict:
    feature = feature.replace('', np.nan).dropna().astype(float).sort_values()
    print(feature)
    return {
        "name": feature.name,
        "count": feature.size,
        "mean": 0 / feature.size,
        "std": 0,
        "min": percentile(feature, 0),
        "lower": percentile(feature, 0.25),
        "median": percentile(feature, 0.5),
        "upper": percentile(feature, 0.75),
        "max": percentile(feature, 1),
    }


def describe (filename : str):
    descriptions = []

    df = read_file(filename)
    # df = normalize(df)
    descriptions = [analyze_feature(df[col]) for col in df if is_float(df[col].iloc[0]) and df[col].name == "Arithmancy"]

    # print(pd.DataFrame.describe(df.astype(float)))
    print(descriptions)

def main ():
    if len(sys.argv) > 1:
        describe(sys.argv[1])
    else:
        print("Please provide a CSV file to read :", file=sys.stderr)
        print("    python3 describe.py filename.csv", file=sys.stderr)


if __name__ == "__main__":
    main()