### hacktech2016IronMan
	Bin Peng, Jeff shaw, Phat, Sam

#### File description
- small_parser.py is a parser that parse through the data of linkedin
	- if b4 no found
		- use pip to install beautiful soup 4
- main.py is a program that use the url of a person in linkedin and download the html webpage. call the small_parser to parse it.
- get_image_from_google is used for using the name of the person in linkedin to search google gallery. get the top 20 result. and download them.
- webpage.py is used as the main program of flask(a python framework for building website)
	- in order to run the program. you will need to install Flask
		- and if they say that you need to install some other library, then install it.
	- the html file of the website will be put in the templates folder
	- the picture, js and css folder will be put in the static folder
- The file in the similarity_algorithm is used for judging whether two picture is similar
	- in order to use the program, you will need to in stall opencv in your computer with python support
	- if the value returned is bigger than 200, than the two picture is not the same person. else the person is the same.
	
- The icon.jpg file is crawl from linkedin using small_parser. and will be the base image when trying to compare with the other picture.

#### How to run?
- for the linkedin profile crawling and analysing
	- replace the value of variable url in the main.py file
	- then run `python main.py`
	- the return result will be a picture called `icon.jpg` and several string that contain the information you need
- for the google picture download part.
	- the input paramter for the function is the name(a string)
	- after that it will download the top 20 picture from google gallery
	- run `python get_google_image.py`

- for the website
	- simply run `python webpage.py`
	- then go to 127.0.0.1:5000
