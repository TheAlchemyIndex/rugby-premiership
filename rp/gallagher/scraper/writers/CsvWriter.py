import csv


# Function for writing data to csv file
def write_to_csv(results, file_name, field_names, write_type):
    with open(file_name, write_type, encoding='utf-8-sig', newline='') as f:
        # If write_type is not a then individual files are created for each season
        if write_type != "a":
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(results)
        # Otherwise data for all seasons is written to a single file
        else:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writerows(results)
