<img src="https://external-preview.redd.it/oLyEwm9EK-XtmSMBXiD371-G3ROSqNIV-YpchI-4VnQ.png?auto=webp&s=807c0719fb73482f53b37b391b6533174d5b2a0b" width="200" height="250">

## SSL and HTTPS
SSL (Secure Sockets Layer) and its successor, TLS (Transport Layer Security), are protocols that provide encryption and authentication for data transmitted over the internet.

HTTPS (Hypertext Transfer Protocol Secure) is a protocol that uses SSL/TLS to secure the communication between a web server and a client (typically a web browser).
When a user visits a website that uses HTTPS, their browser first establishes a secure connection with the web server using SSL/TLS. This ensures that all data transmitted between the two is encrypted and cannot be intercepted or tampered with by attackers. The web server then sends its digital certificate to the browser to authenticate its identity, which allows the user to verify that they are communicating with the intended website and not an impostor.

To set up SSL/TLS and HTTPS on a web server, you will need to obtain a digital certificate from a trusted certificate authority (CA) and configure your server to use it. This typically involves generating a private key and a certificate signing request (CSR), submitting the CSR to a CA, receiving a signed certificate in return, and configuring the web server to use the certificate.

After configuring SSL/TLS and HTTPS, it is important to regularly monitor and update the certificate to ensure the continued security of your website.

#### How to Setup SSL/HTTPS on HAProxy Load Balancer
##### Prerequisites
Before you begin, you will need the following:

* A running instance of HAProxy load balancer
* A domain name that points to your load balancer's IP address
* A valid SSL certificate for your domain name (you can obtain a free SSL certificate from Let's Encrypt)
#### Step 1: Install Certbot
Certbot is a free, open-source software tool that automates the process of obtaining and installing SSL certificates. You can install Certbot on your HAProxy load balancer by running the following commands:
```bash
sudo apt update
sudo apt install -y certbot python3-certbot-nginx
```

#### Step 2: Obtain SSL Certificate
To obtain an SSL certificate from Let's Encrypt using Certbot, run the following command:
```bash
netstat -na | grep ':80.*LISTEN'
```
you need to ensure that no service is listening on port 80. To check which services are listening on port 80

```bash
sudo systemctl stop haproxy
```
```bash
sudo certbot certonly --standalone -d www.your-domain_name.tech --non-interactive --agree-tos --email example@gmail.com
```
<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*F5iSC6unA47adVP9.png">

[For more information](https://mustaphaaliyugaladima.medium.com/how-to-setup-ssl-https-on-haproxy-load-balancer-a47bee7bc146)
