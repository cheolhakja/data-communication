from socket import *

'''
코드 serverSocket.listen(1) 1은 서버가 동시에 처리할 수 있는 대기 중인 연결 큐(==줄, 순서)의 최대 길이를 지정합니다. 
이 값은 아직 서버에서 수락되지 않은 대기 중인 들어오는 연결의 최대 길이를 나타냅니다.

listen(1)은 서버 소켓을 들어오는 연결을 대기하도록 설정하고 한 번에 하나의 연결만 대기열에 있도록 허용합니다. 
첫 번째 연결이 처리되는 동안 두 번째 연결 시도가 발생하면 두 번째 연결은 거부되거나 첫 번째 연결이 수락되거나 닫힐 때까지 대기 상태에 있게 됩니다.
-> 그래서 20개의 연결을 위해 21개의 소켓이필요하구나
'''
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))


serverSocket.listen(1)
print( 'The server is ready to receive')

response_msg = "HTTP/0.1 {} {}" #.format(server_ip)

while True:
    connectionSocket, addr = serverSocket.accept() #요청받기 대기상태. 
    msg = connectionSocket.recv(1024).decode()#바로 recv하는게 아님

    msg_size_bytes = len(msg)
    print(f"Size of HTTP message: {msg_size_bytes} bytes")

    splited_msg = msg.split(' ')
    http_method = splited_msg[0]
    final_msg = None

    if(http_method == 'GET'):
        final_msg = response_msg.format("200", "OK") #msg 생성
    elif(http_method == 'POST'):
        final_msg = response_msg.format("404", "NOT FOUND")
    else:
        final_msg = response_msg.format("400", "BAD REQUEST")
    connectionSocket.send(final_msg.encode())

    connectionSocket.close()