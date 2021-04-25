# Live-streaming-over-mptcp

**Initial Setup**
Server sends video and client recieves it.
To run -> run simpleTopo.py and on host h1 run the server code and on host h2 run client code

**Improved version**
This setup issimilar to the video streaming apps like google meet/zoom where in server starts and multiple clients can connect to it.
Server sends the video that can be seen by multiple clients 
Clients has their own video which is sent by clients and server can see the videos of multiple clients

To run -> rum simpleTopo.py and start server from host h1 and clients from other hosts

The videos are encoded into x264 before sending. This compresses the video thereby reducing the number of packets/data to be sent.

**Improvement at server PC**
Server PC may run many applications at a time and the current application adds extra stress on that.
To reduce that we have used multi-threading where in 3 threads perform simultaneously

thread1->captures video frames
main thread->displays captured frames locally
thread2->sends captured frames

This can help better performance at server PC but the requirement of improving at network layer is still pending
