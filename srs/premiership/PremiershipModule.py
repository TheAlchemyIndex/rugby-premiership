from srs.premiership.wikipedia.calculations import CalculationModule
from srs.premiership.wikipedia.scraper import ScrapingModule


def main():
    #ScrapingModule.write("both", 2014, 15, 23)
    CalculationModule.create_calculated_columns(2014, 15, 23)


if __name__ == "__main__":
    main()
