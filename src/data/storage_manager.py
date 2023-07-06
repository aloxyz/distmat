from utils.data_utils import data_path
from utils.dict_utils import csv_to_dict
import csv


def store_data(filename, data_model):
    with open(data_path(filename + '.csv'), "w", newline="") as fq:
        writer = csv.writer(fq)
        writer.writerow(['Run type:', filename.capitalize()])

        for op, time in data_model.items():
            writer.writerow([op, time])

        fq.close()


def load_data(filename):
    with open(data_path(filename + '.csv'), 'w', newline="") as fq:
        data = csv_to_dict(csv_to_dict(list(csv.DictReader(fq))))

        return data
