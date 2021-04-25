import socket, cv2,pickle,struct,time
from threading import Thread


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host_ip = '10.0.1.1'
print('HOST IP:',host_ip)
port = 9999
socket_address= (host_ip,port)

server_socket.bind(socket_address)

server_socket.listen(5)
print("listening at",socket_address)

class StreamClass(object):
    def __init__(self):
        self.vid = cv2.VideoCapture(0)
        
        
        self.thread = Thread(target=self.read_frames, args=())
        self.thread.daemon = True
        self.thread.start()
        
        self.thread2=Thread(target=self.send_frames,args=())
        #this is not a daemon thread. If there is a problem in main thread and it stops displaying video locally, the sending of frames need not stop and it continues.
        

    def read_frames(self):
        
        self.client_socket,addr =server_socket.accept()
        
        self.thread2.start() #start thread that sends frames
        
        print("got connection from",addr)
        while True:
            if self.vid.isOpened():
                (self.img, self.frame) = self.vid.read()

    def display_locally(self):
        
        self.frame=cv2.resize(self.frame,(500,400))
        cv2.imshow('TRANSMITTING VIDEO', self.frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)
            
    
    def send_frames(self):
        while(True):
            try:
                self.frame=cv2.resize(self.frame,(500,400))
                a=pickle.dumps(self.frame)
                msg=struct.pack("Q",len(a))+a
                self.client_socket.sendall(msg)
            except AttributeError:
                pass
        
if __name__ == '__main__':
	stream_object=StreamClass()
	while True:
	    try:
	    	stream_object.display_locally()
	    except AttributeError:
        	pass
