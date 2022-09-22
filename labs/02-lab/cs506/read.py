import csv


def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    with open(csv_file_path, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

    #raise NotImplementedError()
