import csv

processed_info = []

with open("unformatted_sister_info.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            sister_info = {
                "common_name": "",
                "last_name": "",
                "baptism_name": "",
                "religious_name": "",
                "occupations": "",
                "locations": ""
            }
            idx = 0

            while idx < len(row):
                if len(row[idx]) > 1:
                    if idx == 0:
                        sister_info["common_name"] = row[idx]
                    elif idx == 1:
                        sister_info["last_name"] = row[idx]
                    elif idx == 2:
                        sister_info["baptism_name"] = row[idx]
                    elif idx == 3:
                        sister_info["religious_name"] = row[idx]
                    elif idx >= 4 and idx <= 19:
                        if len(row[idx + 1]) > 1:
                            sister_info["occupations"] += f"{row[idx]} \n"
                        else:
                            sister_info["occupations"] += f"{row[idx]}"
                    elif idx >= 20:
                        location = ""
                        if row[idx].count(",") > 1:
                            location = row[idx].replace(",", " in", 1)
                        else:
                            location = row[idx]

                        if idx + 1 < len(row) - 1 and len(row[idx + 1]) > 1:
                            sister_info["locations"] += f"{location} \n"
                        else:
                            sister_info["locations"] += f"{location}"
                idx += 1

            sister_copy = sister_info.copy()
            processed_info.append(sister_copy)
            line_count += 1

with open("processed_sister_info.csv", mode="w", newline='', encoding="utf-8") as csv_file:
    fieldnames = ["common_name", "last_name", "baptism_name", "religious_name", "occupations", "locations"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

    writer.writeheader()
    idx = 0

    while idx < len(processed_info):
        writer.writerow(processed_info[idx])
        idx += 1
