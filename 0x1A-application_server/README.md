## 0x1A. Application server

1. Task 0: Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
Git clone your AirBnB_clone_v2 on your web-01 server.
Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
Your Flask application object must be named app (This will allow us to run and check your code).

	 Go to your web-01 server, clone Airbnb_clone_v2
	 Install pip3
	
```bash
sudo apt install python3-pip
```

	 Check if pip3 is already installed by running the command:

```css
pip3 --version
```

	 After pip3 is installed, you can use it to install Flask. Run the following command:

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
2. Task 1: Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

Requirements:

Install Gunicorn and any other libraries required by your application.
The Flask application object should be called app. (This will allow us to run and check your code)
You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.
In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.

	To Install Gunicorn on web-01 server Here are the steps:
	Navigate to the project directory that contains your Flask application.

	run the following command:

```css 
pip3 install gunicorn
```
check if anything is listening on port 6000

```bash
sudo lsof -i :6000
```

Then bind gunicorn

```bash
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
```

**Note** problems i faced. An Instance of flask was already running on port 5000 due to task 0, simple stop or kill the pid, also you can only bind gunicorn in the root Airbnb_clone_v2
so in the end 

on terminal 1:
```bash
$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2023-05-16 02:41:45 +0000] [1863114] [INFO] Starting gunicorn 20.1.0
[2023-05-16 02:41:45 +0000] [1863114] [INFO] Listening at: http://0.0.0.0:5000 (1863114)
[2023-05-16 02:41:45 +0000] [1863114] [INFO] Using worker: sync
[2023-05-16 02:41:45 +0000] [1863116] [INFO] Booting worker with pid: 1863116
```

on terminal 2:
```bash
ubuntu@150523-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@150523-web-01:~$
```
--------------------------------------------------------------------------------------------------------------------
3. TASK 2: Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/

Requirements:

Nginx must serve this page both locally and on its public IP on port 80.
Nginx should proxy requests to the process listening on port 5000.
Include your Nginx config file as 2-app_server-nginx_config.
Notes:

In order to test this you’ll have to spin up either your production or development application server (listening on port 5000)
In an actual production environment the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.
You will probably need to reboot your server (by using the command $ sudo reboot) to have Nginx publicly accessible

web-01
Create a file named 2-app_server-nginx_config, Save the file in the appropriate location for Nginx configuration files. This location may vary depending on your operating system and Nginx installation. Common locations include /etc/nginx/conf.d/ or /etc/nginx/sites-available/.
```bash
sudo cd  /etc.nginx/sites-available
```

to create the file 
```
sudo vi filename
```
cofiguration may look like this:

```css
# Configures Nginx to serve the route /airbnb-onepage/ from AirBnB_clone_v2.

server {
    # Listen on port 80
    listen      80 default_server;
    listen      [::]:80 default_server ipv6only=on;

    # Use IP of server as domain name
    server_name ipaddressforweb-01;

    # Customize HTTP response header
    add_header  X-Served-By whateverheaderyouwant;

    # Serve /airbnb-onepage/ route from AirBnB_clone_v2
    location = /airbnb-onepage/ {
        proxy_pass http://127.0.0.1:5000/airbnb-onepage/;
    }

    # 404 error page
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}
```


