# Live-streaming-over-mptcp
 
***Initial Setup***
 
The server sends live video, and the client receives it.

To run -> 
run simpleTopo.py. 
On the host h1, run the server code. 
On the host h2, run the client code.

 
**Improved version**
 
This setup is similar to the video streaming apps like google meet or zoom, where the server starts and multiple clients connect to it. The server sends a video that is visible to many clients. Clients have their video which they send, and the server can see videos of multiple clients.
 
To run -> 

run simpleTopo.py

start the server from host h1

clients from other hosts.

 
The videos are encoded into x264 before sending, compressing the video, and reducing the number of packets/data to send.

(We have done everything on a single PC so for multiple clients multiple cameras are required which is a shortage in our case and hence we are sending pre existing mp4 videos)
 
**Improvement at server PC**
 
Server PC may run many applications at a time. The current application adds extra stress to that. To reduce that, we have used multi-threading, where three threads perform simultaneously.
 
thread1->captures video frames.
 
Main thread->displays captured frames locally.
 
thread2->sends captured frames.
 
Doing this gives better performance at server PC, but the requirement of improving at the network layer is still pending...
