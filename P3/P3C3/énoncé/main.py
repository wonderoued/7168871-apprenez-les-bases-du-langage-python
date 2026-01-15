# Écrivez votre code ici !
import csv


def extract(filename="input.csv"):
    data = []
    with open(filename, "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
    return data


def transform(data_to_transform):
    data_to_load = []
    for data in data_to_transform:
        transform_data = {}
        transform_data["nom"] = data["nom"]
        transform_data["salaire"] = int(data["heures_travaillees"]) * 15
        data_to_load.append(transform_data)
    return data_to_load


def load(data_to_load, filename="output.csv"):
    with open(filename, "w") as file:
        fieldname = ["nom", "salaire"]
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        for data in data_to_load:
            writer.writerow(data)


def main():
    data_to_transform = extract("input.csv")
    data_to_load = transform(data_to_transform)
    load(data_to_load, "output.csv")


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
