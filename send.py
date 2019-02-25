from socket import *
import cv2
import sys, errno
import pickle
import struct

# ==============================
#           Constants
# ------------------------------
HOST = '127.0.0.1'
PORT = 8000

# ==============================
#     Create sender socket
# ------------------------------
sender = socket(AF_INET, SOCK_STREAM)
try:
	sender.connect((HOST, PORT)) # send to remote machine
except IOError as e:
	print("Something went wrong:",e)
	sender.close()
	sys.exit(1)


# ==============================
#          Send frames
# ------------------------------
cap = cv2.VideoCapture('me_at_the_zoo.mp4')

while True:
	# frame is a <class 'numpy.ndarray'>, representing a frame
	(ret, frame) = cap.read() # ret == True if no error during video read
	serialized_frame = pickle.dumps(frame) #serialze frame

	# ==============================
	#       Create byte string
	# ------------------------------
	packed_frame = struct.pack('L', len(serialized_frame)) + serialized_frame

	# Make best effort to handle broken pipe errors
	try:
		sender.sendall(packed_frame)
	except IOError as e:
		if e.errno == errno.EPIPE:
			print( e, "- Try rerunning the program.")
			sender.close()
			sys.exit(2)
		else:
			print("Something else went wrong, exiting program: ", e)
			sender.close()
			sys.exit(3)

	if not ret:
		break


# ==============================
#            Clean up
# ------------------------------
cap.release()
sender.close()