import socket, cv2,pickle,struct

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host_ip = '10.0.1.1'
print('HOST IP:',host_ip)
port = 9999
socket_address= (host_ip,port)

server_socket.bind(socket_address)

server_socket.listen(5)
print("listening at",socket_address)


while True:
    client_socket,addr =server_socket.accept()
    print("got connection from",addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while vid.isOpened():
            img,frame =  vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
