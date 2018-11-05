#ORIGINAL APP BY NSK B3
import socket
class Browser:
	def __init__(self):
		pass
	@classmethod
	def Browse(self):
		while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			page = raw_input("[+] Server IP: ")
			port = input("[+] PyPage (Port): ")
			if page and port != None:
				try:
					s.connect((page, port))
					data = s.recv(65536)
					if "End of this PyPage." in data:
						print(data)
						s.close()
						Browser.Browse()
				except socket.error:
					print "[-] That PyPage Doesn't exist!"
					Browser.Browse()
				except Exception as e:
					print "[+] An error occured:",e
if __name__ == '__main__':
	Browser.Browse()
