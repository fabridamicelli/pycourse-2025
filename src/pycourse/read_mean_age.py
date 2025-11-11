import pandas as pd


def main():
    data = pd.read_csv("./data/participants.tsv", sep="\t")
    mean_age = data["age"].mean().round(2)
    print("The mean age is", mean_age)


if __name__ == "__main__":
    main()