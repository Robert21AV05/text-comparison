Compare content of 2 files.

apt install python3
apt install python3-pip

pip3 install virtualenv

virtualenv environment

source environment/bin/activate

pip3 install flask

python3 app.py

Go to 0.0.0.0:5000/ and enter files to be compared.

##

To build Docker image

docker build --tag file-comparison .
docker run -p 5001:5000 file-comparison

Go to 0.0.0.0:5001/ and enter files to be compared.
