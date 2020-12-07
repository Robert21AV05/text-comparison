import os
from flask import Flask, render_template, url_for
from flask.globals import request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/', methods=['POST'])
def compare():

	if request.method == 'POST':

		file1 = request.files['file1']
		if (file1.filename != ''):
			file1.save(secure_filename(file1.filename))
		else:
			raise Exception ("You did not give enough files to compare!" )    
		
		file2 = request.files['file2']
		if (file2.filename != ''):
			file2.save(secure_filename(file2.filename))
		else:
			raise Exception ("You did not give enough files to compare!" )   

		file1opened = open(file1.filename, "r")
		file2opened = open(file2.filename, "r")

		nameOfFile1 = file1.filename
		nameOfFile2 = file2.filename

		packs1 = file1opened.read().split()
		packs2 = file2opened.read().split()

		onlyFile1 = []
		onlyFile2 = []
		common = []

		for package in packs1:
			if (package in packs2):
				common.append(package)		
				packs1.remove(package)
				packs2.remove(package)
			else:
				onlyFile1.append(package)

		for package in packs2:
			if (package in packs1):
				common.append(package)
				packs1.remove(package)
				packs2.remove(package)
			else:
				onlyFile2.append(package)

		file1opened.close()
		file2opened.close()

		os.remove(file1.filename)
		os.remove(file2.filename)
		
		print(onlyFile1)
		print(onlyFile2)

		return render_template('index.html', onlyFile1=onlyFile1, onlyFile2=onlyFile2, nameOfFile1=nameOfFile1, nameOfFile2=nameOfFile2, common=common)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
