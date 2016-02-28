import urllib2
import urllib
import re
import os

def get_image_from_google(keyword):
	
	# space and + is the same
	new_key_word = keyword.replace(" ", "+")
	url_pre_header = "https://www.google.com/search?safe=active&tbm=isch&q="
	new_url = url_pre_header + new_key_word

	# get the webpage source code
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	response = opener.open(new_url)
	html_content = response.read()
	
	f = open("test.html", "w")
	f.write(html_content)
	f.close()

	# parse the image url out
	image_list = html_content
	reg_expr = "src=\"(.*?(?:))\""
	image_url_list = re.findall(reg_expr, image_list)

	# download the image using the url
	# and save to the folder named using keyword
	if not os.path.exists(keyword):
		os.mkdir(keyword, 0755)
	else:
		os.system("rm " + keyword + "/*")

	for single_url in image_url_list:
		os.system("wget --directory-prefix="+ keyword + " " + single_url)
			
	# rename
	counter = 0
	import subprocess
	for i in subprocess.check_output("ls " + keyword, shell=True).split("\n"):
		if i is not "":
			os.system("mv " + keyword + "/" + i + " " + keyword + "/" + str(counter) + ".jpg")
			counter += 1

get_image_from_google("bin+peng")
