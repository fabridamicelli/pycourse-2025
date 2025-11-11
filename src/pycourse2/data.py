from pathlib import Path

def fetch_data():
    filepath = Path(".") / "data" / "example-data.tsv"
    rawdata = filepath.read_text()
    return rawdata



# This block will only run when calling `python data.py`
if __name__ == "__main__":
    print("Fetching data")
    data = fetch_data()
    print(data)