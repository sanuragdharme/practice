import csv


# Reading existing csv file and adding its content to new file
with open("names.csv", "r") as file:
    csv_reader = csv.reader(file)

    with open("new_names.csv", "w") as write_file:
        csv_write = csv.writer(write_file, delimiter="\t")
        for line in csv_reader:
            csv_write.writerow(line)


# Reading newly created csv file
with open("new_names.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="\t")
    for i in csv_reader:
        print(i)

# Reading csv using in Dict format
with open("names.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        print(i)

# Writing csv file in Dict format
with open("names.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    with open("dict_names.csv", "w") as new_file:
        fieldnames = ['FirstName', 'LastName']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
