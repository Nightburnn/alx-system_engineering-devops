## 0x1A. Application server

1. Task 0: Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
Git clone your AirBnB_clone_v2 on your web-01 server.
Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
Your Flask application object must be named app (This will allow us to run and check your code).

	* Go to your web-01 server, clone Airbnb_clone_v2
	* Install pip3
	```bash
	sudo apt install python3-pip
	```

	* Check if pip3 is already installed by running the command:
	```css
	pip3 --version
	```

	* After pip3 is installed, you can use it to install Flask. Run the following command:
	```bash
	pip3 install flask
	```
After the installation is finished, you should be able to use Flask in your Python scripts. You can verify the installation by running a test script that imports Flask.

Remember to use pip3 instead of pip to ensure you're installing packages for Python 3 specifically.

	**Note** While trying to run flask on port 5000, i found out something else was running on port 5000
	here are a few steps in killing or stopping what is running on port 5000
	Stop the program using port 5000: Identify the program that is currently using port 5000 and stop it. This will free up the port so that you can use it for your Flask server. You can use the following command to identify the process using port 5000:
```css
sudo lsof -i :5000
```
This will show you the process ID (PID) of the program using port 5000. You can then use the PID to stop the program. For example, if the PID is 12345, you can stop it by running:
```bash
sudo kill 12345
```

	* Next step is configuring web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000
	* cd to the directory and open the file "0-hello_route.py"
	* change the port to 5000 and the route to /airbnb-onepage/
```python
#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/')
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(port=5000)
```

Have two terminals open 
in terminal 1:
```bash
ubuntu@150523-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app '0-hello_route'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [16/May/2023 02:09:04] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```
in terminal 2:
```bash
ubuntu@150523-web-01:~/AirBnB_clone_v2/web_flask$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@150523-web-01:~/AirBnB_clone_v2/web_flask$
```

--------------------------------------------------------------------------------------------------------------
2. Task 1:
