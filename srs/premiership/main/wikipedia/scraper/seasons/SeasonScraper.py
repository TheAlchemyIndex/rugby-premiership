from srs.premiership.main.wikipedia.constants.matchData import Teams, ScoringTypes, TeamTypes
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.scoringDataFormatter.ScoringDataFormatter import \
    scoring_data_formatter
from srs.premiership.main.wikipedia.scraper.pageHtml.HtmlParser import parse
from srs.premiership.main.wikipedia.scraper.formatters.teamNameFormatter.TeamNameFormatter import \
    team_name_formatter
from srs.premiership.main.wikipedia.scraper.formatters.scoreFormatter.ScoreFormatter import score_formatter
from srs.premiership.main.wikipedia.scraper.pageHtml.TagExtractor import extract_tags
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.DateFormatter import date_formatter
from srs.premiership.main.wikipedia.scraper.formatters.matchDetailsFormatter.MatchDetailsFormatter import \
    match_details_formatter


def scrape_results(url):
    """Takes a url, scrapes and parses the html data from it and returns a key: value dictionary of data about
    matches.

    :param url: The url to be scraped
    :return: A key: value dictionary of data about individual matches
    """
    # Extracts data in div tags from url
    divs = parse(url)

    # Creates list of information about each match from divs
    data = extract_tags(divs)

    results = []
    count = 0

    while count < len(data):
        # Extracts match result information
        score = score_formatter(data[count + 2])
        team1_points = score[OriginalColumns.TEAM1_POINTS]
        team2_points = score[OriginalColumns.TEAM2_POINTS]
        total_points = score[OriginalColumns.TOTAL_POINTS]
        result = score[OriginalColumns.RESULT][0]
        result_flipped = score[OriginalColumns.RESULT][1]
        extra_time = score[OriginalColumns.EXTRA_TIME]

        # Extracts scoring data
        try:
            # If scoring data is in index of count + 5, then both teams scored in the match
            if ("Try" in data[count + 5]) | ("Pen" in data[count + 5]) | ("Con" in data[count + 5]) | (
                    "Drop" in data[count + 5]):
                team1_scoring_data = data.pop(count + 4)
                team2_scoring_data = data.pop(count + 4)
            # Otherwise one team didn't score anything
            elif ("Try" in data[count + 4]) | ("Pen" in data[count + 4]) | ("Con" in data[count + 4]) | (
                    "Drop" in data[count + 4]):
                # If team1 scored no points, then the data in index of count + 4 relates to team2
                if int(team1_points) == 0:
                    team2_scoring_data = data.pop(count + 4)
                    team1_scoring_data = ""
                # Otherwise the data in index of count + 4 relates to team1
                else:
                    team1_scoring_data = data.pop(count + 4)
                    team2_scoring_data = ""
            else:
                team1_scoring_data = ""
                team2_scoring_data = ""
        except IndexError:
            team1_scoring_data = ""
            team2_scoring_data = ""

        # Extracts tries, conversions, penalties and drop goals for both teams
        extract_team1_scoring_data = scoring_data_formatter(team1_scoring_data)
        team1_tries = extract_team1_scoring_data[ScoringTypes.TRIES]
        team1_conversions = extract_team1_scoring_data[ScoringTypes.CONVERSIONS]
        team1_penalties = extract_team1_scoring_data[ScoringTypes.PENALTIES]
        team1_drop_goals = extract_team1_scoring_data[ScoringTypes.DROP_GOALS]
        extract_team2_scoring_data = scoring_data_formatter(team2_scoring_data)
        team2_tries = extract_team2_scoring_data[ScoringTypes.TRIES]
        team2_conversions = extract_team2_scoring_data[ScoringTypes.CONVERSIONS]
        team2_penalties = extract_team2_scoring_data[ScoringTypes.PENALTIES]
        team2_drop_goals = extract_team2_scoring_data[ScoringTypes.DROP_GOALS]

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

        # Extracts team and bonus point information
        team1_name, team1_bps = team_name_formatter(data[count + 1])
        team2_name, team2_bps = team_name_formatter(data[count + 3])

        # Fixes any incorrect match data - based on manual inspection of Wikipedia
        if (date == "02/Sep/2016") & (team1_name == Teams.WASPS) & (team2_name == Teams.SALE):
            date = "02/Sep/2017"
            year = "2017"
        elif (date == "08/Oct/2016") & (team1_name == Teams.HARLEQUINS) & (team1_penalties != 5):
            team1_penalties = 5
        elif (date == "28/Oct/2016") & (team2_name == Teams.GLOUCESTER) & (team2_penalties != 2):
            team2_penalties = 2
        elif (date == "24/Dec/2016") & (team1_name == Teams.SARACENS) & (team1_penalties != 3):
            team1_penalties = 3
        elif (date == "29/Sep/2017") & (team2_name == Teams.SARACENS) & (team2_penalties != 2):
            team2_penalties = 2
        elif (date == "07/Oct/2017") & (team1_name == Teams.GLOUCESTER) & (team1_tries != 5):
            team1_tries = 5
        elif (date == "09/Feb/2018") & (team2_name == Teams.NORTHAMPTON) & (team2_points != 9):
            team2_points = 9
        elif (date == "01/Sep/2018") & (team2_name == Teams.WASPS) & (team2_penalties != 3):
            team2_penalties = 3
        elif (date == "02/Dec/2018") & (team2_name == Teams.SALE) & (team2_tries != 1):
            team2_penalties = 1
        elif (date == "22/Dec/2018") & (team2_name == Teams.HARLEQUINS) & (team2_penalties != 4):
            team2_penalties = 4
        elif (date == "07/Apr/2019") & (team2_name == Teams.GLOUCESTER) & (team2_tries != 6):
            team2_tries = 6
        elif (date == "10/Nov/2019") & (team1_name == Teams.LONDON_IRISH) & (team1_penalties != 1):
            team1_penalties = 1
        elif (date == "30/Sep/2020") & (team1_name == Teams.BRISTOL) & (team1_tries != 6):
            team1_tries = 6
        elif (date == "21/Nov/2020") & (team1_name == Teams.LEICESTER) & (team1_penalties != 4):
            team1_penalties = 4
        elif (date == "20/Feb/2021") & (team1_name == Teams.LEICESTER) & (team1_penalties != 4):
            team1_penalties = 4
        elif (date == "17/May/2021") & (team1_name == Teams.BRISTOL) & (team1_tries != 5):
            team1_tries = 5
        elif (date == "30/May/2021") & (team1_name == Teams.WORCESTER) & (team2_name == Teams.LEICESTER):
            date = "29/May/2021"
        elif (date == "26/Jun/2021") & (team1_name == Teams.EXETER) & (team1_penalties != 1):
            team1_penalties = 1
        elif (date == "02/Oct/2021") & (team1_name == Teams.NEWCASTLE) & (team1_penalties != 2):
            team1_penalties = 2
        elif (date == "03/Oct/2021") & (team2_name == Teams.EXETER) & (team2_penalties != 2):
            team2_penalties = 2
        elif (date == "09/Oct/2021") & (team1_name == Teams.GLOUCESTER) & (team1_drop_goals != 1):
            team1_drop_goals = 1
        elif (date == "08/Jan/2022") & (team2_name == Teams.NORTHAMPTON) & (team2_drop_goals != 1):
            team2_drop_goals = 1
        elif (date == "28/Jan/2022") & (team1_name == Teams.EXETER) & (team2_name == Teams.GLOUCESTER):
            date = "28/Jan/2023"
        elif (date == "29/Jan/2022") & (team1_name == Teams.LONDON_IRISH) & (team2_name == Teams.HARLEQUINS):
            date = "29/Jan/2023"

        # Creates dictionary of match_data information and appends to results list
        match_data = {OriginalColumns.DATE: date,
                      OriginalColumns.TIME: time,
                      OriginalColumns.TEAM1_NAME: team1_name,
                      OriginalColumns.TEAM1_POINTS: team1_points,
                      OriginalColumns.TEAM2_NAME: team2_name,
                      OriginalColumns.TEAM2_POINTS: team2_points,
                      OriginalColumns.VENUE: venue,
                      OriginalColumns.TEAM_TYPE: TeamTypes.HOME,
                      OriginalColumns.REFEREE: referee,
                      OriginalColumns.TOTAL_POINTS: total_points,
                      OriginalColumns.RESULT: result,
                      OriginalColumns.EXTRA_TIME: extra_time,
                      OriginalColumns.HOUR: hour,
                      OriginalColumns.DAY: day,
                      OriginalColumns.MONTH: month,
                      OriginalColumns.YEAR: year,
                      OriginalColumns.SEASON: season,
                      OriginalColumns.TEAM1_BPS: team1_bps,
                      OriginalColumns.TEAM2_BPS: team2_bps,
                      OriginalColumns.TEAM1_TRIES: team1_tries,
                      OriginalColumns.TEAM1_CONVERSIONS: team1_conversions,
                      OriginalColumns.TEAM1_PENALTIES: team1_penalties,
                      OriginalColumns.TEAM1_DROP_GOALS: team1_drop_goals,
                      OriginalColumns.TEAM2_TRIES: team2_tries,
                      OriginalColumns.TEAM2_CONVERSIONS: team2_conversions,
                      OriginalColumns.TEAM2_PENALTIES: team2_penalties,
                      OriginalColumns.TEAM2_DROP_GOALS: team2_drop_goals}
        match_data_reversed = {OriginalColumns.DATE: date,
                               OriginalColumns.TIME: time,
                               OriginalColumns.TEAM1_NAME: team2_name,
                               OriginalColumns.TEAM1_POINTS: team2_points,
                               OriginalColumns.TEAM2_NAME: team1_name,
                               OriginalColumns.TEAM2_POINTS: team1_points,
                               OriginalColumns.VENUE: venue,
                               OriginalColumns.TEAM_TYPE: TeamTypes.AWAY,
                               OriginalColumns.REFEREE: referee,
                               OriginalColumns.TOTAL_POINTS: total_points,
                               OriginalColumns.RESULT: result_flipped,
                               OriginalColumns.EXTRA_TIME: extra_time,
                               OriginalColumns.HOUR: hour,
                               OriginalColumns.DAY: day,
                               OriginalColumns.MONTH: month,
                               OriginalColumns.YEAR: year,
                               OriginalColumns.SEASON: season,
                               OriginalColumns.TEAM1_BPS: team2_bps,
                               OriginalColumns.TEAM2_BPS: team1_bps,
                               OriginalColumns.TEAM1_TRIES: team2_tries,
                               OriginalColumns.TEAM1_CONVERSIONS: team2_conversions,
                               OriginalColumns.TEAM1_PENALTIES: team2_penalties,
                               OriginalColumns.TEAM1_DROP_GOALS: team2_drop_goals,
                               OriginalColumns.TEAM2_TRIES: team1_tries,
                               OriginalColumns.TEAM2_CONVERSIONS: team1_conversions,
                               OriginalColumns.TEAM2_PENALTIES: team1_penalties,
                               OriginalColumns.TEAM2_DROP_GOALS: team1_drop_goals}
        results.append(match_data)
        results.append(match_data_reversed)

        # count is incremented to look at the data for the next match
        count += 5

    return results
