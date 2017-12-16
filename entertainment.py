import fresh_tomatoes
import media


# first movie arguments
thor = media.Movie(
  "Thor Ragnarok",
  "Imprisoned on the other side of the universe,"
  "the mighty Thor finds himself in a deadly gladiatorial "
  "contest that pits him against the Hulk, his former "
  "ally and fellow Avenger",
  "https://s-media-cache-ak0.pinimg.com/originals/19/c5/0e/19c50e32afad4fb81558d57296645da8.jpg",  #NOQA
  "https://www.youtube.com/watch?v=H84al-zYhq8")  #NOQA

# second movie arguments
fast_and_furious = media.Movie("fast and furious 8",
                               "With Dom and Letty married, "
                               "Brian and Mia retired and the rest of the crew exonerated,"
                               " the globe-trotting team has found some semblance of a normal "
                               "life. They soon face an unexpected challenge when a mysterious "
                               "woman named Cipher forces Dom to betray them all."
                               " Now, they must unite to bring home the man who made them a "
                               "family and stop Cipher from unleashing chaos.",
                               "http://uvchoice.com/wp-content/uploads/2017/10/FAST-FURIOUS-8.jpg",  #NOQA
                               "https://www.youtube.com/watch?v=t83YU-vOwak")  #NOQA

# third movie arguments
titanic = media.Movie("Titanic",
                      "Seventeen-year-old Rose hails from an aristocratic"
                      " family and is set to be married. When she boards the "
                      "Titanic, she meets Jack Dawson, an artist, and falls in love with him.",
                      "https://s-media-cache-ak0.pinimg.com/originals/94/85/56/9485569d77badd96a1ec1d95c280ffc8.jpg",  #NOQA
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")  #NOQA

# making an array/list of movies
movies = [thor, fast_and_furious, titanic]

# passing movies list to fresh tomatoes
fresh_tomatoes.open_movies_page(movies)
