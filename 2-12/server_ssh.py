# Author : GAO
#服务器端

'''
ftp server
1 读取文件名 2 检测文件是否存在 3 打开文件 4 检测文件大小 5 发送文件大小给客户端
6 等客户端确认 7 开始边读边发数据  8 发送md5
'''
import socket,os,time
import hashlib
server = socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待❤新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break

        cmd,filename = data.split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,"rb")
            m = hashlib.md5()
            file_size=os.stat(filename).st_size
            #md5 验证
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5",m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())

        print("send done")

server.close()

'''
print("执行指令：",data)
        #接收字符串，执行结果也是字符串
        cmd_res = os.popen(data.decode()).read()
        print("before send",len(cmd_res))

        if len(cmd_res) == 0:
            cmd_res = "cmd has no output...."
        #如果内容太多，（缓冲区）一次发不完，还会接着在第二次发完
        conn.send( str(len(cmd_res.encode())).encode('utf-8')) #先发大小给客户端

        print(str(len(cmd_res)).encode('utf-8'))
        #time.sleep(0.5)  #解决粘包问题 1。time.sleep(0.5)
        client_ack = conn.recv(1024) #wait client to confirm

        conn.send(cmd_res.encode('utf-8'))
'''


