# EXPLANED

A user wants to access a website hosted on a one server web infrastructure(this is becoming a hard word to spell or maybe it's just my brain) via www.foobar.com

### questions asked:
  1. What is a server:  In this a case the server will host the website and store the web application, database, and any other files that are necessary
  2. What is the role of the domain name: the domain name foobar.com is configured to point to the ip address of the server hosting the website
  3. What type of DNS record www is in www.foobar.com: the www record for foobar.com is configured to point to the ip address of the server hosting the website
  4. What is the role of the web server: the web server is NGINX, which will recieve request from the user's web browser and deliver the website's web pages 
  5. What is the role of the application server: The application server will execute the codebase for the website's web application
  6. What is the role of the database: the database is Mysql which will store the website's data
  7. What is the server using to communicate with the computer of the user requesting the website: the server will use the HTTP protocol to communicate with the user's computer requesting the website. The web server will recieve the user's request via HTTP, process it and respond with the appropriate web pages 


### what the issues are with this infrastructure:
   1. SOP: Since it relies on a single server, it is a **Single Point Of Failure** (SOP). if the server goes down, the website will become unavaialbale , and user will not be able to connect or access it.
 
2. Downtime when maintenance needed (like deploying new code web server needs to be restarted): During maintenance or update the server needs to be restarted, causing downtime and distrupting access to the website
3. Cannot scale if too much incoming traffic: if the website recieves too much traffic, the infrastructure will not be able to handle it,leading to crashes or a slow loading time. since this infrastructure only has a single server the scaling options are limited
