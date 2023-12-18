import csv
import time


def N_cut_by_weak(path: str) -> None:
    """Open .csv file from path and fill "3/" folder with n files : 1 file = 1 weak

    Args:
        path (str): path to file to cut
    """
    for year in range(2008, 2024):
        for month in range(1, 13):
            for i in range(0, 5):
                with open(path, "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    data = []
                    for row in reader:
                        for day in range(1+7*i, 8+7*i):
                            if "-".join((map(lambda x: str(x).zfill(2),  list([year, month, day])))) == row[0]:
                                data.append(row)
                time.sleep(0.01)
                if len(data):
                    with open(f"3/{year}-{month}-{data[0][0][8:10]}-{year}-{month}-{data[-1][0][8:10]}.csv", "w", encoding="utf-8", newline="") as file_N:
                        writer = csv.writer(file_N)
                        writer.writerows(data)
                time.sleep(0.01)
    print("end")


def main() -> None:
    N_cut_by_weak("dataset.csv")


if __name__ == '__main__':
    main()
