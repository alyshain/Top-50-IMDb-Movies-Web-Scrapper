from input import input_from_user
from scrapper import imdb_scrapper


def main():
    """
    Main function that prompts user for a uear and scrapes the IMDb website for
    the top 50 movies from that year

    :return: None
    """
    # Prompts user for input
    year_from_user = input_from_user()

    # Prints user input
    print(f"Showing movies for the year {year_from_user}:")

    # Scraps the IMDb website for the list of movies for the specified year
    movies = imdb_scrapper(year_from_user)

    # Prints the scrapped movies
    for movie in movies:
        print(movie)

if __name__ == "__main__":
    main()
