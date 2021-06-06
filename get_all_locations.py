import csv

locations = set()

with open("sister_locations.csv",  encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",",)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            idx = 0

            while idx < len(row):
                if len(row[idx]) > 1:
                    list_o_locations = row[idx].split(";")
                    for location in list_o_locations:
                        locations.add(location)
                idx += 1
            line_count += 1

with open("sister_locations_processed.csv", mode="w", newline="", encoding="utf-8") as location_file:
    csv_writer = csv.writer(location_file, delimiter=',', quoting=csv.QUOTE_ALL)
    idx = 0
    location_list = list(locations)
    while idx < len(locations):
        csv_writer.writerow([location_list[idx]])
        idx += 1