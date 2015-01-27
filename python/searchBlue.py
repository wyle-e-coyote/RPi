from lightblue import *

#devices = finddevices(getnames=True, length=10)
devices = findservices()

for dev in devices:
    print "Found: ", dev
