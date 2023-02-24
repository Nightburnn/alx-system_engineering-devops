## Explained

                 +-------------+
                 |   Firewall 1 |
                 +-------------+
                           |
                           |
                 +-------------+
                 |   Firewall 2 |
                 +-------------+
                           |
                           |
                 +-------------+
                 |   Firewall 3 |
                 +-------------+
                           |
                           |
                 +-------------+                 +-------------------+
                 | Load Balancer|  <------HTTPS----|   www.foobar.com  |
                 +-------------+                 +-------------------+
                           |
                           |
                 +-------------+
                 |   Web Server |
                 +-------------+
                           |
                           |
                 +-------------+
                 |  MySQL DB   |
                 +-------------+




In this design, we have three firewalls to add layers of security and protect against different types of attacks. The firewalls act as a barrier between the internet and the web infrastructure, allowing only authorized traffic to pass through.

We use SSL to serve encrypted traffic to ensure that the data transmitted between the website and its users is protected from interception and tampering.

We also use monitoring to detect and alert on issues within the web infrastructure. We have three monitoring clients, which are data collectors for a monitoring service, such as Sumologic. These monitoring clients collect data from different components of the web infrastructure, such as the web server and MySQL database, and send it to the monitoring service for analysis and alerting.
To monitor the web server's QPS (Queries Per Second), we need to collect data on the number of queries the web server receives per second. This data can be collected by setting up monitoring for the web server, collecting metrics related to its performance, and analyzing those metrics to calculate the QPS.


### Specifics About This Infrastructure
1. The purpose of the firewalls:
   The purpose of firewalls in a web infrastructure is to add a layer of security by controlling access to the network and the services running on it. Firewalls act as a barrier between the internet and the web infrastructure, allowing only authorized traffic to pass through.

Firewalls typically use a set of rules to filter incoming and outgoing traffic based on specific criteria, such as the source and destination IP addresses, port numbers, and protocols. This helps to block malicious traffic and prevent attacks, such as DDoS attacks, port scanning, and unauthorized access attempts.

By using multiple firewalls, different layers of security can be added to the web infrastructure. For example, the first firewall might allow only HTTP and HTTPS traffic to pass through to the load balancer, while the second firewall might only allow MySQL traffic to pass through to the database server. This way, if one firewall is breached, there are still additional layers of protection in place to prevent a successful attack.

2. The purpose of the SSL certificate:
  The purpose of an SSL (Secure Sockets Layer) certificate in a web infrastructure is to provide encryption and authentication for the traffic between the website and its users. SSL is a protocol that uses encryption to protect sensitive information, such as login credentials, credit card details, and other personal data, from being intercepted or tampered with by attackers.

An SSL certificate is a digital certificate that authenticates the identity of a website and encrypts the data being transmitted between the website and the user's browser. When a user visits a website with an SSL certificate, their browser establishes a secure connection to the website's server and encrypts all data transmitted between them. This helps to protect the user's privacy and ensure the integrity of the data being transmitted.

3. The purpose of the monitoring clients:
   The purpose of monitoring clients in a web infrastructure is to collect and analyze data about the system's performance, availability, and security. Monitoring is essential for ensuring that the web infrastructure is running smoothly and is available to users at all times.

Monitoring clients can collect data from various sources, including servers, applications, network devices, and databases. This data can be used to identify and troubleshoot issues, such as server downtime, high server load, network congestion, or security breaches. Monitoring can also provide insights into system usage patterns, trends, and anomalies, which can help to optimize system performance and prevent future issues.


### Issues With This Infrastructure
* Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted.
* Having one MySQL server is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.
* Having servers with all the same components would make the components contend for resources on the server like CPU, Memory, I/O, etc., which can lead to poor performance and also make it difficult to locate the source of the problem. A setup such as this is not easily scalable.
