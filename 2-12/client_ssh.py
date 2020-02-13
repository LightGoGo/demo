# Author : GAO
#客户端  模拟ssh连接
import socket
import hashlib
client = socket.socket()
client.connect(('localhost',9999))

while True:
    cmd = input('>>:').strip()

    if len(cmd)==0:
        continue

    if cmd.startswith("get"): #接收文件
        client.send(cmd.encode('utf-8'))
        server_response= client.recv(1024)
        print("server response:",server_response)

        client.send(b"ready to recv file")
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename+".new","wb")
        m = hashlib.md5()

        while received_size < file_total_size:
            data = client.recv(1024)
            received_size += len(data)
            m.update(data)
            f.write(data)
            #print(file_total_size,received_size)
        else:
            new_file_md5 = m.hexdigest()
            print("file recv done",received_size,file_total_size)
            f.close()

        server_file_md5 = client.recv(1024)
        print("server file md5:",server_file_md5)
        print("client file md5:", new_file_md5)


client.close()

'''

while True:
    cmd = input('>>:').strip()
    if len(cmd)==0:
        continue
    client.send(cmd.encode('utf-8'))

    cmd_res_size = client.recv(1024) #接收大小
    print('命令结果大小：',cmd_res_size)

    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data) #每次收到的有可能小于1024，必须用len判断
        received_data += data

    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())
'''