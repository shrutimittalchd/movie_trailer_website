import webbrowser  # it will be later used to open the url of trailer


class Movie():
    """ this class Movie will take the arguments in __init__ and open the trailer in show_trailer """"
    
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ This function will initialize the variables """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This function will open the youtube link of the trailer """
        webbrowser.open(self.trailer_youtube_url)
