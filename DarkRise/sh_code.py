#!/usr/bin/python2
import sys

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("usage : %s <file>\n" % (sys.argv[0],))
		sys.exit(0)

	shellcode = "\""
	ctr = 1
	maxlenght = 15

	for b in open(sys.argv[1], "rb").read():
		shellcode += "\\x" + b.encode("hex")
		if ctr == maxlenght:
			shellcode += "\"\n\""
			ctr = 0
		ctr += 1
	shellcode += "\""
	print shellcode
