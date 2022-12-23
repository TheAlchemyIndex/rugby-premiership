from srs.premiership.calculations import CalculationModule
from srs.premiership.scraper import ScrapingModule


def main():
    #ScrapingModule.write("both", 2010, 11, 23)
    CalculationModule.create_calculated_columns(2010, 11, 23)


if __name__ == "__main__":
    main()
