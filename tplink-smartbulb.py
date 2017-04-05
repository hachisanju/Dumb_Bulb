#!/usr/bin/env python
# 
#  
# This code is HEAVILY based on tplink_smartplug.py by 
# Lubomir Stroetmann and is Copyrighted 2016 softScheck GmbH
# The original source code is under the Apache License:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# It can be found here:
#
# https://github.com/softScheck/tplink-smartplug
#
#
# If you wanna take my modifications, alone (?) without the
# original code, you can consider it WTFPL
#
#											-hachisanju
#

import socket
import argparse

version = 0.1

# Check if IP is valid
def validIP(ip):
	try:
		socket.inet_pton(socket.AF_INET, ip)
	except socket.error:
		parser.error("Invalid IP Address.")
	return ip 

commands = {'info'     : '{"system":{"get_sysinfo":{}}}',
			'on'       : '{"smartlife.iot.smartbulb.lightingservice":{"transition_light_state":{"on_off":1}}}',
			'off'      : '{"smartlife.iot.smartbulb.lightingservice":{"transition_light_state":{"on_off":0}}}'
}

# Encryption and Decryption of TP-Link Smart Home Protocol
# XOR Autokey Cipher with starting key = 171
def encrypt(string):
	key = 171
	result = ""
	for i in string: 
		a = key ^ ord(i)
		key = a
		result += chr(a)
	return result

def decrypt(string):
	key = 171 
	result = ""
	for i in string: 
		a = key ^ ord(i)
		key = ord(i) 
		result += chr(a)
	return result

# Parse commandline arguments
parser = argparse.ArgumentParser(description="TP-Link Wi-Fi Smart Plug Client v" + str(version))
parser.add_argument("-t", "--target", metavar="<ip>", required=True, help="Target IP Address", type=validIP)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--command", metavar="<command>", help="Preset command to send. Choices are: "+", ".join(commands), choices=commands) 
group.add_argument("-j", "--json", metavar="<JSON string>", help="Full JSON string of command to send")
args = parser.parse_args()

# Set target IP, port and command to send
ip = args.target
port = 9999
if args.command is None:
	cmd = args.json
else:
	cmd = commands[args.command]

# Send command and receive reply 
try:
	
	sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock_udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock_udp.sendto(encrypt(cmd), (ip, port))
	print "Sent:     ", cmd
        data = sock_udp.recv(1024)

        print "Received: ", decrypt(data[4:])


except socket.error:
	quit("Cound not connect to host " + ip + ":" + str(port))
