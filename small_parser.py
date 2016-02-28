from bs4 import BeautifulSoup
import string
import re
import os
import urllib

def parse_html(html_content):
	
	# final output
	output = ""

	# convert the string into beatifulsoup object
	soup = BeautifulSoup(html_content, 'html.parser')

	# cut the name out
	name_str = soup.find_all("title")
	name = str(name_str[0]).replace("<title>", "").replace("</title>", "").replace(" | LinkedIn", "")
	print "Name : " + name

	# cut the picture out
	pic1 = soup.find_all("meta", {'property':'og:image'})
	pic_url = ""
	picture_url = ""
	pic_url = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(pic1))
	if pic_url is not None:
		picture_url = pic_url[0]
		urllib.urlretrieve(picture_url, "icon.jpg")

	# cut the number of connection out
	connection_number = 0
	connection = 0
	conn = soup.find_all("div", {'class':'member-connections'})
	if conn.__len__() > 0:
		for i in range(0, conn.__len__()):
			connstr = str(conn)
			conn1 = BeautifulSoup(connstr, 'html.parser')
			connection = conn1.strong.contents
			connection_number = connection[0]
	print "connections : " + str(connection_number)

	# cut the experience out
	expr_dict = {}
	expr = soup.find_all("section", {'id': 'experience'})
	expr_soup = BeautifulSoup(str(expr), 'html.parser')
	
	## find the time for the job
	expr_time = expr_soup.find_all("span", {'id': 'data-range'})
	expr_time_number = expr_time.__len__()
	if expr_time_number > 0:
		for i in range(0, expr_time_number):
			print type(expr_time[i])
	
	## find the job
	expr_list = expr_soup.find_all("a")
	expr_number = expr_list.__len__()
	
	expr_tuple_list = []
	if expr_number > 0:
		tmp_tuple_list = ()
		for i in range(0, expr_number):
			if "img" not in str(expr_list[i].contents):
				#print expr_list[i].contents
				continue
			else:
				tmp_tuple_list = (expr_list[i + 1].contents, expr_list[i + 2].contents)
				expr_tuple_list.append(tmp_tuple_list)
				i += 2
	print expr_tuple_list

	# cut the skill out
	skill = soup.find_all("section", {'id': 'skills'})
	skill_soup = BeautifulSoup(str(skill), 'html.parser')
	
	skill_list = skill_soup.find_all("span")
	skill_number = skill_list.__len__()
	
	final_skill_list = []
	if skill_number > 0:
		for i in range(0, skill_number):
			skill1 = str(skill_list[i])[19:].replace("</span>", "")
			final_skill_list.append(skill1)
	print final_skill_list

	# cut the education out
	educ = soup.find_all("section", {'id': 'education'})
	educ_soup = BeautifulSoup(str(educ), 'html.parser')

	educ_list = educ_soup.find_all("a")
	educ_number = educ_list.__len__()

	if educ_number > 0:
		for i in range(0, educ_number):
			educ1 = str(educ_list[i].contents)
			if "img" not in educ1:
				print educ1
