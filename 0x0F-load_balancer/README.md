## Load Balancer and HAProxy

### introduction

<img src="https://pbs.twimg.com/media/FPLhDgFXwAchgEf.jpg">

A load balancer is a device or software that distributes incoming network traffic across multiple servers to ensure that no single server is overloaded, thereby optimizing resource utilization, maximizing throughput, minimizing response time, and avoiding downtime. Load balancing is commonly used in web servers, application servers, and database servers to enhance performance, scalability, and availability.

HAProxy is a free, open-source load balancer and proxy server that can be used to distribute traffic among multiple servers based on a variety of algorithms such as round-robin, least connections, source IP, and more. HAProxy can handle HTTP, HTTPS, TCP, and SSL/TLS protocols, and supports session persistence, health checks, and SSL termination.

### Installing HAProxy on Ubuntu
To install HAProxy on Ubuntu, follow these steps:

1. Update the package index and install HAProxy:
```css
sudo apt update
sudo apt install haproxy
```
2. Verify the installation by checking the HAProxy version:
```css
haproxy -v
```
#### Configuring HAProxy
After installing HAProxy, you need to configure it to distribute traffic among your servers. The HAProxy configuration file is typically located at /etc/haproxy/haproxy.cfg. You can edit this file using a text editor to specify the IP addresses and ports of your servers, as well as the load balancing algorithm you want to use.

Here's an example HAProxy configuration that distributes traffic among two servers using the round-robin algorithm:

```bash
function install() {
	command -v "$1" &> /dev/null

	#shellcheck disable=SC2181
	if [ $? -ne 0 ]; then
		echo -e "	Installing: ${brown}$1${reset}\n"
		sudo apt-get update -y -qq && \
			sudo apt-get install -y "$1" -qq
		echo -e "\n"
	else
		echo -e "	${green}${1} is already installed.${reset}\n"
	fi
}

install haproxy #install haproxy

echo -e "\n${blue}Setting up some minor stuff.${reset}\n"

#backup default server config file
sudo cp /etc/haproxy/haproxy.cfg haproxy_default.backup

server_config=\
"
defaults
  mode http
  timeout client 15s
  timeout connect 10s
  timeout server 15s
  timeout http-request 10s

frontend clickviral-tech-frontend
    bind *:80
    default_backend clickviral-tech-backend

backend clickviral-tech-backend
    balance roundrobin
    server serverName ipAddress:80 check
    server  serverName ipAddress:80 check
"
//hellcheck disable=SC2154
echo "$server_config" | sudo dd status=none of=/etc/haproxy/haproxy.cfg

//enable haproxy to be started by init script
echo "ENABLED=1" | sudo dd status=none of=/etc/default/haproxy

if [ "$(pgrep -c haproxy)" -le 0 ]; then
	sudo service haproxy start
else
	sudo service haproxy restart
fi
```

To check if HAproxy is active and running:

```css
sudo systemctl status haproxy.service -l --no-pager
``` 
#### Conclusion
Load balancing is an essential technique for scaling and optimizing your servers, and HAProxy is a powerful and flexible tool for implementing load balancing in your infrastructure. With the above guide, you should now have a basic understanding of how to install, configure, and use HAProxy to distribute traffic among your servers.
