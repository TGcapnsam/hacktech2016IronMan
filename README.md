### hacktech2016IronMan
	Bin, Jeff, Phat, Sam

#### File description
- small_parser.py is a parser that parse through the data of linkedin
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
 
