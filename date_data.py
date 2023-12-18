import csv
import time


def file_cut_date_and_data(path: str) -> None:
    """Open .csv file from path and fill "1/" folder with 2 files : DATA and DATE

    Args:
        path (str): path to file to cut
    """
    date = []
    data = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            date.append([row[0]])
            data.append([row[i] for i in range(1, 9)])
    with open("1/X.csv", "w", encoding="utf-8", newline="") as file_x:
        writer = csv.writer(file_x)
        writer.writerows(date)
    with open("1/Y.csv", "w", encoding="utf-8", newline="") as file_y:
        writer = csv.writer(file_y)
        writer.writerows(data)
    print("end")


def main() -> None:
    file_cut_date_and_data("dataset.csv")


if __name__ == '__main__':
    main()
