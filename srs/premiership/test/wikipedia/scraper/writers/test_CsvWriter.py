import os
import pathlib
import shutil
import unittest

from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.constants.matchData import TeamTypes
from srs.premiership.main.wikipedia.scraper.writers.CsvWriter import write_to_csv

valid_match_data = [{OriginalColumns.DATE: "26/02/2023",
                     OriginalColumns.TIME: "19:45",
                     OriginalColumns.TEAM1_NAME: "Team1 Name",
                     OriginalColumns.TEAM1_POINTS: "30",
                     OriginalColumns.TEAM2_NAME: "Team2 Name",
                     OriginalColumns.TEAM2_POINTS: "20",
                     OriginalColumns.VENUE: "Test Venue",
                     OriginalColumns.TEAM_TYPE: TeamTypes.HOME,
                     OriginalColumns.REFEREE: "Test Referee",
                     OriginalColumns.TOTAL_POINTS: "50",
                     OriginalColumns.RESULT: "W",
                     OriginalColumns.EXTRA_TIME: "N",
                     OriginalColumns.HOUR: "19",
                     OriginalColumns.DAY: "Sun",
                     OriginalColumns.MONTH: "Feb",
                     OriginalColumns.YEAR: "2023",
                     OriginalColumns.SEASON: "2022-23",
                     OriginalColumns.TEAM1_BPS: "1",
                     OriginalColumns.TEAM2_BPS: "0",
                     OriginalColumns.TEAM1_TRIES: "4",
                     OriginalColumns.TEAM1_CONVERSIONS: "2",
                     OriginalColumns.TEAM1_PENALTIES: "2",
                     OriginalColumns.TEAM1_DROP_GOALS: "0",
                     OriginalColumns.TEAM2_TRIES: "3",
                     OriginalColumns.TEAM2_CONVERSIONS: "1",
                     OriginalColumns.TEAM2_PENALTIES: "1",
                     OriginalColumns.TEAM2_DROP_GOALS: "0"}]

valid_field_names = [OriginalColumns.DATE,
                     OriginalColumns.TIME,
                     OriginalColumns.TEAM1_NAME,
                     OriginalColumns.TEAM1_POINTS,
                     OriginalColumns.TEAM2_NAME,
                     OriginalColumns.TEAM2_POINTS,
                     OriginalColumns.VENUE,
                     OriginalColumns.TEAM_TYPE,
                     OriginalColumns.REFEREE,
                     OriginalColumns.TOTAL_POINTS,
                     OriginalColumns.RESULT,
                     OriginalColumns.EXTRA_TIME,
                     OriginalColumns.HOUR,
                     OriginalColumns.DAY,
                     OriginalColumns.MONTH,
                     OriginalColumns.YEAR,
                     OriginalColumns.SEASON,
                     OriginalColumns.TEAM1_BPS,
                     OriginalColumns.TEAM2_BPS,
                     OriginalColumns.TEAM1_TRIES,
                     OriginalColumns.TEAM1_CONVERSIONS,
                     OriginalColumns.TEAM1_PENALTIES,
                     OriginalColumns.TEAM1_DROP_GOALS,
                     OriginalColumns.TEAM2_TRIES,
                     OriginalColumns.TEAM2_CONVERSIONS,
                     OriginalColumns.TEAM2_PENALTIES,
                     OriginalColumns.TEAM2_DROP_GOALS]

parent_path: str = str(pathlib.Path(__file__).resolve().parent.parent.parent.parent)
valid_file = f"{parent_path}/resources/valid_test_data.csv"
expected_file = f"{parent_path}/resources/expected_test_data.csv"

valid_file_appended = f"{parent_path}/resources/valid_test_data_appended.csv"
expected_file_appended = f"{parent_path}/resources/expected_test_data_appended.csv"


class CsvWriterTest(unittest.TestCase):
    def test_csv_writer_new_file(self):
        write_to_csv(valid_match_data, valid_file, valid_field_names, "w")

        with open(valid_file, 'r') as open_written_file, open(expected_file, 'r') as open_expected_file:
            read_written_file = open_written_file.readlines()
            read_expected_file = open_expected_file.readlines()

        self.assertEqual(
            read_written_file, read_expected_file
        )

        if os.path.exists(valid_file) and os.path.isfile(valid_file):
            os.remove(valid_file)

    def test_csv_writer_append_to_file(self):
        shutil.copy(expected_file, valid_file_appended)
        write_to_csv(valid_match_data, valid_file_appended, valid_field_names, "a")

        with open(valid_file_appended, 'r') as open_written_file,\
                open(expected_file_appended, 'r') as open_expected_file:
            read_written_file = open_written_file.readlines()
            read_expected_file = open_expected_file.readlines()

        self.assertEqual(
            read_written_file, read_expected_file
        )

        if os.path.exists(valid_file_appended) and os.path.isfile(valid_file_appended):
            os.remove(valid_file_appended)


if __name__ == '__main__':
    unittest.main()
