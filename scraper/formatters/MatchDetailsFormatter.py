from re import search

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


# Function for formatting venue and referee details
def match_details_formatter(match_data):
    details_split = match_data.split(BR_REPLACE)
    venue = details_split[0]
    check_for_referee = list(filter(lambda v: search('^Referee', v), details_split))
    if len(check_for_referee) > 0:
        referee = check_for_referee[0].split("Referee: ")[1]
    else:
        referee = "N/A"

    formatted_match_details = {"venue": venue, "referee": referee}

    return formatted_match_details
