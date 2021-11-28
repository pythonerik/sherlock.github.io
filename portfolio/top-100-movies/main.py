from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

responce = requests.get(URL)
website_html = responce.text

soup = BeautifulSoup(website_html, "html.parser")

movie_list = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movie_list]
movies = movie_titles[::-1]

with open(r"C:\Users\ErikAranda-Wikman\Documents\100-Days-Of-Coding\Intermediate+\top-100-movies\movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

