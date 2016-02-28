from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def mainpage():
	data1 = subprocess.check_output("ls ./static/bin+peng", shell=True).split("\n")
	data_list = []
	for i in data1:
		if i is not "":
			data_list.append({'val': "./static/bin+peng/" + i})
	print data_list
	return render_template('index.html', data = data_list)

if __name__ == '__main__':
	app.debug = True
	app.run()
