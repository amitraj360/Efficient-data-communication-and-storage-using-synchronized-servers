import socket
import unittest

host="127.0.0.1"
port=5000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

class check_tracker(unittest.TestCase):
	def test_check_alive(self):
		s.send("check#alive")
		data = s.recv(1024)
		self.assertEqual(str(data),"Alive")
		print("\nInfo:\n"+data)

	def test_check_share(self):
		s.send("share#123#127.0.0.1:3000#myfile.cpp")
		data=s.recv(1024)
		self.assertTrue(str(data) == "SUCCESSFULLY SHARED" or str(data) == "FILE ALREADY SHARED")
		print("\nInfo:\n"+data)

	def test_check_get(self):
		s.send("get#12")
		data=s.recv(1024)
		self.assertTrue(data or str(data) == "No Client found for this File !!!")
		print("\nInfo:\n"+data)

	def test_check_remove(self):
		s.send("remove#123#127.0.0.1:3000")
		data=s.recv(1024)
		self.assertTrue(str(data) == "FILE SUCCESSFULLY REMOVED" or str(data) == "FILE WAS NOT SHARED")
		print("\nInfo:\n"+data)

#s.send("share#123#mt")
#data=s.recv(1024)
#print(data)

if __name__ == '__main__':
	unittest.main()