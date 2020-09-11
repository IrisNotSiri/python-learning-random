s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, interface.encode())
s.settimeout(3)
try:
  s.connect(("ip.jsontest.com", 80))
except socket.error as err:
  logger.error("Could not get external ip for {}: {}".format(interface, err))

s.send(b"GET / HTTP/1.1\nHost: ip.jsontest.com\n\n")
s.settimeout(10)
external_ip = None
try:
    rec = s.recv(400)
except socket.timeout as err: 
    logger.debug("Didn't receive data! Error: {}".format(err))

s.close()