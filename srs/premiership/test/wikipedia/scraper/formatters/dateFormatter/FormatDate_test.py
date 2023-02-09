from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.FormatDate import format_date


def test_format_date_valid_date():

    unformatted_date = "10 January 2023"
    expected_formatted_date = "10/Jan/2023"

    # test format_date function with valid date
    assert format_date(unformatted_date) == expected_formatted_date


def test_format_date_valid_date_missing_year():

    unformatted_date1 = "19 June"
    expected_formatted_date1 = "19/Jun/2021"

    unformatted_date2 = "26 June"
    expected_formatted_date2 = "26/Jun/2021"

    # test format_date function with valid dates with missing year
    assert format_date(unformatted_date1) == expected_formatted_date1
    assert format_date(unformatted_date2) == expected_formatted_date2


def test_format_date_invalid_date():

    unformatted_date1 = "18 June"
    unformatted_date2 = "18-June-2021"

    # test format_date function with invalid dates
    assert format_date(unformatted_date1) == "N/A"
    assert format_date(unformatted_date2) == "N/A"
