import csv
import os

def checkExistValInFile(file_path, value): 
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if value in row:
                file.close()
                return True
        file.close()
        return False


def appendValInFile(file_path, value):
    with open(file_path,'a+', newline='') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow([value])

