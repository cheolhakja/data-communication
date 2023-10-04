#UDP server
#이런것을 echo server라고 부른다. 

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort)) #서버 소켓을 바인딩할 IP 주소를 지정하는 것입니다. 이 경우 빈 문자열 ''을 IP 주소로 사용하는 것은 서버 소켓을 호스트 컴퓨터의 모든 사용 가능한 네트워크 인터페이스에 바인딩하도록 지정하는 것입니다.

print ("The server is ready to receive")

while(True):
    msg, clientAddr = serverSocket.recvfrom(2048) # receive up to 2048 bytes of data at a time.
    '''
    clientIP, clientPort = clientAddr
    '''
    modifiedmsg = msg.decode().upper() #Decode the bytes using the codec registered for encoding.
    serverSocket.sendto(modifiedmsg.encode(), clientAddr)

    