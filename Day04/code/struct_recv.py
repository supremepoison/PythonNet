from socket import *
import struct

s = socket()
s.bind(('0.0.0.0',3698))
s.listen(25)

#确定数据结构
st = struct.Struct('i5sf')

c,addr = s.accept()
data = c.recv(1024)

#解析数据
data = st.unpack(data)
print(data)

c.close()
s.close()