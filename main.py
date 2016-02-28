import small_parser
import urllib2

# download the website file
url = "https://www.linkedin.com/in/bin-peng-79b99296?trk=nav_responsive_tab_profile_pic"
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open(url)
html_content = response.read()
#print html_content

# parse the content of the website and download the picture
# rename the picture into icon.jpg
content = small_parser.parse_html(html_content)
print content


