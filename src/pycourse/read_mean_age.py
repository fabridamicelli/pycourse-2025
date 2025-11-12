import pandas as pd


def get_age_mean(df):
    mean_age_inner = df["age"].mean().roundd(2)
    return mean_age_inner


def main():
    data = pd.read_csv("./data/participants.tsv", sep="\t")
    mean_age = get_age_mean(data)
    print("The mean age is", mean_age)

if __name__ == "__main__":
    main()
