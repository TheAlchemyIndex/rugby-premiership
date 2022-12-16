from rp.gallagher.scraper.pagehtml.HtmlParser import parse
from rp.gallagher.scraper.formatters.TeamNameFormatter import team_name_formatter
from rp.gallagher.scraper.formatters.ScoreFormatter import score_formatter
from rp.gallagher.scraper.pagehtml.TagExtractor import tag_extractor
from rp.gallagher.scraper.formatters.DateFormatter import date_formatter
from rp.gallagher.scraper.formatters.MatchDetailsFormatter import match_details_formatter

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


def scrape_results(url):

    # Extracts data in div tags from url
    divs = parse(url)
    # Creates list of information about each match from divs
    data = tag_extractor(divs)
    # Empty list to store dictionaries of results
    results = []

    # Count for looping through data list
    count = 0

    # Loop continues until count equals length of data list
    while count < len(data):
        # Extracts date and time information
        extract_date = date_formatter(data[count], url)
        date = extract_date["date"]
        time = extract_date["time"]
        year = extract_date["year"]
        month = extract_date["month"]
        season = extract_date["season"]

        # Extracts venue and referee information
        extract_match_details = match_details_formatter(data[count + 4])
        venue = extract_match_details["venue"]
        referee = extract_match_details["referee"]

        # Extracts team information
        team1_name = team_name_formatter(data[count + 1])
        team2_name = team_name_formatter(data[count + 3])

        # Extracts score information
        score = score_formatter(data[count + 2])
        team1_score = score["team1_score"]
        team2_score = score["team2_score"]
        total_score = score["total_score"]
        winner = score["winner"]
        extra_time = score["extraTime"]

        # Creates dictionary of result information and appends to results list
        result = {"date": date, "time": time, "team1Name": team1_name, "team1Score": team1_score,
                  "team2Name": team2_name, "team2Score": team2_score, "venue": venue,
                  "referee": referee, "totalScore": total_score, "winner": winner,
                  "extraTime": extra_time, "month": month, "year": year, "season": season}
        results.append(result)

        # count is incremented to look at the data for the next match
        count += 5

    # Returns list of dictionaries with match results
    return results

