import csv

processed_info = []

with open("unformatted_sister_info-dash-fixed.csv", encoding="utf-8") as csv_file:
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
                "locations": "",
                "fee_id": 2
            }
            idx = 0

            while idx < len(row):
                stripped = row[idx].strip()
                if len(stripped) > 1:
                    if idx == 0:
                        common_name =  row[0].strip()
                        sister_info["common_name"] = common_name
                    elif idx == 1:
                        last_name = row[0].split(" ")
                        ln_strp = last_name[-1].strip()
                        sister_info["last_name"] = ln_strp
                    elif idx == 2:
                        baptism_name = row[idx].strip()
                        sister_info["baptism_name"] = baptism_name
                    elif idx == 3:
                        religious_name = row[idx].strip()
                        sister_info["religious_name"] = religious_name
                    elif idx >= 4 and idx <= 19:
                        occupation = row[idx].strip()
                        sister_info["occupations"] += f"{occupation},"
                    elif idx >= 20:
                        location = ""
                        if row[idx].count(",") > 1:
                            loc_strp = row[idx].strip()
                            location = loc_strp.replace(",", " in", 1)
                        else:
                            location = row[idx].strip()

                        sister_info["locations"] += f"{location};"
                idx += 1

            sister_copy = sister_info.copy()
            processed_info.append(sister_copy)
            line_count += 1

with open("processed_sister_info.csv", mode="w", newline='', encoding="utf-8") as csv_file:
    fieldnames = ["common_name", "last_name", "baptism_name", "religious_name", "occupations", "locations", "fee_id"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

    writer.writeheader()
    idx = 0

    while idx < len(processed_info):
        writer.writerow(processed_info[idx])
        idx += 1
