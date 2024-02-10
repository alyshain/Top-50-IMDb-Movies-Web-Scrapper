import requests
from bs4 import BeautifulSoup


def imdb_scrapper(year_from_user):
    """
        Scrapes the IMDb website for the top 50 movie titles released in the specified year.

        Args:
        year_from_user (str): The year for which movies are to be searched.

        Returns:
        list: A list containing the titles of the top 50 movies released in the specified year.
              Returns an empty list if the URL cannot be fetched or if no movies are found.
    """
    url = f"https://www.imdb.com/search/title/?release_date={year_from_user}-01-01,{year_from_user}-12-31"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    # print("Response status code:", response.status_code)  # Add this line for debugging

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        movie_title_elements = soup.find_all("h3", class_="ipc-title__text")[
                               :50]  # Find all <h3> elements with the class "ipc-title__text" but only first 50 movies
        if not movie_title_elements:
            print("No movie titles found on the page.")
            return []
        movie_titles_list = [title.text.strip() for title in
                             movie_title_elements]  # Extract movie titles from the elements
        return movie_titles_list
    else:
        print("Failed to fetch given URL.")
        return []
