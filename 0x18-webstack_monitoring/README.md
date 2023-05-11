<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg">

## Webstack monitoring
Webstack monitoring is the process of monitoring the various components of a web application stack, including servers, applications, databases, and other infrastructure components. The goal of webstack monitoring is to ensure that the web application stack is running optimally and to identify and resolve issues before they become critical.

### Components of a Webstack Monitoring System
A webstack monitoring system typically consists of several components:
1. Monitoring Agents: These are software components that run on the servers and other infrastructure components that make up the web application stack. The agents collect performance data and send it to the monitoring server for analysis.

2. Monitoring Server: The monitoring server is the central component of the monitoring system. It receives performance data from the monitoring agents and stores it in a database. The monitoring server also performs analysis on the performance data and generates alerts when issues are detected.

3. Dashboard: The dashboard is a web interface that provides a visual representation of the performance data collected by the monitoring system. It allows system administrators to quickly identify performance issues and take corrective action.

4. Alerting System: The alerting system is responsible for sending notifications to system administrators when performance issues are detected. Notifications can be sent via email, SMS, or other messaging systems.

### DATADOG
Datadog is a cloud monitoring service that offers a range of monitoring tools to help you visualize, analyze, and troubleshoot your infrastructure. If you use Nginx as your web server, installing the Datadog agent can provide you with real-time metrics, alerts, and detailed performance insights. In this blog, we will go through the steps to install and use the Datadog agent on an Nginx server.

**Here is a step by step in solving the tasks**

1. Task 0 | Sign up for a free Datadog account. When signing up, for the location choose US1-East, fill in the form and move to the next part, choose a stack (preferable Nginx). For the question "Are you a Managed Service Provider / Hosting Provider?" it is best to choose yes. next step is installation .
	* click on Ubuntu, copy step one installation command
	* Log in to your web-01 server and paste the command 
	* Once done check if datadog is installed and running 
	```css
	sudo systemctl status datadog-agent
	```
	* If running, Datadog will let you know too with the  "waiting for an agent respond" and you'll be able to go t the next part (sometimes it takes few minutes)
	* Next go to organization setting click on API KEYS( if  you don't have anything there, click on new key and generate one) once then copy the key(not the key id) and paste on your intranet
	* Do the same thing for the application key( same place you found API keys, Application is right under)
**DONE FOR TASK 0**

2. Task 1 |  To set up a monitor that checks the number of read requests issued to the server per second:
	* Navigate to the Monitor section in the side bar, click on New Monitor*, then click on *Metric.
	* Under Define the Metric, replace the default system.load.1 with "system.io.r_s", (This will prompt Datadog to monitor all the read requests made to the server)
	* Under Set alert conditions,** set the Alert threshold to 100
	* Under Notify your team set the Monitor name to something like READS PER SECOND, then set the message to "{{#is_alert}}Reads per second alert testif{{/is_alert}}"
	* Scroll all the way down and click on Create. This will successfully create a monitor that checks the read requests issued to the server per second
	![what it should look like](https://cdn.hashnode.com/res/hashnode/image/upload/v1683757512510/e8af203a-75e6-4d4a-b43b-ff1a68bf466c.png?auto=compress,format&format=webp)

To set up a monitor that checks the number of write requests issued to the device per second:

	* Navigate to the Monitor section in the side bar, click on New Monitor,** then on Metric.
	* Under Define the Metric, replace the default system.load.1 with "system.io.w_s"
	* Under Set alert conditions,** set the Alert threshold to 100
	* Under Notify your team set the Monitor name to something like WRITES PER SECOND, then set the message to "{{#is_alert}}Writes per second alert testif{{/is_alert}}"
	* Scroll all the way down and click on Create. This will successfully create a monitor that checks the write requests issued to the server per second.
**DONE**

3. Task 2 | Navigate to the Dashboards tab. Then, click on the New Dashboard button to create a new blank dashboard.

After you create a new dashboard, you can add widgets to it to display your data sources. To add a widget, click on the Add Widget button on the top-right corner of the dashboard, and select the type of widget you want to add, such as a time series graph, log stream, or alert graph.( Create 4, any of your choice but make sure it's 4)
	* To get the dashboard_id
	https://app.datadoghq.com/dashboard/by5-jsi-y67/ashlees-dashboard-thu-may-11-100824-am?from_ts=1683806670620&to_ts=1683810270620&live=true
	* copy the part of the URL after "dashboard/" and before the next forward slash, which in this case is "by5-jsi-y67"

**DONE**
