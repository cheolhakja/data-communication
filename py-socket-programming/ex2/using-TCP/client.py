from socket import *
import time

serverName = "127.0.0.1"
serverPort = 12000

msg1 = "GET /index.html HTTP/1.1\r\nHost: www-net.cs.umass.edu\r\nUser-Agent: Firefox/3.6.10\r\nAccept: text/html,application/xhtml+xml\r\n"
msg2 = "POST /index.html HTTP/1.1\r\nHost: www-net.cs.umass.edu\r\nUser-Agent: Firefox/3.6.10\r\nAccept: text/html,application/xhtml+xml\r\n"
msg3 = "DELETE /index.html HTTP/1.1\r\nHost: www-net.cs.umass.edu\r\nUser-Agent: Firefox/3.6.10\r\nAccept: text/html,application/xhtml+xml\r\n"
msgs = [msg1, msg2, msg3]

for i in msgs:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort)) #연결을 보낼떄마다 해야되나, handshake
    clientSocket.send(i.encode())
    response_msg = clientSocket.recv(1024)
    print ("----------From Server----------", response_msg.decode('ascii'))
    time.sleep(5)

    clientSocket.close() #아.. 이게 문제였구나

'''
OSError: [WinError 10056] 이미 연결된 소켓에서 다른 연결을 요청했습니다
이미 연결된 소켓을 닫지 않고 여전히 사용하려고 시도하는 경우.
이미 사용 중인 포트 번호로 새로운 소켓을 생성하려고 시도하는 경우.
한 번에 여러 개의 소켓을 동시에 사용하고자 할 때, 연결이 이미 존재하는 소켓과 충돌하는 경우.
'''
