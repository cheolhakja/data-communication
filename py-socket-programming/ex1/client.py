from socket import *

serverName = "127.0.0.1" #루프백 ip
'''
같은 컴퓨터내에서 클라-서버 구조를 실행시킬때 자기자신 PC로 접속되는 루프백 ip
'''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
msg = input("서버로 보낼 메시지 입력: ")

clientSocket.sendto(msg.encode(), (serverName, serverPort))

modifiedMsg, serverAddr = clientSocket.recvfrom(2048)
print( modifiedMsg.decode())
clientSocket.close()