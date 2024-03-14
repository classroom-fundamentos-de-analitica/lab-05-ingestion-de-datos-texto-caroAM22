import os
import csv
import pandas as pd


def create_train_dataset():
    folder_path = "data/train"
    output_file = "train_dataset.csv"
    folders = ["negative", "positive", "neutral"]
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["phrase", "sentiment"])
    for folder in folders:
        folder_path = "data/train/" + folder
        with open(output_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, "r") as file:
                        content = file.read()
                        writer.writerow([content, folder])
    return output_file


def create_test_dataset():
    folder_path = "data/test"
    output_file = "test_dataset.csv"
    folders = ["negative", "positive", "neutral"]
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["phrase", "sentiment"])
    for folder in folders:
        folder_path = "data/test/" + folder
        with open(output_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, "r") as file:
                        content = file.read()
                        writer.writerow([content, folder])
    return output_file


create_train_dataset()
create_test_dataset()
