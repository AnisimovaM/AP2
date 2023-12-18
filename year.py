import csv
import time


def N_cut_by_year(path: str) -> None:
    """Open .csv file from path and fill "2/" folder with n files : 1 file = 1 year

    Args:
        path (str): path to file to cut
    """
    for year in range(2008, 2024):
        data = []
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if str(year) in row[0]:
                    data.append(row)
        time.sleep(0.1)
        with open(f"2/{year}-01-01-{year}-12-31.csv", "w", encoding="utf-8", newline="") as file_N:
            writer = csv.writer(file_N)
            writer.writerows(data)
        time.sleep(0.1)
    print("end")


def main() -> None:
    N_cut_by_year("dataset.csv")


if __name__ == '__main__':
    main()
