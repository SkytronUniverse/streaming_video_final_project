from socket import *
import cv2
import sys
import pickle
import struct
from imutils.video import FPS
import imutils

# ==============================
#           Constants
# ------------------------------
HOST = '127.0.0.1'
PORT = 8000
MAX_BUFF_SIZE = 4096


# ==============================
#    Create receiver sockets
# ------------------------------
receiver = socket(AF_INET, SOCK_STREAM)
receiver.bind((HOST, PORT)) # TODO: send/receive to/from remote machine
receiver.listen()
(comm_socket, sender_addr) = receiver.accept()


# ==============================
#         Receive frames
# ------------------------------
raw_data = b''
frame_size_delim = struct.calcsize('L') # unsigned long (8 bytes)
fps = FPS().start()
while True:
	# ==============================
	#     Get pickled_frame len
	# ------------------------------
	while len(raw_data) < frame_size_delim:
		raw_data += comm_socket.recv(MAX_BUFF_SIZE)

	frame_len = raw_data[:frame_size_delim] # struct.pack('L', len(serialized_frame))
	raw_data = raw_data[frame_size_delim:]

	frame_len = struct.unpack('L', frame_len)[0] # unpack frame_len

	# ==============================
	#      Get frame as bytes
	# ------------------------------
	while len(raw_data) < frame_len:
		raw_data += comm_socket.recv(MAX_BUFF_SIZE)
	frame_data = raw_data[:frame_len]

	# ==============================
	#        Get next frame
	# ------------------------------
	next_frame = raw_data[frame_len:]
	raw_data = next_frame

	current_frame = pickle.loads(frame_data) # deserialize frame

	if not len(raw_data): # Exit, no more frame data
		break
	else:
		# ==============================
		#     Show frame with OpenCV
		# ------------------------------
		current_frame = imutils.resize(current_frame, width=750) # enlarge frame
		cv2.imshow('current_frame', current_frame) # show frame
		cv2.waitKey(25) # Attempting the keep frame rate around 30 fps

	if cv2.waitKey(1) & 0xFF == ord('q'): # Exit condition by OpenCV
		break
	fps.update()

# ==============================
#            Clean up
# ------------------------------
fps.stop()
print("Approximate Frames per Second (FPS): {:.2f}".format(fps.fps()))
comm_socket.close() # Close socket with sender
cv2.destroyAllWindows()
receiver.close()