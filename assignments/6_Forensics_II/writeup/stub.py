import sys
import struct
import datetime 

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8badf00d
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
idx = 0
magic, version = struct.unpack("<LL", data[idx:idx+8])
idx += 8
time,_ = struct.unpack("<LL", data[idx:idx+8])
idx += 4
author= struct.unpack("<8s", data[idx:idx+8])
idx += 8
sec_count,_ = struct.unpack("<LL", data[idx: idx+8])
timestamp = datetime.datetime.fromtimestamp(time)
i = 0
if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("Time: %s" % str(timestamp))
print("Author: %s" % author )
print("Num of Sections: %d" % int(sec_count))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!
offset = 24
print("-------  BODY  -------")
for x in range(sec_count) :
	print("**********")
	stype, slen = struct.unpack("<LL", data[offset:offset+8])
	print(str(hex(stype)) + ' ' +  str(slen))
	if stype == 1:
		sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		print(sval[0])
	elif stype == 2:
		sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		print(sval)
	elif stype == 3:
		
		sval = struct.unpack("<" + str(slen / 4) + "L", data[offset+8:offset+8+slen / 4])
		print(sval)
	elif stype == 4:
		
		sval = struct.unpack("<" + str(slen / 8) + "Q", data[offset+8:offset+8+slen / 8])
		print(sval)
	elif stype == 5:
		
		sval = struct.unpack("<" + str(slen / 8) + "Q", data[offset+8:offset+8+slen / 8])
		print(sval)
	elif stype == 6:
	
		lat,lon = struct.unpack("dd",data[offset+8:offset+8 + slen])
		print("cord :  (%f,%f)" % (lat,lon))
	elif stype == 7:
		if slen == 4:
			sval = struct.unpack("<L", data[offset+8:offset+8 + slen])
			print(sval)
	elif stype == 8:
		png_header = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
		with open("image.png", 'wb') as f:
			f.write(png_header)
			f.write(data[offset+8:offset+8+slen])
		
		#print result
		print("Image found - named image.png")

		# offset = offset + slen

		# sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		# code = struct.pack('8L', 137,80,78,71,13,10,26,10)
		# png = code + data
	else:
		bork("Bad stype! Got %d, expected %d" % (int(slen) ))
	offset += 8 + slen 	
