import sys, csv

def describe (name):
    with open(name) as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(', '.join(row))

def main ():
    if len(sys.argv) > 1:
        describe(sys.argv[1])
    else:
        print("Please provide a CSV file to read :", file=sys.stderr)
        print("    python3 describe.py filename.csv", file=sys.stderr)


if __name__ == "__main__":
    main()