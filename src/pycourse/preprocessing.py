from pycourse.data import fetch_data


def cleanup(input_data):
    lines = input_data.splitlines()
    rows = []
    for line in lines[1:]:
        row = line.split()
        rows.append(
            {
                "onset": row[0],
                "duration": row[1],
                "trial_type": row[2],
                "rewards": row[3],
            }
        )
    return rows


def preprocess_pipeline():
    data = fetch_data()
    return cleanup(data)


if __name__ == "__main__":
    print("Running preprocessing")
    out = preprocess_pipeline()
    print(out)

