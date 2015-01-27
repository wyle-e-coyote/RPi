from lightblue import *
import select, json

s = socket()
s.bind(("",7))
s.listen(1)
advertise("RPi Bluetooth", s,RFCOMM)

print "Listening on %s port %s" % (s.getsockname()[0], s.getsockname()[1])

conn, addr = s.accept()
print "Connected by", addr
#result = conn.recv(1024)
result = select.select([conn], [], [], 10000)
data = None
if (result):
	data = conn.recv(1024)
conn.send('WTF?!?')
print "Data: ", data
decoded = json.loads(data)
print "Decoded: %d - %s" %(decoded['code'], decoded['coords'])
conn.close()
s.close()

