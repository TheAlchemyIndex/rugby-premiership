from srs.premiership.constants import OriginalColumns
from srs.premiership.scraper.pagehtml.HtmlParser import parse
from srs.premiership.scraper.formatters.TeamNameFormatter import team_name_formatter
from srs.premiership.scraper.formatters.ScoreFormatter import score_formatter
from srs.premiership.scraper.pagehtml.TagExtractor import tag_extractor
from srs.premiership.scraper.formatters.DateFormatter import date_formatter
from srs.premiership.scraper.formatters.MatchDetailsFormatter import match_details_formatter

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


def scrape_results(url):
    """Takes a url, scrapes and parses the html data from it and returns a key: value dictionary of data about
    matches.

    :param url: The url to be scraped
    :return: A key: value dictionary of data about individual matches
    """
    # Extracts data in div tags from url
    divs = parse(url)

    # Creates list of information about each match from divs
    data = tag_extractor(divs)

    results = []
    count = 0

    while count < len(data):
        # Extracts date and time information
        extract_date = date_formatter(data[count], url)
        date = extract_date[OriginalColumns.DATE]
        time = extract_date[OriginalColumns.TIME]
        hour = extract_date[OriginalColumns.HOUR]
        day = extract_date[OriginalColumns.DAY]
        year = extract_date[OriginalColumns.YEAR]
        month = extract_date[OriginalColumns.MONTH]
        season = extract_date[OriginalColumns.SEASON]

        # Extracts venue and referee information
        extract_match_details = match_details_formatter(data[count + 4])
        venue = extract_match_details[OriginalColumns.VENUE]
        referee = extract_match_details[OriginalColumns.REFEREE]

        # Extracts team information
        team1_name = team_name_formatter(data[count + 1])
        team2_name = team_name_formatter(data[count + 3])

        # Extracts score information
        score = score_formatter(data[count + 2])
        team1_score = score[OriginalColumns.TEAM1_SCORE]
        team2_score = score[OriginalColumns.TEAM2_SCORE]
        total_score = score[OriginalColumns.TOTAL_SCORE]
        winner = score[OriginalColumns.WINNER]
        extra_time = score[OriginalColumns.EXTRA_TIME]

        # Creates dictionary of match_data information and appends to results list
        match_data = {OriginalColumns.DATE: date, OriginalColumns.TIME: time, OriginalColumns.TEAM1_NAME: team1_name,
                      OriginalColumns.TEAM1_SCORE: team1_score, OriginalColumns.TEAM2_NAME: team2_name,
                      OriginalColumns.TEAM2_SCORE: team2_score, OriginalColumns.VENUE: venue,
                      OriginalColumns.REFEREE: referee, OriginalColumns.TOTAL_SCORE: total_score,
                      OriginalColumns.WINNER: winner, OriginalColumns.EXTRA_TIME: extra_time,
                      OriginalColumns.HOUR: hour, OriginalColumns.DAY: day, OriginalColumns.MONTH: month,
                      OriginalColumns.YEAR: year, OriginalColumns.SEASON: season}
        results.append(match_data)

        # count is incremented to look at the data for the next match
        count += 5

    return results
