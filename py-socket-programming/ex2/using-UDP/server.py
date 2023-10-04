'''
HTTP는 안정적인 데이터 전송이 필요하기 때문에 일반적으로 TCP 프로토콜을 사용합니다. 
UDP(사용자 데이터그램 프로토콜)는 신뢰성과 순서 보장이 부족하기 때문에 HTTP 통신에 적합하지 않습니다. 
그러나 교육 또는 실험 목적으로 UDP를 사용하여 기본적인 HTTP와 유사한 통신을 시뮬레이션하려는 경우 간단한 예제를 만들 수 있습니다
'''

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort)) #서버 소켓을 바인딩할 IP 주소를 지정하는 것입니다. 이 경우 빈 문자열 ''을 IP 주소로 사용하는 것은 서버 소켓을 호스트 컴퓨터의 모든 사용 가능한 네트워크 인터페이스에 바인딩하도록 지정하는 것입니다.

print ("The server is ready to receive")

while(True):
    msg, clientAddr = serverSocket.recvfrom(2048) # receive up to 2048 bytes of data at a time.
    
    httpReq = msg.decode()
    



    serverSocket.sendto(modifiedmsg.encode(), clientAddr)

    