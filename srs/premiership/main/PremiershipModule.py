from srs.premiership.main.wikipedia.calculations import CalculationModule
from srs.premiership.main.wikipedia.scraper import ScrapingModule


def main():
    ScrapingModule.write("recent", 2014, 15, 23)
    #CalculationModule.create_calculated_columns(2014, 15, 16)


if __name__ == "__main__":
    main()
