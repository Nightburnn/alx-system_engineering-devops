## Explained

                                +-----------+
                                |  Load     |
                                |  Balancer |
                                +-----------+
                                       |
                  +--------------------------------+
                  |                |               |
           +---------+      +---------+      +---------+
           |  Web    |      | App     |      | App     |
           |  Server |      | Server  |      | Server  |
           +---------+      +---------+      +---------+
                  |                |               |
                  |                |               |
           +---------+      +--------------+
           |         |      |              |
           |  MySQL  |      |  Application |
           |         |      |  Files       |
           +---------+      +--------------+


* What distribution algorithm your load balancer is configured with and how it works:
  A load balancer distributes incoming traffic to multiple servers to ensure that no single server becomes overloaded. By using a load balancer, we can improve the performance, availability, and scalability of the web infrastructure. For this i am using HAProxy, HAProxy is a widely used, open-source load balancer that offers high performance, scalability, and flexibility. It supports various distribution algorithms, including round-robin, least connections, and IP hash, among others. Additionally, HAProxy can perform health checks on the servers to ensure that they are healthy before forwarding traffic to them, which helps to ensure that the web infrastructure is highly available. 

* The setup enabled by the load-balancer:
  Active-Passive Setup, HAProxy can be configured to enable an active-passive setup, in which only one server is active at any given time, while the other server is in standby mode. The active server handles all incoming requests, while the passive server is ready to take over in case the active server fails.

* How a database Primary-Replica (Master-Slave) cluster works:
  A Primary-Replica (or Master-Slave) database cluster is a setup in which one database node acts as the primary or master node, while one or more database nodes act as replica or slave nodes. The primary node is responsible for accepting read and write requests from the application and processing them, while the replica nodes replicate the data from the primary node and serve read-only requests from the application.

* The difference between the Primary node and the Replica node in regard to the application:
  1. Read-Write Access: The primary node is responsible for handling both read and write requests from the application, while replica nodes are typically only used for read-only requests. This is because the primary node is the only node that can accept write requests and update the database. The replica nodes replicate the data from the primary node and can serve read requests, but they cannot accept write requests.

  2. Data Consistency: Since the primary node is the only node that can accept write requests, it is responsible for ensuring data consistency across the database. Any changes made to the data are made on the primary node first, and then propagated to the replica nodes. This ensures that the data is consistent across all nodes in the cluster.

 3. Replication Lag: Replica nodes may experience some degree of replication lag, which is the delay between when data is updated on the primary node and when it is replicated to the replica nodes. This can result in slightly stale data being served by replica nodes, which can be acceptable for read-only operations. However, it can lead to data inconsistency if the replica nodes are not kept up-to-date.

 4. Failover: In case the primary node fails, one of the replica nodes is promoted to become the new primary node. This process can take some time, during which the database may be unavailable or have limited functionality. Applications need to be designed to handle such events and switch to the new primary node once it is available.

     Overall, the primary node and replica nodes in a Primary-Replica database cluster have different roles in terms of read-write access, data consistency, replication lag, and failover. Understanding these differences is essential for designing applications that use Primary-Replica database clusters.


### Issues With This Infrastructure

 1. There are multiple SPOF (Single Point Of Failure).
For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.

 2. Security issues.
The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.

 3. No monitoring.
We have no way of knowing the status of each server since they're not being monitored.
