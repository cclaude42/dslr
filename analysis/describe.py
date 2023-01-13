import sys, csv
import pandas as pd

def is_float(element: any) -> bool:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False



def describe (name):
    with open(name) as csvfile:
        csvdata = csv.reader(csvfile)
        df = pd.DataFrame(csvdata)
        df.columns = df.iloc[0]
        df = df[1:]
        for col in df:
            if is_float(df[col].iloc[0]):
                print(df[col])

def main ():
    if len(sys.argv) > 1:
        describe(sys.argv[1])
    else:
        print("Please provide a CSV file to read :", file=sys.stderr)
        print("    python3 describe.py filename.csv", file=sys.stderr)


if __name__ == "__main__":
    main()