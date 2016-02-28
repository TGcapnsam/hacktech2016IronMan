from PIL import Image
import math
import operator
import subprocess

# small than 200 is good, bigger than 200 means not the same guys
for i in subprocess.check_output("ls ../bin+peng/", shell=True).split("\n"):
	h1 = Image.open("../bin+peng/" + i).histogram()
	h2 = Image.open("icon.jpg").histogram()

	rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
	print rms
