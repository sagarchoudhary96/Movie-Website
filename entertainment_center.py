# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

Captain_america = media.Movie("Captain America",
                        "&#9733 &#9733 &#9733 &#9733",
                        "http://ia.media-imdb.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=1L3c17AmCZw")

interstellar = media.Movie("Interstellar",
                     "&#9733 &#9733 &#9733",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "https://www.youtube.com/watch?v=zSWdZVtXT7E")

batman = media.Movie("Batman Vs Superman",
                     "&#9733 &#9733 ",
                     "http://ia.media-imdb.com/images/M/MV5BNTE5NzU3MTYzOF5BMl5BanBnXkFtZTgwNTM5NjQxODE@._V1_.jpg",
                     "https://www.youtube.com/watch?v=eX_iASz1Si8")

rio_2 = media.Movie("Rio 2",
                     "&#9733 &#9733 &#9733",
                     "https://upload.wikimedia.org/wikipedia/en/6/67/Rio_2_Poster.JPG",
                     "https://www.youtube.com/watch?v=sOwvE40hsjc")

smurf = media.Movie("Smurfs 2",
                     "&#9733 &#9733",
                     "https://upload.wikimedia.org/wikipedia/en/1/19/The_Smurfs_2_poster.jpg",
                     "https://www.youtube.com/watch?v=Kh1PTKTgCDk")

kingsman = media.Movie("Kingsman",
                     "&#9733 &#9733 &#9733 &#9733",
                     " https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg",
                     "https://www.youtube.com/watch?v=m4NCribDx4U")

movies = [Captain_america, rio_2, batman, interstellar, smurf, kingsman]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.valid_ratings)
# to print class name ---> print media.Movie.__name__
# to print class doc ---> print media.Movie.__doc__
#to print module name --->print media.Movie.__module__
