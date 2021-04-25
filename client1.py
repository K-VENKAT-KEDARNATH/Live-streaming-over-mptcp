import socket ,cv2,pickle,struct
import threading
import imutils
import ffmpy
import os
camera = False

if camera == True:
    vid = cv2.VideoCapture(0)
else:
    input_name = 'videos/teen.mp4'
    output_name = 'videos/teen_out.mp4'
    inp={input_name:None}
    outp = {output_name:'-vcodec libx264 -crf 32'}
    ff=ffmpy.FFmpeg(inputs=inp,outputs=outp,global_options='-n')
    if not os.path.exists('videos/teen_out.mp4'):
        ff.run()
    vid = cv2.VideoCapture('videos/teen_out.mp4')

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '10.0.1.1'
port = 9999
client_socket.connect((host_ip,port))

def send():
	if client_socket:
	    while(vid.isOpened()):
               try:
                   image,frame = vid.read()
                   frame = imutils.resize(frame,width = 380)
                   a = pickle.dumps(frame)
                   message = struct.pack("Q",len(a)) + a
                   client_socket.sendall(message)
                   key = cv2.waitKey(1) & 0xFF
                   if key == ord('q') :
                   	client_socket.close()
               except :
                   print('VIDEO FINISHED')
                   break
		    
		  
def receive():
	data = b""
	payload_size = struct.calcsize("Q")
	while True:
		while len(data) < payload_size:
			packet = client_socket.recv(4*1024) # 4K
			if not packet: break
			data+=packet
		packed_msg_size = data[:payload_size]
		data = data[payload_size:]
		msg_size = struct.unpack("Q",packed_msg_size)[0]
		
		while len(data) < msg_size:
			data += client_socket.recv(4*1024)
		frame_data = data[:msg_size]
		data  = data[msg_size:]
		frame = pickle.loads(frame_data)
		cv2.imshow("RECEIVING VIDEO FROM SERVER",frame)
		key = cv2.waitKey(1) & 0xFF
		if key  == ord('q'):
			break
			
			
thread = threading.Thread(target= send)
thread1= threading.Thread(target= receive)	
thread.start()
thread1.start()


	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
