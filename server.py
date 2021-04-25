import socket,cv2,pickle,struct
import imutils
import threading
import cv2
import ffmpy
import os

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '10.0.1.1'
print('Host ip:',host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at",socket_address)

def start_video_stream(addr,client_socket):
	camera = False
	if camera == True:
		vid=cv2.VideoCapture(0)
	else:
		input_name = 'videos/peng.mp4'
		output_name = 'videos/peng_out.mp4'
		inp={input_name:None}
		outp = {output_name:'-vcodec libx264 -crf 32'}
		ff=ffmpy.FFmpeg(inputs=inp,outputs=outp,global_options='-n')
		if not os.path.exists('videos/peng_out.mp4'):
        		ff.run()
		vid = cv2.VideoCapture('videos/peng.mp4')
	try:
		print('client connected'.format(addr))
		if client_socket:
			while(vid.isOpened()):
				img,frame=vid.read()
				frame = imutils.resize(frame,width=320)
				a = pickle.dumps(frame)
				message = struct.pack("Q",len(a))+a
				client_socket.sendall(message)
				#cv2.imshow('transmitting to cache server',frame)
				#key = cv2.waitKey(1) & 0xFF
				#if key == ord('q'):
					#client_socket.close()
					#break
	except Exception as e:
		print(e)
		print(f"cache server {addr} disconnected")
		pass

def show_client(addr, client_socket):
    try:
        print('client connected'.format(addr))
        if client_socket:
            data = b""
            payload_size = struct.calcsize("Q")
            while True:
                while len(data) <payload_size:
                    packet = client_socket.recv(4*1024)
                    if not packet :break
                    data += packet
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q",packed_msg_size)[0]

                while len(data) <msg_size:
                    data += client_socket.recv(4*1024)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)
                text = f"CLIENT: {addr}"
                #frame = ps.putBText(frame,text,10,10,vspace=10,hspace =1,font_scale=0.7,
                                    #background_RGB=(255,0,0), text_RGB=(255,250,250))
                cv2.imshow(f"From {addr}",frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
            client_socket.close()
    except Exception as e:
        print(e)
        print(f"client {addr} disconnected")
        pass

while True:
    client_socket,addr = server_socket.accept()
    thread = threading.Thread(target= show_client,args = (addr,client_socket))
    thread1 = threading.Thread(target= start_video_stream,args = (addr,client_socket))
    thread.start()
    thread1.start()
    print("Total clients are",threading.activeCount()-1)
