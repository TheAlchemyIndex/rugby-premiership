import csv


def write_to_csv(match_data, file_name, field_names, write_type):
    """Writes data to csv file.

    :param match_data: Match data to be written to csv file
    :param file_name: The name of the file to be written to
    :param field_names: The column names to use when writing to the csv file
    :param write_type: Whether the file is being overwritten or appended to
    """
    with open(file_name, write_type, encoding='utf-8-sig', newline='') as f:
        # If write_type is not a then individual files are created for each season
        if write_type != "a":
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(match_data)
        # Otherwise data for all seasons is written to a single file
        else:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writerows(match_data)

