from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect, secure_filename
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
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

    
    return compare(file1.filename,file2.filename)

def compare(file1name,file2name):
    file1 = open(file1name, "r")
    file2 = open(file2name, "r")

    packs1 = file1.read().split()
    packs2 = file2.read().split()

    onlyFile1 = []
    onlyFile2 = []

    for package in packs1:
        if (package in packs2):
            packs1.remove(package)
            packs2.remove(package)
        else:
            onlyFile1.append(package)   
            #print(package, " exists only in ", file1.name)
                
    print("----------------------------------------------")
    for package in packs2:
        if (not(package in packs1)):
               
            #print(package, " exists only in ", file2.name)
            onlyFile2.append(package)
               
    print("----------------------------------------------")
    file1.close()
    file2.close()
    
    os.remove(file1name)
    os.remove(file2name)
    
    return """
<!DOCTYPE html>
<head>
   <title>Result</title>
</head>
    <h1>Comparison Result</h1>
    <p>only in %s --> %s</p>
    
    <p>only in %s --> %s</p>
    
</body>
"""    %(file2.name, onlyFile2, file1.name, onlyFile1)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
